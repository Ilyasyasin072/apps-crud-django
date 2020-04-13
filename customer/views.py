from django.shortcuts import render, redirect
from .forms import CreateCustomerForm
from .models import Customers
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def Home(request):
    if request.method == 'POST':
        customers = CreateCustomerForm(request.POST)
        if customers.is_valid():
            customers.save()
            messages.success(request, f'Customers have been created!')
            return redirect('customer_list')
    else:
        customers = CreateCustomerForm()

    context = {
        'customers': customers
    }
    return render(request, 'customer/home_customer.html', context)


@login_required
def List(request):
    customers = CreateCustomerForm()
    context = {
        'customers': Customers.objects.all(),
        'u_forms': customers
    }
    return render(request, 'customer/list_customer.html', context)


def DashboardCustomer(request):
    return render(request, 'customer/dashboard_customer.html')


