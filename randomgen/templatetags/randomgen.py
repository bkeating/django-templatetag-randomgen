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
            hashmd5 = os.urandom(16).encode('hex')
            return hashmd5
        elif 'float' in self.items:
            num1 = self.items[0]
            num2 = self.items[1]
            floatnum = random.uniform(int(num1), int(num2))
            return floatnum
        elif not self.items:
            floatnum = random.random()
            return floatnum
        else:
            num1 = self.items[0]
            num2 = self.items[1]
            intnum = random.randint(int(num1), int(num2))
            return intnum
            