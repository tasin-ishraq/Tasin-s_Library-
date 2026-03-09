# 📚 Digital Library - Static Website

A modern, responsive digital library website built with vanilla HTML, CSS, and JavaScript. Integrates with Google Drive for book storage and is hosted on GitHub Pages.

## 🚀 Features

- 📚 **Browse Books**: Organized by author and category
- 🔍 **Search Functionality**: Find books by title, author, or description
- 💾 **Download Books**: Direct download from Google Drive
- 📖 **Read Online**: Preview books directly in browser
- 📱 **Fully Responsive**: Works on all devices (mobile, tablet, desktop)
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- ⚡ **Fast Loading**: Static website with no backend required
- 🌐 **SEO Friendly**: Proper HTML semantic structure

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **API**: Google Drive API v3
- **Hosting**: GitHub Pages
- **Database**: Google Drive Folder
- **IDE**: Visual Studio Code

## 📋 Project Structure

```
digital-library/
├── index.html                 # Main HTML file
├── css/
│   ├── style.css             # Main styles
│   └── responsive.css        # Mobile responsive styles
├── js/
│   ├── config.js             # Configuration (API keys)
│   ├── google-drive-api.js    # Google Drive integration
│   ├── utils.js              # Utility functions
│   └── main.js               # Main application logic
├── assets/
│   └── images/               # Images folder
├── .github/
│   └── copilot-instructions.md
└── README.md                 # This file
```

## 🎯 Quick Start

### Prerequisites
- Google Account
- GitHub Account
- VS Code (optional but recommended)
- Google Drive folder with PDF/EPUB books

### Setup Steps

#### Step 1: Get Google API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Google Drive API
4. Create an API key (Web browser restriction)
5. Copy your API key

#### Step 2: Get Your Google Drive Folder ID
1. Open your Google Drive folder
2. Copy the folder ID from the URL: `https://drive.google.com/drive/folders/FOLDER_ID_HERE`

#### Step 3: Configure the Application
1. Open `js/config.js`
2. Replace:
   - `YOUR_GOOGLE_API_KEY_HERE` → Your Google API Key
   - `1wow9tOtg7eOvmLEKUxHNwmBUTvl4Nk1V` → Your Drive Folder ID

#### Step 4: Test Locally
1. Open `index.html` with VS Code Live Server
2. Check if books load from your Google Drive
3. Test search, filter, read, and download functions

#### Step 5: Create GitHub Repository
1. Go to GitHub and create a new repository
2. Name it: `digital-library` or any name you prefer
3. Clone it locally: `git clone <repository-url>`
4. Copy all files from this project to the cloned repository

#### Step 6: Deploy to GitHub Pages
1. Push files to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit: Digital Library"
   git push origin main
   ```
2. Go to Repository Settings → Pages
3. Select "main" branch as source
4. Your site will be available at: `https://yourusername.github.io/digital-library`

## 📖 How to Use

### For Users
1. **Browse Books**: Scroll through the books section
2. **Filter by Author**: Click on an author card
3. **Search**: Use the search bar (Ctrl+K shortcut)
4. **Read Online**: Click "📖 Read" button
5. **Download**: Click "📥 Download" button
6. **View Details**: Click a book card to see full details

### For Developers

#### Adding Books
1. Upload PDF/EPUB files to your Google Drive folder
2. Name files as: `Author Name - Book Title.pdf`
3. Refresh the website to see new books

#### Customizing UI
- Edit `css/style.css` for colors and styles
- Edit `index.html` for layout changes
- CSS Variables available in `:root` section

#### Categories
Books are auto-categorized based on keywords:
- **Fiction**: Novel, story, tale
- **Non-Fiction**: History, biography, self-help
- **Science**: Physics, chemistry, biology, science
- **Other**: Default category

## 🌐 API Integration Details

### Google Drive API Limits
- 1,000 requests per day (free tier)
- 10,000 requests per day (after request)
- File metadata is cached in local storage

### Book Metadata Extraction
- **Title**: From filename (removes extension)
- **Author**: Extracted from filename pattern
- **Category**: Auto-detected from keywords
- **Cover**: Drive file thumbnail or emoji

### File Formats Supported
- PDF (.pdf)
- EPUB (.epub)
- Text (.txt)
- MOBI (.mobi)

## 🔒 Security

- ✅ API key restricted to web browsers only
- ✅ Public books (no private data exposure)
- ✅ No user data collection
- ✅ HTTPS by default on GitHub Pages
- ✅ No backend server (static files only)

## 📱 Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🎨 Customization

### Colors
Edit in `css/style.css` `:root` section:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    /* ... other colors ... */
}
```

### Fonts
Change in `body` CSS rule:
```css
body {
    font-family: 'Any Google Font', sans-serif;
}
```

### Books Per Page
Edit in `js/config.js`:
```javascript
ITEMS_PER_PAGE: 12
```

## 🐛 Troubleshooting

### Books not loading?
1. Check Google API Key in `config.js`
2. Verify Drive Folder ID is correct
3. Check browser console for errors (F12)
4. Ensure Google Drive API is enabled

### Download not working?
1. Verify books have direct download enabled
2. Check file format is supported
3. Try different browser

### Search not working?
1. Clear browser cache
2. Check books are loaded first
3. Try exact author/title name

## 🚀 Deployment Checklist

- [ ] Google API Key added to `config.js`
- [ ] Google Drive Folder ID added to `config.js`
- [ ] Books uploaded to Google Drive folder
- [ ] GitHub repository created
- [ ] Files pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Website is live and accessible

## 📈 Future Enhancements

- [ ] User ratings and reviews
- [ ] Reading progress tracking (with localStorage)
- [ ] Reading list/bookmarks
- [ ] Multiple language support
- [ ] Dark mode toggle
- [ ] Advanced search filters
- [ ] Book recommendations
- [ ] Author profiles
- [ ] Social sharing buttons

## 📄 License

This project is open source and available under the MIT License.

## 🙋 Support

For issues or questions:
1. Check the troubleshooting section
2. Review browser console (F12)
3. Visit GitHub Issues
4. Check Google Drive API documentation

## 🎓 Learning Resources

- [HTML5 Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS3 Guide](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Google Drive API](https://developers.google.com/drive/api/v3/quickstart/js)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

---

**Created with ❤️ for book lovers and developers**

**Version**: 1.0.0  
**Last Updated**: March 2024
