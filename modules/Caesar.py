def shift_text(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            pos = ord(char) - ord('A')
            new_pos = (pos + shift) % 26
            new_char = chr(ord('A') + new_pos)
        elif char.islower():
            pos = ord(char) - ord('a')
            new_pos = (pos + shift) % 26
            new_char = chr(ord('a') + new_pos)
        else:
            new_char = char
        result += new_char
    return result

def encode(text, shift):
    return shift_text(text, shift)

def decode(text, shift):
    return shift_text(text, -shift)

def brute_force_decode(text):
    return [shift_text(text, -i) for i in range(26)]
