import string

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def is_pangram(sentence):
    sentence = sentence.strip().lower().replace(" ", "")
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    print(sentence)
    for char in alphabet:
        if char not in sentence:
            return False
    return True

print(is_pangram("abcdefghijklm ABCDEFGHIJKLM"))
