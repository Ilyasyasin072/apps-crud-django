from django.urls import path
from employee import views

urlpatterns = [
    path('crud/',  views.EmployeeView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
]