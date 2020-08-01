"""Print out all the melons in our inventory."""

# PLAN
# adjust melons.py to be a "melons" dictionary of each melon (key: melon; values: price, etc.)
# import melons function from melons document
# create new function with parameter melons (document)
# create for loop to print key and values in "melons" dictionary

# Ideal Output:
# CASABA
#     seedless: False
#     price: 2.5
#     flesh_color: None
#     weight: None
#     rind_color: None

from melons import melons

def melon_info(melons):
    for melon_name, melon_properties in melons.items():
        print(melon_name)

        for melon_properties, value in melon_properties.items():
            print(f"{melon_properties} : {value}")

        print("-----------")
    
print(melon_info(melons))

# from melons import melon_names, melon_seedlessness, melon_prices


# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])

# print(print_melon)
