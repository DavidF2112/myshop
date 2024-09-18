from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Количество пустых форм для добавления новых OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at', 'updated_at')  # Поля для отображения в списке
    search_fields = ('user__username',)  # Поиск по имени пользователя
    inlines = [OrderItemInline]  # Встраиваемые модели для отображения OrderItems

# Регистрация моделей
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
