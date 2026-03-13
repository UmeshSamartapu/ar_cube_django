Your code already rotates the cube, but it only rotates **left/right (Y axis)**.
To **inspect all faces of the cube**, we should allow **full 360° rotation (X and Y axes)** with **mouse drag and mobile swipe**.

Below is the **improved version of your exact code**.

---

# ✅ Full 360° Drag / Swipe Rotation Cube (A-Frame + AR.js)

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

<script>
AFRAME.registerComponent('drag-rotate', {
init: function () {

let el = this.el;

let dragging = false;
let previousX = 0;
let previousY = 0;

window.addEventListener('mousedown', function(e){
dragging = true;
previousX = e.screenX;
previousY = e.screenY;
});

window.addEventListener('mouseup', function(){
dragging = false;
});

window.addEventListener('mousemove', function(e){

if(!dragging) return;

let rotation = el.getAttribute('rotation');

let deltaX = e.screenX - previousX;
let deltaY = e.screenY - previousY;

rotation.y += deltaX * 0.5;
rotation.x += deltaY * 0.5;

el.setAttribute('rotation', rotation);

previousX = e.screenX;
previousY = e.screenY;

});

window.addEventListener('touchstart', function(e){
dragging = true;
previousX = e.touches[0].screenX;
previousY = e.touches[0].screenY;
});

window.addEventListener('touchend', function(){
dragging = false;
});

window.addEventListener('touchmove', function(e){

if(!dragging) return;

let rotation = el.getAttribute('rotation');

let deltaX = e.touches[0].screenX - previousX;
let deltaY = e.touches[0].screenY - previousY;

rotation.y += deltaX * 0.5;
rotation.x += deltaY * 0.5;

el.setAttribute('rotation', rotation);

previousX = e.touches[0].screenX;
previousY = e.touches[0].screenY;

});

}
});
</script>

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
rotation="0 0 0"
color="red"
drag-rotate>
</a-box>

</a-marker>

<a-entity camera></a-entity>

</a-scene>

</body>
</html>
```

---

# 🎮 What This Version Does

### 🖱 Desktop

Drag mouse → rotate cube **left/right + up/down**

### 📱 Mobile

Swipe → rotate cube **in full 360°**

### 🧊 Result

You can now **inspect all 6 faces of the cube freely**.

---

# 🔥 Why this version is better

Your previous version only changed:

```
rotation.y
```

Now it changes:

```
rotation.x
rotation.y
```

So the cube rotates **in both directions**, allowing **complete 3D inspection**.

---

# 🚀 If you want, I can also show you a **much smoother professional version** that includes:

* **inertia rotation (like Sketchfab / 3D viewers)**
* **pinch to zoom**
* **two-finger rotate**
* **works perfectly with `.glb` Blender models**

This will make your **Django AR project look like a professional 3D product viewer**.
