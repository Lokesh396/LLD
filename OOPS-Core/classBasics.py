
class Cake():
    """
    A class is a template or blueprint which contains attributes(data) and behaviour (methods)
    for an object. A class is not a object itself it just the template.

    A object is an real world manifestation of an object, with all properties and behaviour.
    """
    def __init__(self, milk, dough, sugar, eggs, water,flavour):
        # attributes
        self.milk = milk 
        self.dough = dough
        self.sugar = sugar
        self.eggs = eggs
        self.water = water
        self.flavour = flavour
    
    # behaviour
    def prepare(self):
        print(f'Added all the ingredients in to a pan and mixed {self.flavour}')
    
    def bake(self):
        print(f'{self.flavour} cake is baking')


chocolate =  Cake('1tr', '1kg','1kg','6','1tr','chocolate-esence')
vanilla = Cake('1tr', '1kg','1kg','6','1tr','vanill-esence')

chocolate.prepare()
chocolate.bake()

vanilla.prepare()
vanilla.bake()

