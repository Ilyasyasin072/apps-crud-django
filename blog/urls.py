from django.urls import path
from . import views

# untuk path about pada web akan menampilkan seperti berikut 127.0.0.1:8000/blog/about/
# sehingga link akan bersatu dengan blog/aboout
urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
]