import re
from django import template

register = template.Library()

@register.filter(name='limit_words')
def limit_words(value, word_count):
    """Limit the number of words in a string to the specified count."""
    words = value.split()
    if len(words) > word_count:
        return ' '.join(words[:word_count]) + '...'  # Add ellipsis if truncated
    return value
