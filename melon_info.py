"""Print out all the melons in our inventory."""

# PLAN
# create for loop to loop through keys in the 3 dictionaries in melons.py

# Ideal Output:
# CASABA
#     seedless: False
#     price: 2.5
#     flesh_color: None
#     weight: None
#     rind_color: None


from melons import melon_names, melon_seedlessness, melon_prices


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])

print(print_melon)
