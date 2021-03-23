from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book, Cart, BookInCart
from django.shortcuts import redirect
from django.template.loader import render_to_string
import json
# Create your views here.


def home(request):
    cart = Cart.get_cart(request.user, request.session.session_key)
    cart_template = render_to_string('bookstore/cart.html', {'cart': cart})
    quan = cart.items_count if cart else 0
    context = {
        'gridData': gridData,
        'cart_template': cart_template,
        'quantity': quan
    }
    return render(request, 'bookstore/home.html', context)


def about(request):
    cart = Cart.get_cart(request.user, request.session.session_key)
    cart_template = render_to_string('bookstore/cart.html', {'cart': cart})
    quan = cart.items_count if cart else 0
    context = {
        'cart_template': cart_template,
        'quantity': quan
    }
    return render(request, 'bookstore/about.html', context)


def contact(request):
    cart = Cart.get_cart(request.user, request.session.session_key)
    cart_template = render_to_string('bookstore/cart.html', {'cart': cart})
    quan = cart.items_count if cart else 0
    context = {
        'cart_template': cart_template,
        'quantity': quan
    }
    return render(request, 'bookstore/contact.html', context)


def products(request):
    if request.method == 'POST':
        current_book = Book.objects.get(pk=request.POST['add'])
        Cart.add_to_cart(current_book, request.user, request.session)
    books = Book.objects.all()
    cart = Cart.get_cart(request.user, request.session.session_key)
    cart_template = render_to_string('bookstore/cart.html', {'cart': cart})
    quan = cart.items_count if cart else 0
    context = {
        'books': books,
        'cart_template': cart_template,
        'quantity': quan
    }

    return render(request, 'bookstore/products.html', context)


def redirectHome(request):
    return redirect('book-home')


def cart(request):
    cart = Cart.get_cart(request.user, request.session.session_key)
    return render(request, 'bookstore/cart.html', {'cart': cart})


def updateCart(request):
    data = json.loads(request.body)
    print(data)
    book = Book.objects.get(pk=data['book_pk'])
    if data['action'] == 'increase':
        cart = Cart.add_to_cart(book, request.user, request.session)
    elif data['action'] == 'decrease':
        cart = Cart.get_cart(request.user, request.session.session_key)
        cart.remove_book(book)
    elif data['action'] == 'delete':
        print("deleting...[in views]")
        cart = Cart.get_cart(request.user, request.session.session_key)
        BookInCart.objects.get(book=book, cart=cart).delete()
        cart.refresh_from_db()

    return JsonResponse(cart.items_count, safe=False)


gridData = [{
    id: 1,
    'title': "Some random stuff",
    'content': '''<div><p> Lorem ipsum dolor sit, amet consectetur adipisicing elit. Minima aut, porro facilis eaque accusamus
    sequi temporibus repellat eveniet error saepe laboriosam velit odio nesciunt necessitatibus
    explicabo perferendis provident, molestiae voluptatibus!</p>
    <p> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fugit eos aperiam mollitia laboriosam in
    quidem? Ipsa tempore maxime, minima vitae eveniet molestiae. Expedita, voluptatum praesentium in
    quas sapiente esse voluptates?</p></div >''',
    'img': 'books1.jpg'


},
    {
    id: 2,
    'title': "Another random text thing",
    'content': '''<div><p> Lorem ipsum dolor sit, amet consectetur adipisicing elit. Minima aut, porro facilis eaque accusamus
    sequi temporibus repellat eveniet error saepe laboriosam velit odio nesciunt necessitatibus
    explicabo perferendis provident, molestiae voluptatibus!</p>
        <ul>
    <li> Lorem ipsum dolor sit amet consectetur, adipisicing elit. Atque a excepturi harum dicta
        repudiandae consequuntur?</li>
    <li> Rem quia in perspiciatis, ut soluta ullam ipsam explicabo ipsum voluptatibus odit perferendis
        alias esse?</li>
    <li> Minima aut, porro facilis eaque accusamus
        sequi temporibus repellat eveniet error saepe laboriosam </li>
        </ul></div>''',
    'img': 'books2.jpg'
},
    {
    id: 3,
    'title': "A final one",
    'content': '''<div><p> Lorem ipsum dolor sit, amet consectetur adipisicing elit. Minima aut, porro facilis eaque accusamus
    sequi temporibus repellat eveniet error saepe laboriosam velit odio nesciunt necessitatibus
    explicabo perferendis provident, molestiae voluptatibus!</p> </div>''',
    'img': 'books3.jpg'
},


]
