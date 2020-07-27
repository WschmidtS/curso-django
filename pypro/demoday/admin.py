from django.contrib.admin import ModelAdmin, register

from pypro.demoday.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'vimeo_id')
