from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models
from .forms import UserChangeForm, UserCreationForm
# Register your models here.


class DiamondAdmin(admin.ModelAdmin):
    pass


# admin.site.register(models.User, DiamondAdmin)
admin.site.register(models.Gameid, DiamondAdmin)
admin.site.register(models.Depositstatement, DiamondAdmin)
admin.site.register(models.Withdrawstatement, DiamondAdmin)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('phone_number', 'is_active', 'is_admin', 'is_superuser')
    list_filter = ('is_active', 'is_admin')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin',
         'is_superuser', 'last_login', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'fields': ('phone_number', 'password', 'balance')}),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['phone_number'].disabled = True
        return form


admin.site.register(models.User, UserAdmin)
