To view your **Django AR app on your Android phone camera using the same WiFi**, you must run Django using your **computer’s local IP address instead of `127.0.0.1`**.

Follow these steps.

---

# 1️⃣ Find Your Computer's Local IP Address

Open **Command Prompt** on your laptop and run:

```bash
ipconfig
```

Look for something like:

```
IPv4 Address . . . . . . . . . . : 192.168.1.8
```

Example IP:

```
192.168.1.8
```

---

# 2️⃣ Run Django Using the IP Address

Instead of running:

```bash
python manage.py runserver
```

Run:

```bash
python manage.py runserver 0.0.0.0:8000
```

or

```bash
python manage.py runserver 192.168.1.8:8000
```

Now Django will accept connections from other devices on the network.

---

# 3️⃣ Connect Android Phone to Same WiFi

Make sure:

* Laptop and phone are on **same WiFi**
* Laptop firewall allows **port 8000**

---

# 4️⃣ Open the App on Your Phone

Open **Chrome on your Android phone** and type:

```
http://192.168.1.8:8000/ar/
```

Replace with your **actual IP address**.

Example:

```
http://192.168.1.8:8000/ar/
```

---

# 5️⃣ Allow Camera Permission

When the page loads:

* Chrome will ask **Allow Camera**
* Click **Allow**

Now **AR.js will open the phone camera**.

Point the camera to a **Hiro marker** to see the cube.

Download marker if needed:

[https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png](https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png)

Print it or display it on another screen.

---

# 6️⃣ Important Fix for Mobile Camera

Replace this line in your HTML:

```html
arjs="trackingMethod: best; sourceType: webcam; debugUIEnabled: false"
```

with

```html
arjs="trackingMethod: best; sourceType: webcam; debugUIEnabled: false;"
```

Actually AR.js **automatically uses the phone camera**.

---

# 7️⃣ Final Phone URL

Your Android phone will open:

```
http://YOUR_PC_IP:8000/ar/
```

Example:

```
http://192.168.1.8:8000/ar/
```

---

# 8️⃣ Common Errors

### Camera not opening

Use **Chrome mobile**, not normal browser.

### Cannot connect

Check firewall or confirm IP again.

---

# 9️⃣ Optional (Better for AR)

Use **HTTPS** instead of HTTP for better camera support.

Tools:

```
ngrok
```

or

```
localtunnel
```

---

✅ If you want, I can also show you a **perfect Django AR project structure for phone + WebAR + GLB models** so your **heart model / Blender model works smoothly in AR on Android**.
