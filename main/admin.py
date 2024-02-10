from django.contrib import admin
from .models import YourModel

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')
    search_fields = ('field1', 'field2')
    list_filter = ('field3',)

# Register your model with the custom admin class
admin.site.register(YourModel, YourModelAdmin)