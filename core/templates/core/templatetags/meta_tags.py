from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag(takes_context=True)
def meta_title(context, default="Anonphoto - Partage de posts anonyme"):
    return context.get('meta_title', default)

@register.simple_tag(takes_context=True)
def meta_description(context, default="Commente mon post de façon anonyme ."):
    return context.get('meta_description', default)

@register.simple_tag(takes_context=True)
def meta_image(context, default=None):
    request = context['request']
    if 'meta_image' in context:
        return request.build_absolute_uri(context['meta_image'])
    # fallback image
    return request.build_absolute_uri(static('core/preview.png'))
