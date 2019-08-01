from datetime import timezone
from django.conf import settings
from wagtail_factories import PageFactory
from factory import (
    Faker,
    LazyAttribute
)
from wagtail.core.models import Page as WagtailPage

from networkapi.wagtailpages.models import BlogPage
from networkapi.utility.faker.helpers import (
    get_homepage,
    reseed
)
from .index_page import IndexPageFactory

RANDOM_SEED = settings.RANDOM_SEED
TESTING = settings.TESTING

blog_body_streamfield_fields = ['paragraph', 'image', 'image_text', 'image_text_mini',
                                'video', 'linkbutton', 'spacer', 'quote']


class BlogPageFactory(PageFactory):

    class Meta:
        model = BlogPage
        exclude = (
            'title_text',
        )

    title = LazyAttribute(lambda o: o.title_text.rstrip('.'))
    author = Faker('name')
    body = Faker('streamfield', fields=blog_body_streamfield_fields)
    first_published_at = (Faker('date_time', tzinfo=timezone.utc) if RANDOM_SEED and not TESTING
                          else Faker('past_datetime', start_date='-30d', tzinfo=timezone.utc))
    live = True

    # Lazy Values
    title_text = Faker('sentence', nb_words=3, variable_nb_words=False)


def generate(seed):
    reseed(seed)
    home_page = get_homepage()

    try:
        blog_namespace = WagtailPage.objects.get(title='blog')
        print('blog namespace exists')
    except WagtailPage.DoesNotExist:
        print('Generating a blog namespace')
        blog_namespace = IndexPageFactory.create(
            parent=home_page,
            title='blog',
            header='blog',
            live=True
        )

    print('Generating blog posts under namespace')
    for i in range(7):
        title = Faker('sentence', nb_words=6, variable_nb_words=False)
        try:
            BlogPage.objects.get(title=title)
        except BlogPage.DoesNotExist:
            BlogPageFactory.create(parent=blog_namespace, title=title)
