Here is the **complete step-by-step setup** to run your **Django AR project with HTTPS locally (without ngrok)** using **`django-sslserver`**.

This will allow **mobile camera access** for your AR project.

---

# 1️⃣ Activate Your Virtual Environment

Open terminal in your Django project folder.

Example:

```bash
cd E:\3D_Django\django-ar-project\ar_project
```

Activate environment:

```bash
conda activate env310
```

(or)

```bash
env\Scripts\activate
```

---

# 2️⃣ Install django-sslserver

Run:

```bash
pip install django-sslserver
```

Verify installation:

```bash
pip list
```

You should see:

```
django-sslserver
```

---

# 3️⃣ Edit `settings.py`

Open:

```
ar_project/settings.py
```

Find **INSTALLED_APPS** and add **sslserver**.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sslserver',   # add this line
    'ar_app',
]
```

Save the file.

---

# 4️⃣ Allow Your Local Network

Still inside **settings.py**, update:

```python
ALLOWED_HOSTS = ['*']
```

Example:

```python
ALLOWED_HOSTS = ['*']
```

This allows access from **mobile devices on the same network**.

---

# 5️⃣ Run HTTPS Django Server

Run:

```bash
python manage.py runsslserver 0.0.0.0:8000
```

You will see something like:

```
Starting development server at

https://0.0.0.0:8000
```

---

# 6️⃣ Find Your Computer IP Address

Open another terminal and run:

```bash
ipconfig
```

Look for:

```
IPv4 Address . . . . . . . . : 192.168.1.7
```

Your IP might look like:

```
192.168.1.7
```

---

# 7️⃣ Open the AR Page on Your Phone

Connect phone to **same WiFi network**.

Open browser and type:

```
https://192.168.1.7:8000/ar/
```

Replace with your IP.

---

# 8️⃣ Accept Security Warning

Since this is **local SSL**, browser will show warning.

On Chrome:

```
Advanced
→ Proceed to 192.168.1.7
```

Then your page loads.

---

# 9️⃣ Result

Now your **Django AR project will work on mobile**:

✅ Camera access
✅ AR marker detection
✅ `.glb` model rendering
✅ 360° model rotation

---

# Example Final Project Flow

```
Laptop
│
├── Django HTTPS Server
│      https://192.168.1.7:8000
│
└── Phone Browser
       ↓
https://192.168.1.7:8000/ar/
       ↓
Camera opens
       ↓
AR model appears
```

---

# ⚠️ Important AR.js Tip

Use this scene configuration in your template:

```html
<a-scene embedded arjs>

    <a-marker preset="hiro">
        <a-entity
            gltf-model="{% static 'models/colored_cube.glb' %}"
            scale="0.6 0.6 0.6"
            animation="property: rotation; to: 0 360 0; loop: true; dur: 8000">
        </a-entity>
    </a-marker>

    <a-entity camera></a-entity>

</a-scene>
```

