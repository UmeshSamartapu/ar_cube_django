You are seeing these errors because **mobile browsers block camera and sensor access on HTTP**.

Errors you see:

* **“Access this site over HTTPS to enter VR mode and grant access to the device sensors.”**
* **“navigator.mediaDevices not present”**

Both mean **your site must run over HTTPS** when accessed from a phone.

Your Django server currently runs like:

```
http://192.168.x.x:8000
```

This is **not secure**, so the phone blocks the camera.

---

# ✅ Best Solution (Use HTTPS with ngrok)

This is the **standard way to test AR projects locally**.

## 1️⃣ Install ngrok

Download:
[https://ngrok.com/download](https://ngrok.com/download)

Extract it.

---

## 2️⃣ Run Django

In your project folder:

```bash
python manage.py runserver 0.0.0.0:8000
```

---

## 3️⃣ Start ngrok

Open another terminal:

```bash
ngrok http 8000
```

You will see something like:

```
Forwarding https://abcd1234.ngrok-free.app -> http://localhost:8000
```

---

## 4️⃣ Open on your Android phone

Open Chrome and go to:

```
https://abcd1234.ngrok-free.app/ar/
```

Now:

* HTTPS is enabled
* Camera works
* Sensors work
* AR.js works correctly

---

# ✅ Important HTML Fix

Use this **final working HTML**.

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AR Cube</title>

<script src="https://aframe.io/releases/1.4.0/aframe.min.js"></script>
<script src="https://cdn.jsdelivr.net/gh/AR-js-org/AR.js/aframe/build/aframe-ar.js"></script>

<style>
body{
margin:0;
overflow:hidden;
}
</style>

</head>

<body>

<a-scene
embedded
vr-mode-ui="enabled: false"
renderer="logarithmicDepthBuffer: true;"
arjs="trackingMethod: best; sourceType: webcam; debugUIEnabled: false;">

<a-marker preset="hiro">

<a-box
position="0 0.5 0"
rotation="0 45 0"
color="red"
animation="property: rotation; to: 0 360 0; loop: true; dur: 4000">
</a-box>

</a-marker>

<a-entity camera></a-entity>

</a-scene>

</body>
</html>
```

---

# ⚠️ Also Make Sure

✔ Use **Chrome browser on Android**
✔ Allow **camera permission**
✔ Use **HTTPS link from ngrok**

---

# 🚀 Recommended for Your Project

Since your project is **AR Heart Visualization**, the **best setup** is:

```
Django
A-Frame
AR.js
GLB Heart Model
ngrok HTTPS
```

---

If you want, I can also show you **a much better AR setup for Django that supports:**

* **360° rotating heart**
* **Zoom with fingers**
* **Tap to show heart parts**
* **Much smoother AR tracking**

which will make your **project look like a professional AR medical app**.
