from django.shortcuts import render, redirect
from django.contrib import messages  # (debug info success waring error)
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.template.loader import render_to_string
from bookstore.models import Cart


def register(request):
    print(request.session.session_key)
    if request.user.is_authenticated:
        return redirect('book-home')

    if request.method == 'POST' and 'reg-but' in request.POST:
        registerForm = UserRegisterForm(request.POST)
        print("trying to reg new user")
        if registerForm.is_valid():
            new_user = registerForm.save()
            login(request, new_user)
            # guest_cart = Cart.objects.filter
            # username = registerForm.cleaned_data.get('username')
            # messages.success(request, f"Account create for {username}")
            return redirect('book-home')
        loginForm = AuthenticationForm()
    elif request.method == 'POST' and 'log-but' in request.POST:
        print("trying to login")
        loginForm = AuthenticationForm(data=request.POST)
        if loginForm.is_valid():
            loginForm.clean()
            guest_cart = Cart.get_cart(ses_key=request.session.session_key)
            login(request, loginForm.user_cache)
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart.merge_carts(created, guest_cart)

            return redirect('book-home')
        registerForm = UserRegisterForm()

    else:
        registerForm = UserRegisterForm()
        loginForm = AuthenticationForm()

    cart = Cart.get_cart(request.user, request.session.session_key)
    cart_template = render_to_string('bookstore/cart.html', {'cart': cart})
    quan = cart.items_count if cart else 0
    context = {
        'cart_template': cart_template,
        'quantity': quan,
        'registerForm': registerForm,
        'loginForm': loginForm
    }

    return render(request, 'users/register.html', context)
