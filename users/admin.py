# Django
from django.contrib import admin 

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
    )