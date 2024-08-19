import datetime
from django import template

# register in the template library
register = template.Library()

# register the tag
@register.simple_tag
# tag that provides today's date in a particular format
def todays_date():
    return datetime.datetime.now().strftime("%d %b, %Y")