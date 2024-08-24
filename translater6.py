
def translate_to_chinese(text):
    # English to Chinese transliteration dictionary
    transliteration_dict = {
        'a': '阿', 'b': '比', 'c': '西', 'd': '迪', 'e': '伊',
        'f': '艾弗', 'g': '吉', 'h': '艾尺', 'i': '艾', 'j': '杰',
        'k': '开', 'l': '艾勒', 'm': '艾马', 'n': '艾娜', 'o': '哦',
        'p': '屁', 'q': '吉吾', 'r': '艾儿', 's': '艾丝', 't': '提',
        'u': '伊吾', 'v': '维', 'w': '豆贝尔维', 'x': '艾克斯', 'y': '吾艾',
        'z': '贼德'
    }
    
    # Translate text to Chinese transliteration
    translated_text = ''
    for char in text:
        if char.lower() in transliteration_dict:
            translated_text += transliteration_dict[char.lower()]
        else:
            translated_text += char
    return translated_text

# Example usage
english_text = input("Enter text to translate to Chinese: ")
chinese_text = translate_to_chinese(english_text)
print("Translated text in Chinese:", chinese_text)

