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

    <a-scene embedded arjs>

    <a-marker preset="hiro">

        <a-entity
            gltf-model="{% static 'models/colored_cube.glb' %}"
            scale="0.7 0.7 0.7"
            position="0 0 0"
            animation="property: rotation; to: 0 360 0; loop: true; dur: 8000; easing: linear">
        </a-entity>

    </a-marker>

    <a-entity camera></a-entity>

</a-scene>

</body>
</html>