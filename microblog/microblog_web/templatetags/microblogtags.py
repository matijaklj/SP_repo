from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

regx = re.compile("\#[0-9\w]{1,100}\b")

def hashrepl(matchobj):
    return "<a href=\"/microblog/hashtag/" + str(matchobj.group(0)[1:]) + "\">" + str(matchobj.group(0)) + "</a>"

def afnarepl(matchobj):
    return "<a href=\"/microblog/profile/" + str(matchobj.group(0)[1:]) + "\">" + str(matchobj.group(0)) + "</a>"

@register.filter(name="editpost")
def hashtag(content):
    content = mark_safe(re.sub('\@[0-9\w_]{1,100}\\b', afnarepl, content))
    return mark_safe(re.sub('\#[0-9\w]{1,100}\\b', hashrepl, content))

hashtag.mark_safe=True
