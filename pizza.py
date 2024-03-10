## IMPORTING AN ENTIRE MODULE

# we first need to create a module
# a module is a file endin in .py that contains the code you 
# want to import inot your program
# lets make one that contains the function make_pizza()


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + 
         "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)