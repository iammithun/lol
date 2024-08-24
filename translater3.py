def translate_to_tamil(text):
    # English to Tamil dictionary
    translation_dict = {
        'a': 'அ', 'b': 'ப', 'c': 'ச', 'd': 'ட', 'e': 'எ',
        'f': 'ஃ', 'g': 'க', 'h': 'ஹ', 'i': 'இ', 'j': 'ஜ',
        'k': 'க', 'l': 'ல', 'm': 'ம', 'n': 'ன', 'o': 'ஒ',
        'p': 'ப', 'q': 'ஃ', 'r': 'ர', 's': 'ஸ', 't': 'ட',
        'u': 'உ', 'v': 'வ', 'w': 'வ', 'x': 'ஃ', 'y': 'ய',
        'z': 'ஜ'
    }
    
    # Translate text to Tamil
    translated_text = ''
    for char in text:
        if char.lower() in translation_dict:
            translated_text += translation_dict[char.lower()]
        else:
            translated_text += char
    return translated_text

# Example usage
english_text = input("Enter text to translate to Tamil: ")
tamil_text = translate_to_tamil(english_text)
print("Translated text in Tamil:", tamil_text)
