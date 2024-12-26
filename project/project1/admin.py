from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Type1, Flower

admin.site.register(Type1)

class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_photo', 'type1', 'color', 'price', 'production_date')
    list_display_links = ('id', 'name')
    list_editable = ('type1',)
    list_filter = ('type1',)
    search_fields = ('name',)
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = False
    save_on_top = False

    def get_photo(self,flower):
        if flower.photo:
            return mark_safe(f'<img src="{flower.photo.url}" width="150px">')
        return "-"

    get_photo.short_description = "Photo"

admin.site.register(Flower, FlowerAdmin)