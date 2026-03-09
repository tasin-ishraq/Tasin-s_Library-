# 🧪 Testing Checklist & Demo Guide

## Current Website Status: ✅ READY TO TEST

Your website is running at: **http://localhost:8000**

---

## 🎬 Interactive Demo Walkthrough

### Page 1: Welcome (index.html)
- **Colors:** White background with GREEN and RED buttons
- **Features:** 4 feature cards, stats section
- **CTA Button:** "Browse Library" → clicks to writers.html
- **Test:** Click "Browse Library"

### Page 2: Writers (writers.html)
- **Dynamic Loading:** Reads from js/data.js
- **Display:** 3 writers with bookshelves
- **Books:** Click ANY book to select it
- **Test:** Click on "Hamlet" or any book title

### Page 3: Book Detail (book.html)
- **Info Shown:** Book cover, title, author, file size
- **Two Buttons:** Read Online & Download
- **Breadcrumb:** Shows Home → Writers → Author → Book
- **Back Button:** Returns to Writers page
- **Test:** Try the back button

---

## ✨ Key Features to Test

| Feature | How to Test | Expected Result |
|---------|------------|-----------------|
| Welcome Page Colors | View index.html | Green & Red gradients |
| Book Selection | Click book on writers.html | Goes to book.html |
| Book Details | Click book | Shows title, author, file size |
| Back Navigation | Click back button | Returns to writers page |
| Responsive Design | Resize browser | Layout adapts to screen size |
| Hover Effects | Hover over books | Animation effect |
| Breadcrumb | Look at top | Shows navigation path |

---

## 🔗 Direct Links to Test

**Click these to jump to different pages:**

1. **Welcome Page:**  
   http://localhost:8000/

2. **Writers & Books:**  
   http://localhost:8000/writers.html

3. **Individual Book** (test with URL parameter):  
   http://localhost:8000/book.html?writer=William%20Shakespeare&book=Hamlet

---

## 📊 Data System Test

### Check if data.js is loading:

1. Open browser console (F12 or right-click → Inspect → Console)
2. Type: `getWriters()`
3. You should see: `["William Shakespeare", "George Orwell", "Jane Austen"]`

4. Type: `getWriterBooks("Jane Austen")`
5. You should see all of Jane Austen's books with fileIds and sizes

---

## ⚙️ Configuration for You to Do

### ❌ Not Yet Configured:
The Google Drive file IDs are set to `PASTE_FILE_ID_HERE`

### ✅ To Activate Read/Download:

1. **Get File IDs:**
   - Go to https://drive.google.com/drive/u/1/folders/1wow9tOtg7eOvmLEKUxHNwmBUTvl4Nk1V
   - Right-click any PDF
   - Click "Get Link"
   - Copy the ID between `/d/` and `/view`

2. **Update js/data.js:**
   ```javascript
   { 
       title: "Hamlet", 
       fileId: "ACTUAL_ID_HERE",  // ← Replace this
       size: "2.5 MB" 
   }
   ```

3. **Test Read/Download:**
   - Go to book page
   - Click "Read Online" - should open PDF in Google Drive viewer
   - Click "Download" - should start downloading PDF

---

## 🎨 Color Scheme Reference

If you want to adjust colors, they're in the CSS:

**index.html:**
- Green: `#228B22`
- Red: `#DC143C`
- Hover Green: `#1a6b1a`
- Hover Red: `#b01030`

**writers.html:**
- Background: Wooden brown gradient
- Buttons: Same green/red as welcome page

**book.html:**
- Primary: Green & Red
- Accent: Light backgrounds

---

## 🐛 Troubleshooting

### "Writers not loading on writers.html"
- Check if `js/data.js` is in the correct folder
- Open browser console (F12) and check for errors
- Verify file is loading: Check Network tab in DevTools

### "Book page shows 'Book not found'"
- Check URL parameters: `?writer=Name&book=Title`
- Make sure writer name matches exactly (case-sensitive)
- Make sure book title matches exactly

### "Buttons look wrong colors"
- Refresh page (Ctrl+R or Cmd+R)
- Clear browser cache (Ctrl+Shift+Delete)

### "Bookshelf not showing books"
- Check js/data.js is valid JSON
- Open console (F12) - look for red errors
- Try: `getWriters()` in console to debug

---

## 📱 Responsive Design Tests

### Desktop (1920px+)
✅ Full-width layout
✅ 4-column feature grid
✅ Large bookshelf

### Tablet (768px - 1920px)
✅ 2-column grid
✅ Adjusted spacing
✅ Readable on landscape

### Mobile (320px - 768px)
✅ Single-column layout
✅ Stacked buttons
✅ Touch-friendly buttons

---

## 🔄 Update Workflow

### When you want to add writers/books:

1. **Edit js/data.js:**
   ```bash
   # Open in editor
   code "c:\Users\ishra\OneDrive\Desktop\Tasin's Library\js\data.js"
   ```

2. **Add new writer or book**

3. **Save file** (Ctrl+S)

4. **Refresh browser** (F5)

5. **Changes appear automatically!**

---

## 💾 File Sizes for Reference

Our demo books are sized at:
- Small books: ~1.2 MB
- Medium books: ~2.5 MB
- Large books: ~3.1 MB

Update sizes in `js/data.js` to match your actual files.

---

## 🚀 Ready When You Are!

✅ Welcome page - Vibrant and beautiful  
✅ Writers page - Dynamic with real data  
✅ Book page - Professional and functional  
✅ Data system - Easy to manage  

### Next: Add your Google Drive file IDs and deploy!

---

## Questions About the System?

See the detailed guide: **IMPLEMENTATION_GUIDE.md**

Good luck! 📚✨
