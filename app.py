from pyramid.config import Configurator
from pyramid.response import Response

program_active = True

def pigLatin(original):
    if len(original) > 0 and original[0] in ('a', 'e', 'i', 'o', 'u') and original.isalpha():
        word = original.lower()
        new_word = word + pyg
        return new_word
    elif len(original) > 0 and original.isalpha():
        word = original.lower()
        vowel_indices = [idx for idx, ch in enumerate(original) if ch.lower() in 'aeiou']
        splitIdx = vowel_indices[0]
        first = original[0 : splitIdx]
        new_word = word[splitIdx: len(word)] + first + pyg
        return new_word
    else:
        print 'empty'

while program_active:
    print 'Type \'quit\' to exit'
    pyg = 'ay'

    sentence = raw_input('Enter a sentence:')
    if sentence == 'quit':
        program_active = False

    output = []

    sentArr = sentence.split( )

    for item in sentArr:
        output.append(pigLatin(item))
        answer = ' '.join(output)
    print answer
    output = []
    sentArr = []


config = Configurator()
config.add_route('hello', '/hello')
config.add_view(hello_world, route_name='hello')
app = config.make_wsgi_app()
