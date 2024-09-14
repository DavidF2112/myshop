from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *


from cart.forms import CartAddProductForm


def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
         category = get_object_or_404(Category, slug=category_slug)
         products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                       'category': category,
                       'categories':categories,
                       'products':products
                  })


def product_detail(request,id,slug):
     product = get_object_or_404(Product , id=id,slug=slug,available=True)
     cart_product_form = CartAddProductForm()
     return render(request,'shop/product/detail.html',{'product':product,
                                                       'cart_product_form':cart_product_form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/login/register.html'
    success_url = reverse_lazy('/login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return '/'


def logout_user(request):
    logout(request)
    return redirect('/login')
