from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def execute(self, text):
        pass

    @abstractmethod
    def get_name(self):
        pass

class SpellCheckPlugin(Plugin):
    def execute(self, text):
        text = text.replace('teh', 'the')
        text = text.replace('adn', 'and')
        return text  # TODO: replace "teh" with "the", "adn" with "and"

    def get_name(self):
        return "Spell Check"

class WordCountPlugin(Plugin):
    def execute(self, text):
        temp = text.split()
        text += f'\n[Word Count: {len(temp)}]'
        return text  # TODO: append "\n[Word count: X]" to the text

    def get_name(self):
        return "Word Count"

class UpperCasePlugin(Plugin):
    def execute(self, text):
        
        return text.upper()  # TODO: return text.upper()

    def get_name(self):
        return "Upper Case"

class TextEditor:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin):
        # TODO: Add the plugin to the list and print "Registered: [name]"
        self.plugins.append(plugin)
        print(f'Registered: {plugin.get_name()}')

    def run_plugins(self, text):
        # TODO: Run each plugin in sequence, passing output of one as input to the next
        # Print "Running: [name]" before each plugin
        # Return the final processed text
        for plugin in self.plugins:
            print(f'Running: {plugin.get_name()}')
            text = plugin.execute(text)
        return text
from abc import ABC, abstractmethod
import math

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f'Drawing circle with radius {self.radius}')
         # TODO: print "Drawing circle with radius X"

    def get_area(self):
        return math.pi * self.radius ** 2
          # TODO: return π * r²

class Rectangle(Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f'Drawing rectangle {self.width}x{self.height}')
         # TODO: print "Drawing rectangle WxH"

    def get_area(self):
        return self.width * self.height
        return 0  # TODO: return width * height

class Triangle(Drawable):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def draw(self):
        print(f"Drawing triangle with base {self.base} and height {self.height}")
        pass  # TODO: print "Drawing triangle with base B and height H"

    def get_area(self):
        return 0.5 * self.base * self.height
         # TODO: return 0.5 * base * height

class Canvas:
    def draw_all(self, shapes):
        # TODO: For each shape, call draw() and print its area
        for shape in shapes:
            shape.draw()
            print(f'  Area: {shape.get_area():.2f}\n')

if __name__ == "__main__":
    canvas = Canvas()

    shapes = [
        Circle(5.0),
        Rectangle(4.0, 6.0),
        Triangle(3.0, 8.0),
    ]

    canvas.draw_all(shapes)
    
    editor = TextEditor()
    editor.register_plugin(SpellCheckPlugin())
    editor.register_plugin(WordCountPlugin())

    result = editor.run_plugins("teh quick brown fox adn teh lazy dog")
    print(f"\nFinal output: {result}")