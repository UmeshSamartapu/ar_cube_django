Here is the **complete setup from scratch** to run **Augmented Reality with `colored_cube.glb` in Django**.

---

# 1️⃣ Install Python and Create Project Folder

Create a folder for the project.

```
django-ar-project
```

Open terminal inside it.

---

# 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

Activate it.

Windows:

```bash
env\Scripts\activate
```

Linux / Mac:

```bash
source env/bin/activate
```

---

# 3️⃣ Install Django

```bash
pip install django
```

Check installation:

```bash
django-admin --version
```

---

# 4️⃣ Create Django Project

```bash
django-admin startproject ar_project
```

Move into project folder.

```bash
cd ar_project
```

Project structure now:

```
ar_project
│
├── ar_project
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── manage.py
```

---

# 5️⃣ Create Django App

```bash
python manage.py startapp ar_app
```

Now structure becomes:

```
ar_project
│
├── ar_app
│   ├── views.py
│   ├── models.py
│   └── apps.py
│
├── ar_project
│
└── manage.py
```

---

# 6️⃣ Register App in Django

Open **settings.py**

Add:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'ar_app'
]
```

---

# 7️⃣ Create Templates Folder

Inside **ar_app** create:

```
ar_app
│
├── templates
│     └── ar_cube.html
```

---

# 8️⃣ Create Static Folder

```
ar_app
│
├── static
│   └── models
│        colored_cube.glb
```

Place your **Blender exported cube model** here.

Final structure:

```
ar_project
│
├── ar_app
│   │
│   ├── static
│   │   └── models
│   │        colored_cube.glb
│   │
│   ├── templates
│   │        ar_cube.html
│   │
│   ├── views.py
│   └── apps.py
│
└── manage.py
```

---

# 9️⃣ Create AR Template

`templates/ar_cube.html`

```html
{% load static %}

<html>
<head>

<script src="https://aframe.io/releases/1.4.0/aframe.min.js"></script>
<script src="https://cdn.jsdelivr.net/gh/AR-js-org/AR.js/aframe/build/aframe-ar.js"></script>

</head>

<body style="margin:0; overflow:hidden;">

<a-scene embedded arjs>

    <a-marker preset="hiro">

        <a-entity
            gltf-model="{% static 'models/colored_cube.glb' %}"
            scale="1 1 1">
        </a-entity>

    </a-marker>

    <a-entity camera></a-entity>

</a-scene>

</body>
</html>
```

---

# 🔟 Create View

`views.py`

```python
from django.shortcuts import render

def ar_cube(request):
    return render(request, "ar_cube.html")
```

---

# 1️⃣1️⃣ Create App URLs

Create file:

```
ar_app/urls.py
```

Add:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ar_cube, name='ar_cube'),
]
```

---

# 1️⃣2️⃣ Connect URLs to Main Project

Open:

```
ar_project/urls.py
```

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ar/', include('ar_app.urls')),
]
```

---

# 1️⃣3️⃣ Run Server

```bash
python manage.py migrate
python manage.py runserver
```

---

# 1️⃣4️⃣ Open Browser

```
http://127.0.0.1:8000/ar/
```

Allow **camera permission**.

---

# 1️⃣5️⃣ Show Marker to Camera

Print this marker and show to camera.

![Image](https://upload.wikimedia.org/wikipedia/commons/4/48/Hiro_marker_ARjs.png)

![Image](https://upload.wikimedia.org/wikipedia/commons/0/08/Pattern-hiro.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A792/0%2A1rr3GeX2F4QXNLfd)

![Image](https://user-images.githubusercontent.com/6317076/27867192-e55306b8-6190-11e7-9bd1-7a9dbf4fa76a.png)

Download marker:

```
https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png
```

When the camera sees the marker → **colored cube appears in AR**.

---

# ⚡ How It Works

```
Blender
   ↓
Export colored_cube.glb
   ↓
Django static folder
   ↓
HTML template loads model
   ↓
AR.js accesses camera
   ↓
Marker detected
   ↓
3D cube appears
```

---

✅ Since you are working on **ECG + 3D Heart Visualization project**, this cube demo is the **first step**.
Later you can replace:

```
colored_cube.glb
```

with

```
heart_model.glb
```

and highlight heart regions based on CNN prediction.

---

If you want, I can also show **a much better version using marker-less AR (place heart on table without marker)** which looks **very impressive for final year projects.**
