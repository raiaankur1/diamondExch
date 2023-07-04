from django.contrib import admin
from . import models
# Register your models here.


class DiamondAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.User, DiamondAdmin)
admin.site.register(models.Gameid, DiamondAdmin)
