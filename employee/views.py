from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView


class EmployeeView(ListView):
    model = Employee
    template_name = 'employee/list.html'
    context_object_name = 'users'


from django.views.generic import View
from django.http import JsonResponse


class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Employee.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)
