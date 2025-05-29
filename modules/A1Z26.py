def encode(text):
    words = text.split()
    encoded_words = []
    for word in words:
        encoded_word = '-'.join(str(ord(char.upper()) - ord('A') + 1) for char in word if char.isalpha())
        encoded_words.append(encoded_word)
    return ' '.join(encoded_words)

def decode(encoded_text):
    encoded_words = encoded_text.split()
    decoded_words = []
    for encoded_word in encoded_words:
        numbers = encoded_word.split('-')
        decoded_word = ''.join(chr(int(num) + ord('A') - 1) for num in numbers)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)
