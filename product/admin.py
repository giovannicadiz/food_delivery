from django.contrib import admin
from product.models import Menu, MainCourse, SideDish, Salad, Dessert, Drink


# Register your models here.
admin.site.site_header = "Food Delivery - Administration"


class MenuAdmin(admin.ModelAdmin):

    list_display = ['name', 'mainCourse', 'sideDish', 'salad', 'dessert', 'drink']
    ordering = ('name',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(MainCourse)
admin.site.register(SideDish)
admin.site.register(Salad)
admin.site.register(Dessert)
admin.site.register(Drink)