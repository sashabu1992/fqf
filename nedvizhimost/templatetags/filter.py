from django import template


register = template.Library()



@register.filter
def user_in(objects, username):
    if objects.filter(username=username):
        return True
    return False

