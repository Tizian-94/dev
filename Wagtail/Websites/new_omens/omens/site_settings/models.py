from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    # Social media settings

    patreon = models.URLField(blank=True, null=True, help_text="Patreon URL")
    twitter =  models.URLField(blank=True, null=True, help_text="Twitter URL")
    deviantart = models.URLField(blank=True, null=True, help_text="Deviantart URL")
    youtube = models.URLField(blank=True, null=True, help_text="Youtube Channel URL")
    tumblr = models.URLField(blank=True, null=True, help_text="tumblr URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("patreon"),
            FieldPanel("twitter"),
            FieldPanel("deviantart"),
            FieldPanel("youtube"),
            FieldPanel("tumblr"),
        ], heading = "Social Media Settings")
    ]