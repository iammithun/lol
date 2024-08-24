def translate_to_tamil_meaning(text):
    # English to Tamil meaning dictionary
    translation_dict = {
        'a': 'அயல்பாய்வு (Ayalpaayvu)', 
        'b': 'பணி (Pani)', 
        'c': 'செயல் (Seyal)', 
        'd': 'தொடர்பு (Thodarpu)', 
        'e': 'என்று (Endru)',
        'f': 'போது (Pothu)', 
        'g': 'நோக்கம் (Nokkam)', 
        'h': 'ஆதரவு (Aatharavu)', 
        'i': 'ஒப்புதல் (Opputhal)', 
        'j': 'அறிவு (Arivu)',
        'k': 'படை (Padai)', 
        'l': 'படைப்பு (Padaippu)', 
        'm': 'நிரப்பு (Nirappu)', 
        'n': 'உள்ளம் (Ullam)', 
        'o': 'அறிவு (Arivu)',
        'p': 'அறிவு (Arivu)', 
        'q': 'அறிவு (Arivu)', 
        'r': 'அறிவு (Arivu)', 
        's': 'அறிவு (Arivu)', 
        't': 'அறிவு (Arivu)',
        'u': 'அறிவு (Arivu)', 
        'v': 'அறிவு (Arivu)', 
        'w': 'அறிவு (Arivu)', 
        'x': 'அறிவு (Arivu)', 
        'y': 'அறிவு (Arivu)',
        'z': 'அறிவு (Arivu)'
    }
    
    # Translate text to Tamil meaning
    translated_text = ''
    for char in text:
        if char.lower() in translation_dict:
            translated_text += translation_dict[char.lower()] + ' '
        else:
            translated_text += char + ' '
    return translated_text

# Example usage
english_text = input("Enter text to translate to Tamil meaning: ")
tamil_meaning_text = translate_to_tamil_meaning(english_text)
print("Translated text in Tamil meaning:", tamil_meaning_text)
