Since you are running **Django projects (AR / camera access) on your laptop**, you need **HTTPS** so that **mobile browsers allow camera access**.
**ngrok** solves this by exposing your **local server (localhost:8000)** to a **public HTTPS URL**.

Below is the **complete setup from scratch for Windows**.

---

# 1️⃣ Download ngrok

Go to:

👉 [https://ngrok.com/download](https://ngrok.com/download)

Download **Windows version**.

You will get a zip file like:

```
ngrok-v3-stable-windows-amd64.zip
```

Extract it.

You will get:

```
ngrok.exe
```

Place it inside a folder like:

```
C:\ngrok\
```

or inside your **Django project folder**.

---

# 2️⃣ Create ngrok Account

Open:

👉 [https://dashboard.ngrok.com/signup](https://dashboard.ngrok.com/signup)

Create a **free account**.

After login go to:

👉 [https://dashboard.ngrok.com/get-started/your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)

You will see something like:

```
ngrok config add-authtoken 2ab3xxxxxxxxxxxxxxxxxxxx
```

---

# 3️⃣ Connect ngrok to your Account

Open **PowerShell or CMD**.

Run:

```bash
ngrok config add-authtoken YOUR_TOKEN
```

Example:

```bash
ngrok config add-authtoken 2ab3xxxxxabcdef
```

Output should show:

```
Authtoken saved to configuration file
```

---

# 4️⃣ Start Your Django Server

Inside your Django project:

```bash
python manage.py runserver 8000
```

Server runs at:

```
http://127.0.0.1:8000
```

or

```
http://localhost:8000
```

---

# 5️⃣ Start ngrok Tunnel

Open **another terminal** and run:

```bash
ngrok http 8000
```

You will see output like:

```
Forwarding  https://a1b2c3d4.ngrok-free.app -> http://localhost:8000
Forwarding  http://a1b2c3d4.ngrok-free.app -> http://localhost:8000
```

Important part:

```
https://a1b2c3d4.ngrok-free.app
```

---

# 6️⃣ Open on Mobile

Open this URL on your phone:

```
https://a1b2c3d4.ngrok-free.app
```

Now:

✅ HTTPS enabled
✅ Camera works
✅ AR.js works
✅ WebRTC works

This fixes errors like:

```
navigator.mediaDevices not present
Access this site over HTTPS
```

---

# 7️⃣ Inspect Traffic (Very Useful)

Open:

```
http://127.0.0.1:4040
```

You will see:

```
Requests
Headers
Response
Latency
```

Useful for debugging APIs.

---

# 8️⃣ Typical Workflow for Your Django AR Project

Every time you run the project:

### Terminal 1

```bash
python manage.py runserver
```

### Terminal 2

```bash
ngrok http 8000
```

Open:

```
https://xxxxx.ngrok-free.app
```

---

# 9️⃣ Optional (Better command)

You can bind host like this:

```bash
ngrok http http://127.0.0.1:8000
```

---

# 🔟 Example Output

```
Session Status                online
Account                       free plan
Version                       3.x
Region                        Asia (ap)
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123.ngrok-free.app -> http://localhost:8000
```

---

# 🚀 For Your Current AR Django Project

Open:

```
https://xxxxx.ngrok-free.app/ar/
```

instead of:

```
http://192.168.x.x:8000/ar/
```

Then **camera + AR will work on mobile**.

---

✅ If you want, I can also show you **the correct Django + AR.js project structure that works perfectly with ngrok and mobile AR** (most tutorials miss some important settings).
