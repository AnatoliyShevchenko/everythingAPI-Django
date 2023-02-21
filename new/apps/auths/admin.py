from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from typing import Optional

from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """Model admin."""

    model = User
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'date_joined',
        'is_active',
        'is_staff',
        'is_superuser'
    )
    readonly_fields = (
        
    )

    def get_readonly_fields(
        self, 
        request: WSGIRequest, 
        obj: Optional[User] = ...):
        if not obj:
            return self.readonly_fields
        return self.readonly_fields + ('date_joined',)

admin.site.register(User, UserAdmin)