from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import redirect
from .models import Product, Customer, Order, OrderItem, Payment, Review
from .forms import CustomerSignUpForm, CustomerLoginForm
from django.contrib.auth.decorators import login_required

def customer_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'customer_id' not in request.session:
            return redirect('/login')
        return view_func(request, *args, **kwargs)
    return wrapper

def Login(request):
    form = CustomerLoginForm()
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                customer = Customer.objects.get(email=email, password=password)
                request.session['customer_id'] = customer.id
                return redirect('/')
            except Customer.DoesNotExist:
                return HttpResponse('Invalid email or password')
    return render(request, 'myapp/login.html', {'form': form})
    
def SignUp(request):
    form = CustomerSignUpForm()
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    return render(request, 'myapp/signup.html', {'form': form})

@customer_login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'myapp/home.html', {'products': products})

def logout(request):
    request.session.flush()
    return redirect('/login')