from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from home.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from .models import Order, OrderItem

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def checkout_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=cart.get_total_price())
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['price'])
        cart.clear()  # Очищаем корзину после оформления заказа
        return redirect('/')
    return render(request, 'cart/order.html', {'cart': cart})    