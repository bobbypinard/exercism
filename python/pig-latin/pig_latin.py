import re
def translate(text):
    pig = []
    for word in text.split():
        regex = r'([xy](?=[aeiouy])|s*qu|[bcdfghjklmnpqrstvwz]*)(.*)'
        pig.append(re.sub(regex, r'\2\1', word) + 'ay')
    return ' '.join(pig)
