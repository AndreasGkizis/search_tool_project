from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def is_active(request, url):
    # if on the current url the return "active" otherwise return ""
    if request.path == reverse(url):
        return "active"
    else:
        return ""

#
# @register.pub_page
# def url_pub_page(request, slug):
#
#
#     return reverse('show_publication', kwargs={'slug': self.slug})
