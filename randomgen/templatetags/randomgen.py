import random
import hashlib
import os

from django import template

register = template.Library()

@register.tag(name="randomgen")
def randomgen(parser, token):
    items = []
    bits =  token.split_contents()
    for item in bits:
        items.append(item)
    return RandomgenNode(items[1:])
    
class RandomgenNode(template.Node):
    def __init__(self, items):
        self.items = []
        for item in items:
            self.items.append(item)
    
    def render(self, context):
        if 'hash' in self.items:
            result = os.urandom(16).encode('hex')
        elif 'float' in self.items:
            result = random.uniform(int(self.items[0]), int(self.items[1]))
        elif not self.items:
            result = random.random()
        else:
            result = random.randint(int(self.items[0]), int(self.items[1]))
        return result
            