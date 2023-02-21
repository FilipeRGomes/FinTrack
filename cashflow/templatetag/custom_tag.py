
from django import template

register = template.Library()


@register.filter
def get_attr(self, attr):
    if attr is not None:
        return self.get_attr(self, attr)
    else:
        return self.__str__()
