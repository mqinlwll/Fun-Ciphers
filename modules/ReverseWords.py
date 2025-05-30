def encode(text):
    return ' '.join(word[::-1] for word in text.split())

def decode(text):
    return ' '.join(word[::-1] for word in text.split())

def brute_force_decode(text):
    return [' '.join(word[::-1] for word in text.split())]
