from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from copy import deepcopy


class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=30)
    description = models.TextField(default="no description available")
    quote = models.TextField(default="no quote available")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    session = session = models.CharField(max_length=64, null=True)
    items_count = models.IntegerField(default=0)
    price_total = models.DecimalField(
        max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s Cart" if hasattr(self.user, 'username') else "Guest Cart"

    # this is static cause some times we need to create a cart, could break it into 2 methods...
    @staticmethod
    def add_to_cart(book, user=None, session=None):
        # loggedin user
        if user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=user)
        # guest user
        else:
            if not session.session_key:
                session.create()
            cart, created = Cart.objects.get_or_create(
                session=session.session_key)
        # the rest of the logic is the same
        bookincart, created = BookInCart.objects.get_or_create(
            book=book, cart=cart)
        bookincart.quantity += 1
        bookincart.save()
        # update price and item count
        cart.items_count += 1
        cart.price_total += book.price
        cart.save()
        return cart

    @staticmethod
    def get_cart(user=None, ses_key=None):
        cart = []
        if user and user.is_authenticated:
            cart = Cart.objects.filter(user=user)
        elif ses_key != None:
            cart = Cart.objects.filter(session=ses_key)
        return cart[0] if cart else None

    def remove_book(self, book):
        bookincart = BookInCart.objects.get(book=book, cart=self)
        if bookincart.quantity == 1:
            return self
        bookincart.quantity -= 1
        bookincart.save()
        # update price and item count
        self.items_count -= 1
        self.price_total -= book.price
        self.save()
        return self

    def merge_carts(self, created, guest_cart):
        print("mergin...")
        if guest_cart is not None:
            for bookincart in guest_cart.bookincart_set.all():
                print(
                    f'merging {bookincart.book} x {bookincart.quantity} in my cart')
                newBookinCart, created = BookInCart.objects.get_or_create(
                    cart=self, book=bookincart.book)
                newBookinCart.quantity += bookincart.quantity
                self.items_count += bookincart.quantity
                self.price_total += bookincart.quantity * bookincart.book.price
                newBookinCart.save()
            self.save()
            guest_cart.delete()

    # def delete_book(self, book):
    #     bookincart = BookInCart.objects.get(book=book, cart=self)
    #     bookincart.delete()
    #     if bookincart.quantity == 1:
    #         return self
    #     bookincart.quantity -= 1
    #     bookincart.save()
    #     # update price and item count
    #     self.items_count -= 1
    #     self.price_total -= book.price
    #     self.save()
    #     return self
    #     pass

    def update_count_and_price(self):
        self.price_total = 0
        self.items_count = 0
        for book in self.bookincart_set.all():
            self.price_total += book.book.price*book.quantity
            self.items_count += book.quantity
        self.save()
        return


class BookInCart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def delete(self):
        print("deleting...")
        self.cart.price_total -= self.quantity * self.book.price
        self.cart.items_count -= self.quantity
        self.cart.save()
        super(BookInCart, self).delete()
        return

    # def __str__(self):
    #     return self.title

    # change this to one-to-one each user has one basket and each basket belongs to one user
    # books = models.ManyToManyField(BookOnCart)

    # def __str__(self):
    #     return self.title
