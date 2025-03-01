# Convert Static Paths to Django `{% static %}`

🚀 A simple yet powerful script that automatically converts static asset paths in your HTML templates to Django's `{% static %}` tag format.

## ✨ Features
- 🔄 Automatically detects and replaces static asset paths (`href`, `src`, `url()`)
- 📂 Works on all `.html` files inside the `templates/` directory
- 🏆 Supports CSS, JS, images, and background images in inline styles
- ⚡ Helps in integrating static files seamlessly with Django projects

## 🛠️ How to Use

1. Make sure you have a Django project set up with `STATIC_URL` properly configured.
2. Place your HTML files inside the `templates/` directory.
3. Run the script from the root of your Django project:
   
   ```bash
   python convert_static.py
