from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.site_header = "Diamond Exchange Admin"
admin.site.site_title = "Diamond Exchange Admin"

from . import models
from .forms import UserChangeForm, UserCreationForm
# Register your models here.

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

class GameidAdmin(admin.ModelAdmin):
  list_display = ('username', 'user')
  search_fields = ('user',)
# admin.site.register(models.User, DiamondAdmin)
admin.site.register(models.Gameid, GameidAdmin)

class DepositsAdmin(admin.ModelAdmin):
  list_display = ('user', 'utrno','amount','status',)
  list_filter = ('status',)
  search_fields = ('user',)
admin.site.register(models.Depositstatement, DepositsAdmin)

class WithdrawalsAdmin(admin.ModelAdmin):
    list_display = ('user','upiid','amount','status',)
    list_filter = ('status',)
    search_fields = ('user',)
admin.site.register(models.Withdrawstatement, WithdrawalsAdmin)

class DiamondAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Verifyotp, DiamondAdmin)