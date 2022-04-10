from turtle import title
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta:
        template = "base/blocks/title_and_text_block.html"
        icon = "doc-full"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=False, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=False, max_length=40)),
                ("text", blocks.TextBlock(required=False, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text= "if the button page above is selected, that will be used first")),
            ]
        )
    )

    class Meta:
        template = "base/blocks/card_block.html"
        icon = "placeholder"
        label = "Cards"

class RichtextBlock(blocks.RichTextBlock):

    class Meta:
        template = "base/blocks/richtext_block.html"
        icon =  "edit"
        label = "Full RichText"

class SimpleRichtextBlock(blocks.RichTextBlock):

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]
        

    class Meta:
        template = "base/blocks/richtext_block.html"
        icon =  "edit"
        label = "Simple RichText"

class CTABlock(blocks.StructBlock):
    # Simple cta section

    title = blocks.CharBlock(required=False, max_lenght=60)
    text = blocks.RichTextBlock(required=False, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length="40")

    class Meta: 
        template = "base/blocks/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"