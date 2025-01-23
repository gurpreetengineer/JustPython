import random;
import sys;
import os;
from string import Template

'''
MULTI LINE COMMENTS
'''

'''
@ DATA TYPES
> Numbers
> Strings
> Lists
> Tuples
> Dictionaries
'''

print(f'8 // 2 = {8//2}');

firstQuote = '''
Yeah, this is multiline first QUOTE
''';

secondQuote = "\"Escape Character\"";

combinedQuoteFirstWay = firstQuote+ "" + secondQuote;

print('FIRST WAY TO COMBINE: ', combinedQuoteFirstWay);
print('\n' * 3);
print('%s %s %s' % ('This is the second of combining', firstQuote, secondQuote));


'''

Using % Formatting (Old Style)
While %s is the placeholder for strings, here are alternatives for other data types:

> %d for integers
> %f for floats
> %.2f for floats with 2 decimal places
> %x for hexadecimal
> %o for octal
'''

template = Template('My name is $Name, and my new name is also $Name');

print(f'{template.substitute(Name = 'Hitler')}')

