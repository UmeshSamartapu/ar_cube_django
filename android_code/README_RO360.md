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

window.addEventListener('mousedown', function(e){
dragging = true;
previousX = e.screenX;
});

window.addEventListener('mouseup', function(){
dragging = false;
});

window.addEventListener('mousemove', function(e){
if(!dragging) return;

let rotation = el.getAttribute('rotation');
let delta = e.screenX - previousX;

rotation.y += delta * 0.5;

el.setAttribute('rotation', rotation);

previousX = e.screenX;
});

window.addEventListener('touchstart', function(e){
dragging = true;
previousX = e.touches[0].screenX;
});

window.addEventListener('touchend', function(){
dragging = false;
});

window.addEventListener('touchmove', function(e){
if(!dragging) return;

let rotation = el.getAttribute('rotation');
let delta = e.touches[0].screenX - previousX;

rotation.y += delta * 0.5;

el.setAttribute('rotation', rotation);

previousX = e.touches[0].screenX;
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
drag-rotate> </a-box>

</a-marker>

<a-entity camera></a-entity>

</a-scene>

</body>
</html>
