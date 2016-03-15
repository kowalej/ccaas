from django import template
from mezzanine.blog.models import BlogPost
from mezzanine.pages.models import Page
from mezzanine.galleries.models import Gallery
from mainsite.models import Slide, ExtraFact
import re
import random
from mezzanine.utils.views import paginate
from mezzanine.conf import settings
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

register = template.Library()

def do_upper(parser, token):
    nodelist = parser.parse(('endupper',))
    parser.delete_first_token()
    return UpperNode(nodelist)

class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()

def recent_blog_posts_by_cat(parser, token):
     # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, cat, limit, void, var_name = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents[0])
    return RecentBlogPostsByCat(cat, limit, var_name)

class RecentBlogPostsByCat(template.Node):
    def __init__(self, cat, limit, var_name):
        self.cat = template.Variable(cat)
        self.limit = limit
        self.var_name = var_name

    def render(self, context):
        actual_cat = self.cat.resolve(context)
        context[self.var_name] = list(BlogPost.objects.published().filter(categories__id=actual_cat)[:self.limit])
        return ''

def get_slides(parser, token):
     # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, limit, var_name = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents[0])
    return GetSlides(limit, var_name)

class GetSlides(template.Node):
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = list(Slide.objects.published()[:self.limit])
        return ''

def get_extra_facts(parser, token):
     # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, limit, var_name = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents[0])
    return GetExtraFacts(limit, var_name)

class GetExtraFacts(template.Node):
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = list(ExtraFact.objects.all()[:self.limit])
        return ''

def get_home_page(parser, token):
    try:
        tag_name, var_name = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents[0])
    return GetHomePage(var_name)

class GetHomePage(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = Page.objects.get(title="Home")
        return ''

def get_gallery(parser, token):
    try:
        tag_name, var_name = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents[0])
    return GetGallery(var_name)

class GetGallery(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        gallery_id = context['gallery_id']
        context[self.var_name] = Gallery.objects.get(page_ptr_id = gallery_id)
        return ''   

def random_num(parser, token):
    try:
        tag_name, lower_bound, upper_bound, num_randoms, var_name = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents[0])
    return RandomNum(lower_bound, upper_bound, num_randoms, var_name)

class RandomNum(template.Node):
    def __init__(self, lower_bound, upper_bound, num_randoms, var_name):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.num_randoms = num_randoms
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = [str(random.randint(int(self.lower_bound), int(self.upper_bound))) for r in xrange(int(self.num_randoms))]
        return ''   

def is_link(value):
    validate = URLValidator()
    try:
        validate(value)
    except ValidationError, e:
        return ''
    return value

register.filter(is_link)
register.tag('upper', do_upper)
register.tag(get_slides)
register.tag(get_extra_facts)
register.tag(get_home_page)
register.tag(get_gallery)
register.tag(random_num)
register.tag(recent_blog_posts_by_cat)


