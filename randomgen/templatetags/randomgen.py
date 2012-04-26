import datetime
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
			
			
"""
class CurrentTimeNode(template.Node):
		def __init__(self, format_string):
				self.format_string = format_string
		def render(self, context):
				return datetime.datetime.now().strftime(self.format_string)
				
@register.tag(name="randomgen")
def do_current_time(parser, token):
		try:
				# split_contents() knows not to split quoted strings.
				tag_name, format_string = token.split_contents()
		except ValueError:
				raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
		if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
				raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
		return CurrentTimeNode(format_string[1:-1])
"""