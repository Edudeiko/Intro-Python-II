'''
A Store has Categories.      # has-a relationship
Each Category has Products.  # has-a relationship
'''

class Store:
    def __init__(self, name, categories):    # Constructor
    # attributes
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f'{self.name}\n'
        for i, c in enumerate(self.categories):
            output += ' ' + str(i+1) + '. ' + c.name + '\n'

        # Add line below
        output += ' ' + str(i+2) + '. Exit'
        return output


class Category:
    def __init__(self, name): #, products)
        self.name = name

    def __str__(self):
        return 'No products available in ' + self.name


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}\t${self.price}'

my_store = Store('The Dugout', [Category('Running'), Category('Baseball'), Category('Basketball')])
