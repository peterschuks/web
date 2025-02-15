from django.contrib import admin
from .models import account,Profile
from django.contrib.auth.admin import UserAdmin

class accountAdmin(UserAdmin):
    list_display = ('email','first_name', 'last_name', 'username', 'last_login',
     'date_joined','is_active',)
    
    # i want to add links to the firstname and lastname

    list_display_links = ('email','first_name','last_name',)
    readonly_fields = ('last_login','date_joined','username',)
    ordering = ('-date_joined',)

    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()

admin.site.register(account, accountAdmin)
admin.site.register( Profile)

# Register your models here.
