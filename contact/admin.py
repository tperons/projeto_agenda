from django.contrib import admin
from contact import models
from django.contrib.auth.models import User




# Personaliza a exibição do usuário no Django Admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'date_joined')  # Mostra se está ativo
    list_filter = ('is_active', 'is_staff')  # Adiciona filtros no admin
    search_fields = ('username', 'email')  # Permite buscar por nome e e-mail
    actions = ['approve_users']  # Adiciona a opção de aprovação
    list_editable = ('is_active',)

    @admin.action(description='Aprovar usuários selecionados')
    def approve_users(self, request, queryset):
        queryset.update(is_active=True)  # Ativa os usuários selecionados

# Remove o registro padrão do modelo User no Django Admin
admin.site.unregister(User)
# Registra o modelo User com as novas configurações
admin.site.register(User, UserAdmin)




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
