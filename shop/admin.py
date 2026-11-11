
from django.contrib import admin
from .models import Profile, Product, Cart, CartItem, Payment, ProductHistory, Comment, Rate


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'is_paid')
    list_filter = ('is_paid',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('cart', 'amount', 'payment_method', 'status')
    list_filter = ('status',)


@admin.register(ProductHistory)
class ProductHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'action', 'date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')