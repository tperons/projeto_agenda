from django.contrib import admin
from contact import models




@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'phone', 'category', 'show')
    ordering = ('-id',)
    list_filter = ('category',)
    search_fields = ('first_name',)
    list_per_page = 10
    list_display_links = ('first_name',)
    list_editable = ('show',)



    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
