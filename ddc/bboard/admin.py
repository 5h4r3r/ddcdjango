from .models import Rubric
from django.contrib import admin

# Register your models here.

from .models import Bb


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'prise', 'rubric', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Bb, BbAdmin)

admin.site.register(Rubric)
