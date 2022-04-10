from importlib.resources import path

from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey
from pyexpat import features
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from base.blocks import CTABLOCK
from streams import blocks

from page.models import PageListingPage, PageDetailPage

class HomePageCarouselImages(Orderable):
    # between 1 and 5 images for the homepage carousel

    page = ParentalKey("base.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [ImageChooserPanel("carousel_image")]

class HomePage(RoutablePageMixin, Page):
    # class HomePage(Page):

    # template = "base\templates\base\home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(
        features=[
            "bold",
            "italic",
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "ol",
            "ul",
            "hr",
            "link",
            "document-link",
            "image",
            "embed",
        ]
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    # banner_cta = models.URLField je za bilo koj html
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content = StreamField(
        [
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cta"),
        ], heading="Banner Options"),
        
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=30, min_num=1, label="Image"),       
            ],
            heading="Carousel Images",
        ),
        StreamFieldPanel("content"),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['latest_context'] = PageListingPage.objects.live()
        return context

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


    @route(r'^subscribe/$')

    def the_subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context["a_special_test"] = ""
        return render(request, "base/subscribe.html", context)