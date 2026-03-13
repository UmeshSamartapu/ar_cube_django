{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AR 3D Viewer</title>

<script src="https://aframe.io/releases/1.4.0/aframe.min.js"></script>
<script src="https://cdn.jsdelivr.net/gh/AR-js-org/AR.js/aframe/build/aframe-ar.js"></script>

<style>
body{
margin:0;
overflow:hidden;
}
</style>

<script>

AFRAME.registerComponent('professional-controls', {

init: function () {

let el = this.el;

let dragging = false;
let previousX = 0;
let previousY = 0;

let velocityX = 0;
let velocityY = 0;

let scale = 1;

let lastDistance = null;

let rotation = el.getAttribute('rotation');


// DESKTOP CONTROLS

window.addEventListener('mousedown', (e)=>{
dragging = true;
previousX = e.screenX;
previousY = e.screenY;
});

window.addEventListener('mouseup', ()=>{
dragging = false;
});

window.addEventListener('mousemove', (e)=>{

if(!dragging) return;

let deltaX = e.screenX - previousX;
let deltaY = e.screenY - previousY;

rotation.y += deltaX * 0.5;
rotation.x += deltaY * 0.5;

velocityX = deltaX;
velocityY = deltaY;

el.setAttribute('rotation', rotation);

previousX = e.screenX;
previousY = e.screenY;

});


// INERTIA (Sketchfab-like)

this.el.sceneEl.addEventListener('renderstart', ()=>{

setInterval(()=>{

if(dragging) return;

velocityX *= 0.95;
velocityY *= 0.95;

rotation.y += velocityX * 0.05;
rotation.x += velocityY * 0.05;

el.setAttribute('rotation', rotation);

},16);

});


// TOUCH CONTROLS

window.addEventListener('touchstart',(e)=>{

if(e.touches.length == 1){

dragging = true;
previousX = e.touches[0].screenX;
previousY = e.touches[0].screenY;

}

if(e.touches.length == 2){

let dx = e.touches[0].screenX - e.touches[1].screenX;
let dy = e.touches[0].screenY - e.touches[1].screenY;

lastDistance = Math.sqrt(dx*dx + dy*dy);

}

});

window.addEventListener('touchend', ()=>{

dragging = false;
lastDistance = null;

});


window.addEventListener('touchmove',(e)=>{

// ONE FINGER ROTATE

if(e.touches.length == 1 && dragging){

let deltaX = e.touches[0].screenX - previousX;
let deltaY = e.touches[0].screenY - previousY;

rotation.y += deltaX * 0.5;
rotation.x += deltaY * 0.5;

velocityX = deltaX;
velocityY = deltaY;

el.setAttribute('rotation', rotation);

previousX = e.touches[0].screenX;
previousY = e.touches[0].screenY;

}


// PINCH ZOOM

if(e.touches.length == 2){

let dx = e.touches[0].screenX - e.touches[1].screenX;
let dy = e.touches[0].screenY - e.touches[1].screenY;

let distance = Math.sqrt(dx*dx + dy*dy);

if(lastDistance){

let diff = distance - lastDistance;

scale += diff * 0.002;

scale = Math.max(0.3, Math.min(3, scale));

el.setAttribute('scale', scale+" "+scale+" "+scale);

}

lastDistance = distance;

}

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

<!-- Works for cube -->
<a-box
position="0 0.5 0"
rotation="0 0 0"
color="red"
professional-controls>
</a-box>

<!-- Example GLB model -->
<!--
<a-entity
gltf-model="{% static 'models/model.glb' %}"
position="0 0 0"
scale="1 1 1"
professional-controls>
</a-entity>
-->

</a-marker>

<a-entity camera></a-entity>

</a-scene>

</body>
</html>