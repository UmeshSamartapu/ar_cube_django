# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'ar_app',
]



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "ar_app/static"
]


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# project urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ar/', include('ar_app.urls')),
]


# project views.py


# app urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.ar_cube, name='ar_cube'),
]

# app views.py
from django.shortcuts import render

def ar_cube(request):
    return render(request, "ar_cube.html")


# app>templates>ar_cube.html

{% load static %}
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">

<script src="https://aframe.io/releases/1.4.0/aframe.min.js"></script>
<script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar.js"></script>

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
renderer="logarithmicDepthBuffer: true"
arjs="trackingMethod: best; sourceType: webcam; debugUIEnabled: false">

<a-marker preset="hiro">

<a-box
position="0 0.5 0"
color="red"
depth="0.5"
height="0.5"
width="0.5">
</a-box>

</a-marker>

<a-entity camera></a-entity>

</a-scene>

</body>
</html>
