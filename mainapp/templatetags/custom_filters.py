from django import template

register = template.Library()

@register.filter(name='add_commas')
def add_commas(value):
    # Convert value to string
    value_str = str(value)
    
    # Split the string into integer and decimal parts
    if '.' in value_str:
        integer_part, decimal_part = value_str.split('.')
    else:
        integer_part, decimal_part = value_str, ''
    
    # Add commas to the integer part
    integer_part_with_commas = ''
    count = 0
    for digit in reversed(integer_part):
        if count == 2:
            integer_part_with_commas = ',' + integer_part_with_commas
            count = 0
        integer_part_with_commas = digit + integer_part_with_commas
        count += 1
    
    # Combine integer and decimal parts
    if decimal_part:
        return integer_part_with_commas + '.' + decimal_part
    else:
        return integer_part_with_commas
