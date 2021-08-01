
from django import template

register = template.Library()

@register.filter
def add_space(word):
    """this will add a new space like NewConfirmed to New Confirmed"""
    if word.startswith("N"):
        word = word[:3] + " " + word[3:]
        return word
    else:
        word = word[:5] + " " + word[5:]
        return word

@register.filter
def increment(color_list,index_value):
    """this will return the list with specified index"""
    return color_list[index_value]

@register.filter
def format_date(date):
    """this is will format data like 2021-02-27T00:00:00Z to 2021-02-27"""
    get_index = date.index('T')
    new_date  =  date[:get_index]
    return new_date
