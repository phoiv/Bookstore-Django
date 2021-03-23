from django.contrib import admin
from .models import Book, Cart, BookInCart
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CartInline(admin.StackedInline):
    model = Cart


class UserAdminCustom(UserAdmin):
    inlines = [CartInline]


class BookInCartInline(admin.StackedInline):
    model = BookInCart


class CartAdmin(admin.ModelAdmin):
    inlines = [BookInCartInline]


admin.site.register(Book)
admin.site.unregister(User)
admin.site.register(Cart, CartAdmin)
admin.site.register(User, UserAdminCustom)


# Register your models here.
