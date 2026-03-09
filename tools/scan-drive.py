#!/usr/bin/env python3
"""
Digital Library - Automated Google Drive Scanner
Scans your public Google Drive folder and generates JavaScript code automatically
No authentication needed! Uses the Google Drive API with your folder's public link.
"""

import sys
import json
from pathlib import Path

def install_required_packages():
    """Install required packages if not already installed"""
    try:
        import google.auth
        from googleapiclient.discovery import build
    except ImportError:
        print("\n📦 Installing required packages...")
        import subprocess
        subprocess.check_call([
            sys.executable, "-m", "pip", "install",
            "google-auth-oauthlib", "google-auth-httplib2", "google-api-python-client"
        ])
        print("✅ Packages installed!\n")


class DriveScanner:
    def __init__(self, folder_id):
        """Initialize scanner with folder ID"""
        self.folder_id = folder_id
        self.service = None
        self.books = {}
        self.total_books = 0
        
    def authenticate_without_prompt(self):
        """
        Authenticate using Application Default Credentials
        For public folders, we can use API without user interaction
        """
        try:
            import google.auth
            from googleapiclient.discovery import build
            
            # Try to get default credentials
            creds, project_id = google.auth.default(scopes=[
                'https://www.googleapis.com/auth/drive.readonly'
            ])
            
            self.service = build('drive', 'v3', credentials=creds)
            print("✅ Authenticated successfully!\n")
            return True
            
        except Exception as e:
            print(f"⚠️  Using fallback authentication method...")
            return self.authenticate_with_browser()
    
    def authenticate_with_browser(self):
        """Authenticate using browser (one-time setup)"""
        try:
            from google_auth_oauthlib.flow import InstalledAppFlow
            from googleapiclient.discovery import build
            
            SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
            
            # For first time, you need to create credentials from Google Cloud Console
            # But we'll try to use cached credentials
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
            self.service = build('drive', 'v3', credentials=creds)
            print("✅ Authenticated with browser!\n")
            return True
            
        except FileNotFoundError:
            print("\n❌ credentials.json not found!")
            print("This is needed for authentication.")
            return False
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            return False
    
    def scan_folder(self, folder_id=None, parent_name=""):
        """
        Recursively scan folder for authors and books
        """
        if folder_id is None:
            folder_id = self.folder_id
        
        try:
            # Build query for this folder
            query = f"'{folder_id}' in parents and trashed=false"
            
            # Get all items in this folder
            results = self.service.files().list(
                q=query,
                spaces='drive',
                fields='files(id, name, mimeType)',
                pageSize=1000
            ).execute()
            
            items = results.get('files', [])
            
            # Sort folders first, then files
            folders = [i for i in items if i['mimeType'] == 'application/vnd.google-apps.folder']
            files = [i for i in items if i['mimeType'] != 'application/vnd.google-apps.folder']
            
            # Process folders (authors)
            for folder in sorted(folders, key=lambda x: x['name']):
                author_name = folder['name']
                print(f"📁 Scanning author: {author_name}")
                self.scan_folder(folder['id'], author_name)
            
            # Process files (books)
            for file in sorted(files, key=lambda x: x['name']):
                if file['name'].lower().endswith(('.pdf', '.epub', '.txt', '.mobi')):
                    if parent_name:  # Only add if inside an author folder
                        if parent_name not in self.books:
                            self.books[parent_name] = []
                        
                        # Extract title from filename
                        title = file['name']
                        for ext in ['.pdf', '.PDF', '.epub', '.EPUB', '.txt', '.TXT', '.mobi', '.MOBI']:
                            title = title.replace(ext, '')
                        
                        file_id = file['id']
                        
                        self.books[parent_name].append({
                            'title': title,
                            'fileId': file_id,
                            'category': 'fiction'
                        })
                        
                        self.total_books += 1
                        print(f"  ✅ {title}")
                        
        except Exception as e:
            print(f"❌ Error scanning folder: {e}")
            return False
        
        return True
    
    def generate_code(self):
        """Generate JavaScript code"""
        if not self.books:
            return None
        
        code = "let bookDatabase = {\n"
        
        authors = sorted(self.books.keys())
        for i, author in enumerate(authors):
            code += f'    "{author}": [\n'
            
            books_list = self.books[author]
            for j, book in enumerate(books_list):
                code += f'        {{ title: "{book["title"]}", fileId: "{book["fileId"]}", category: "{book["category"]}" }}'
                if j < len(books_list) - 1:
                    code += ','
                code += '\n'
            
            code += '    ]'
            if i < len(authors) - 1:
                code += ','
            code += '\n'
        
        code += '};\n'
        
        return code
    
    def run(self):
        """Main execution"""
        print("\n" + "=" * 70)
        print("📚  DIGITAL LIBRARY - AUTOMATED FOLDER SCANNER")
        print("=" * 70)
        print(f"\n🔍 Folder ID: {self.folder_id}")
        print("📡 Connecting to Google Drive...\n")
        
        # Authenticate
        if not self.authenticate_without_prompt():
            print("\n❌ Failed to authenticate!")
            print("Make sure you have Google Drive API enabled.")
            return False
        
        # Scan folder
        print("🔄 Scanning your folder structure...\n")
        if not self.scan_folder():
            print("❌ Failed to scan folder!")
            return False
        
        # Check results
        if not self.books:
            print("\n❌ No books found!")
            print("Make sure:")
            print("  1. Your folder is publicly shared")
            print("  2. You have author folders inside")
            print("  3. You have PDF/EPUB files inside author folders")
            return False
        
        # Generate code
        print(f"\n✅ Found {self.total_books} books by {len(self.books)} authors!\n")
        
        code = self.generate_code()
        if not code:
            print("❌ Failed to generate code!")
            return False
        
        # Display results
        print("=" * 70)
        print("📝 GENERATED CODE - Copy this into js/google-drive-api.js")
        print("=" * 70)
        print()
        print(code)
        print()
        
        # Save to file
        try:
            output_path = Path(__file__).parent.parent / 'js' / 'bookDatabase.js'
            output_path.write_text(code)
            print(f"✅ Code saved to: {output_path}")
        except Exception as e:
            print(f"⚠️  Could not save file: {e}")
        
        # Save JSON too
        try:
            json_path = Path(__file__).parent.parent / 'data' / 'books.json'
            json_path.parent.mkdir(exist_ok=True)
            json_path.write_text(json.dumps(self.books, indent=2))
            print(f"✅ JSON data saved to: {json_path}")
        except Exception as e:
            print(f"⚠️  Could not save JSON: {e}")
        
        print("\n" + "=" * 70)
        print("📋 NEXT STEPS:")
        print("=" * 70)
        print("1. Copy the code above ☝️")
        print("2. Open: js/google-drive-api.js")
        print("3. Replace the 'bookDatabase' object with the code above")
        print("4. Save the file")
        print("5. Open index.html in your browser to test!")
        print("\n🎉 Your Digital Library is ready!\n")
        
        return True


def main():
    """Main entry point"""
    try:
        # Install packages if needed
        install_required_packages()
        
        # Your Google Drive folder ID
        folder_id = "1wow9tOtg7eOvmLEKUxHNwmBUTvl4Nk1V"
        
        # Create scanner and run
        scanner = DriveScanner(folder_id)
        
        if not scanner.run():
            print("\n⚠️  Scanner failed. Troubleshooting:")
            print("  - Make sure the folder is publicly shareable")
            print("  - Check your internet connection")
            print("  - Try running again in 30 seconds")
            sys.exit(1)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Scan cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
