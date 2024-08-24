
def translate_to_japanese(text):
    # English to Japanese dictionary
    translation_dict = {
        'a': 'あ', 'b': 'い', 'c': 'う', 'd': 'え', 'e': 'お',
        'f': 'か', 'g': 'き', 'h': 'く', 'i': 'け', 'j': 'こ',
        'k': 'さ', 'l': 'し', 'm': 'す', 'n': 'せ', 'o': 'そ',
        'p': 'た', 'q': 'ち', 'r': 'つ', 's': 'て', 't': 'と',
        'u': 'な', 'v': 'に', 'w': 'ぬ', 'x': 'ね', 'y': 'の',
        'z': 'は'
    }
    
    # Translate text to Japanese
    translated_text = ''
    for char in text:
        if char.lower() in translation_dict:
            translated_text += translation_dict[char.lower()]
        else:
            translated_text += char
    return translated_text

# Example usage
english_text = "hojoghbdhfmkvifvkadfirfsm"
japanese_text = translate_to_japanese(english_text)
print(japanese_text)
