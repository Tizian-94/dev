# Chapter listing & detail page
from tabnanny import verbose

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from django.db import models
from django.shortcuts import render

from streams import blocks

class ChapterCarouselImages(Orderable):
    # put pages here
    page = ParentalKey("page.PageDetailPage", related_name="carousel_page_image")
    page_image = models.ForeignKey(
    "wagtailimages.Image",
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name="+",
    )

    panels = [
        ImageChooserPanel("page_image")
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cta"),
        ], heading="Banner Options"),
        
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=69, min_num=1, label="Image"),       
            ],
            heading="Carousel Images",
        ),
        StreamFieldPanel("content"),
    ]



class PageListingPage(RoutablePageMixin, Page):
    # Lists all individual pages
    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text='Overwrites the default title',)

    template = "base/blocks/page_listing_page.html"

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
    # adding custom stuff to our context
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = PageDetailPage.objects.live().public()
        return context

    @route(r'^latest/?$')

    def latest_chapter(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context["latest_chapters"] = PageDetailPage.objects.live().public()[:2]

        return render(request, "base/latest_chapter.html", context)


class PageDetailPage(Page):
    # Chapter detail page
    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text='Overwrites the default title',)
    chapter_image = models.ForeignKey("wagtailimages.Image", blank=False, null=True, related_name="+", on_delete=models.SET_NULL,)

    template = "base/blocks/page_detail_page.html"

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
            FieldPanel("custom_title"),
            ImageChooserPanel("chapter_image"),
        ], heading="Banner Options"),
        
        MultiFieldPanel([
            InlinePanel("carousel_page_image", max_num=69, min_num=1, label="Image"),       
            ],
            heading="Page Images",
        ),
        StreamFieldPanel("content"),
    ]

class Meta:

    verbose_name = "Chapter Page"
    verbose_name_plural = "Chapter Pages"