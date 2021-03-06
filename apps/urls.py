"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from customer import views as customer_views
from customer import views as customer_list_views
from employee import views as views_employee
from blog import views as views_blog
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path(r'profile/', user_views.profile, name="profile"),
    path(r'customer/', customer_views.Home, name="customer"),
    path(r'customer_list/', customer_list_views.List, name="customer_list"),
    path('dashboard/customer/', customer_list_views.DashboardCustomer, name="dashboard_customer"),
    path('crud/', views_employee.EmployeeView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/', views_employee.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path(r'dashboard/home', views_blog.Dashboard, name="dashboard_home")

]

handler404 = views_blog.PageNotFound

# configuration upload images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

