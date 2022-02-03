from re import search
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . forms import CustomUserCreationForm, CustomUserChnageForm
from . models import CustomUser


# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChnageForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {
            "fields": (
                'email', 'password', 'image'
            ),
        }),
        ('Permissions', {'fields':('is_staff', 'is_active',)}),
    )
    add_fielsets = (
        (None, {
            'class':('wide',),
            'fields':('email', 'password1', 'password2','image', 'is_staff', 'is_active',)}
        ),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    





admin.site.register(CustomUser, CustomUserAdmin)