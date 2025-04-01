from django.contrib import admin
from .models import Post, PostAttachments
# Register your models here.
@admin.register(Post)
class CustomePostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {'fields' : ('title', 'content',)}),
        ('Дополнительная информация', {'fields': ('time_stamp', 'edited',)})
    )
    add_fieldsets = (
        ('Основная информация', {'fields' : ('title', 'content',)}),
    )
    list_display = ('title', 'time_stamp', 'edited')
    search_fields = ('title', 'content')
    ordering = ('time_stamp',)
    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets

admin.site.register(PostAttachments)