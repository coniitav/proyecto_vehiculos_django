from django import template

register = template.Library()

@register.filter(name='separar_miles_precio')
def separar_miles_precio(value):
    result = ''
    x = int(value)
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ".%03d%s" % (r, result)
    return "%d%s" % (x, result)