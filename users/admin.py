# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#Django models
from django.contrib.auth.models import User

#models personals
from users.models import Profile

#one way to register:
#admin.site.register(Profile)

#another way to register:
@admin.register(Profile) 
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin """
    list_display = (
        'id',
        'user', 
        'phone_number', 
        'website', 
        'picture'
    )
    list_display_links = ('id','user')
    list_editable = ('phone_number', 'website', 'picture')
    readonly_fields=('created','modified','user')
    search_fields = (
        'user__email',
        'user__username', 
        'user__first_name', 
        'user__last_name', 
        'phone_number'
    )

    list_filter =(
        'created', 
        'modified', 
        'user__is_active', 
        'user__is_staff'
    )

    fieldsets = (
        ('Profile', {
            'fields': (
                #si queremos que los elementos esten juntos deben estar en una tupla ambos
                ('user', 'picture'),
            ),
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            ),
        }),
    )

class ProfileInline(admin.StackedInline):
    """ Profile in line admin for users """
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """add profile admin to base user admin """
    inlines = (ProfileInline,)
    list_display= (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)