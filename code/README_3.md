Your **Django AR project code is already correct**.
To make the **VR / AR page open on your phone or another device in the same Wi-Fi**, you only need to do **2 configuration steps**.

I will show the **exact steps clearly**.

---

# 1️⃣ Change `ALLOWED_HOSTS` in Django

Open this file:

```
cube_project/settings.py
```

Find this line:

```python
ALLOWED_HOSTS = []
```

Change it to:

```python
ALLOWED_HOSTS = ['*']
```

Your section should look like this:

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
```

### Why?

By default Django only allows:

```
http://127.0.0.1
http://localhost
```

Setting `['*']` allows **any device in the same network** to access your project.

---

# 2️⃣ Find Your Computer's Local IP Address

Open **Command Prompt** and run:

```
ipconfig
```

Look for:

```
IPv4 Address . . . . . . . . . . : 192.168.1.15
```

Example:

```
192.168.1.15
```

This is your **local network IP**.

---

# 3️⃣ Run Django Server for the Network

Normally people run:

```
python manage.py runserver
```

But that only works for **your computer**.

Instead run:

```
python manage.py runserver 0.0.0.0:8000
```

### Meaning

```
0.0.0.0 = allow connections from entire network
8000 = port number
```

---

# 4️⃣ Open the AR Page on Your Phone

Make sure:

* 📶 Phone and computer are on **same Wi-Fi**

Then open **browser on phone**:

```
http://192.168.1.15:8000/ar/
```

Replace with your IP.

Example:

```
http://192.168.0.103:8000/ar/
```

Your **AR cube page will open**.

---

# 5️⃣ Allow Camera Permission

When the page loads:

```
Allow Camera Access
```

Point camera at **Hiro marker**.

Your **red cube will appear in AR**.

---

# 6️⃣ Hiro Marker for Testing

Print or open this marker:

[https://raw.githubusercontent.com/AR-js-org/AR.js/master/three.js/examples/marker-training/examples/pattern-files/pattern-hiro.png](https://raw.githubusercontent.com/AR-js-org/AR.js/master/three.js/examples/marker-training/examples/pattern-files/pattern-hiro.png)

Show it to your camera.

---

# 7️⃣ Your Final URL Structure

```
cube_project/
│
├── cube_project/
│    ├── settings.py
│    ├── urls.py
│
├── ar_app/
│    ├── templates/
│    │     └── ar_cube.html
│    ├── static/
│    ├── views.py
│    ├── urls.py
│
└── manage.py
```

Run server:

```
python manage.py runserver 0.0.0.0:8000
```

Open on phone:

```
http://YOUR-IP:8000/ar/
```

---

✅ **Your current code is already correct for AR cube.**
You only needed to **allow network access + run server correctly**.

---
