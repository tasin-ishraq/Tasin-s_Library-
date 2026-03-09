# 📚 Digital Library - Quick Setup Guide

## No Complex Setup Required! 🎉

This is a simplified version that works with public Google Drive links - no API keys, no authentication!

---

## **3 Easy Steps to Get Started**

### **Step 1: Make Your Google Drive Folder Public**

1. Open your folder: https://drive.google.com/drive/u/1/folders/1wow9tOtg7eOvmLEKUxHNwmBUTvl4Nk1V
2. Click **Share** button (top-right)
3. Click **"Change"** → Select **"Viewer"** → **"Anyone with the link"**
4. Click **Share** ✅

---

### **Step 2: Upload Your PDF Books**

1. Go to your Google Drive folder
2. Upload PDF files
3. **Folder structure** (optional but recommended):
   ```
   Your Folder/
   ├── William Shakespeare/
   │   ├── Hamlet.pdf
   │   └── Macbeth.pdf
   ├── George Orwell/
   │   ├── 1984.pdf
   │   └── Animal Farm.pdf
   └── Jane Austen/
       └── Pride and Prejudice.pdf
   ```

---

### **Step 3: Get File IDs and Add to Website**

#### How to Get a File's ID:

1. **Right-click** on your PDF file in Google Drive
2. Click **"Get link"**
3. Copy the link - it looks like: `https://drive.google.com/file/d/**FILE_ID_HERE**/view?usp=sharing`
4. **Extract the FILE_ID** (the long string between `/d/` and `/view`)

#### Example:
```
URL: https://drive.google.com/file/d/1a2b3c4d5e6f7g8h9i0j/view?usp=sharing
FILE_ID: 1a2b3c4d5e6f7g8h9i0j
```

---

### **Step 4: Add Books to Your Website**

Open: [js/google-drive-api.js](js/google-drive-api.js)

Find this section:
```javascript
let bookDatabase = {
    "William Shakespeare": [
        { title: "Hamlet", fileId: "FILE_ID_HERE", category: "fiction" },
        { title: "Macbeth", fileId: "FILE_ID_HERE", category: "fiction" }
    ],
    // ... more authors
};
```

Replace with your books:
```javascript
let bookDatabase = {
    "Your Author Name": [
        { title: "Book Title 1", fileId: "1a2b3c4d5e6f7g8h9i0j", category: "fiction" },
        { title: "Book Title 2", fileId: "2b3c4d5e6f7g8h9i0j1k", category: "fiction" }
    ],
    "Another Author": [
        { title: "Their Book", fileId: "3c4d5e6f7g8h9i0j1k2l", category: "non-fiction" }
    ]
};
```

**Categories**: `fiction`, `non-fiction`, `science`, `biography`

---

## **Example Setup**

Here's a complete example:

```javascript
let bookDatabase = {
    "Agatha Christie": [
        { title: "Murder on the Orient Express", fileId: "abc123def456", category: "fiction" },
        { title: "Death on the Nile", fileId: "ghi789jkl012", category: "fiction" }
    ],
    "Stephen Hawking": [
        { title: "A Brief History of Time", fileId: "mno345pqr678", category: "science" }
    ],
    "Sherlock Conan Doyle": [
        { title: "Sherlock Holmes", fileId: "stu901vwx234", category: "fiction" }
    ]
};
```

---

## **How It Works**

✅ Users visit your website  
✅ They see all books organized by author  
✅ They can search for books  
✅ They click "📖 Read" → Opens in Google Drive preview  
✅ They click "📥 Download" → Downloads the PDF  

**No passwords, no authentication, no complexity!**

---

## **Testing Locally**

1. After adding books to `google-drive-api.js`
2. Open `index.html` in your browser
3. Books should appear immediately
4. Test reading and download links

---

## **Tips**

- 📝 Keep filenames simple (no special characters)
- 🔤 Author names should match exactly (case-sensitive)
- 📚 Add as many books as you want
- 🔄 Changes appear immediately when you refresh

---

## **Troubleshooting**

### Books not showing?
- Refresh the page (F5)
- Check browser console (F12 → Console tab)
- Make sure FILE_IDs are correct
- Verify Google Drive folder is public

### Download link not working?
- Make sure PDF is uploaded to Google Drive
- Check FILE_ID is correct
- Try opening in incognito mode

### Preview not working?
- Google Drive preview may be blocked for some file types
- Download option will always work

---

## **Next Steps**

1. ✅ Add your books to `google-drive-api.js`
2. ✅ Test locally
3. ✅ Upload to GitHub
4. ✅ Enable GitHub Pages
5. ✅ Share your public link!

Done! 🎉
