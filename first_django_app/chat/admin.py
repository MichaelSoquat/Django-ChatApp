from django.contrib import admin
from .models import Chat, Message


# show/search fields in admin panel
class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','text', 'created_at', 'time_created_at','author', 'receiver')
    list_display = ('text', 'created_at', 'time_created_at', 'author', 'receiver')
    search_fields = ('text',)
    pass


# Register your models here.
admin.site.register(Message,MessageAdmin)
admin.site.register(Chat)
