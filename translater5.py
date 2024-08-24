
def translate_to_chinese_meaning(text):
    # English to Chinese meaning dictionary
    translation_dict = {
        'a': '爱 (ài)', 
        'b': '百 (bǎi)', 
        'c': '成 (chéng)', 
        'd': '大 (dà)', 
        'e': '饿 (è)',
        'f': '富 (fù)', 
        'g': '高 (gāo)', 
        'h': '好 (hǎo)', 
        'i': '爱 (ài)', 
        'j': '家 (jiā)',
        'k': '开 (kāi)', 
        'l': '乐 (lè)', 
        'm': '梦 (mèng)', 
        'n': '你 (nǐ)', 
        'o': '哦 (ò)',
        'p': '朋 (péng)', 
        'q': '起 (qǐ)', 
        'r': '人 (rén)', 
        's': '世 (shì)', 
        't': '天 (tiān)',
        'u': '有 (yǒu)', 
        'v': '无 (wú)', 
        'w': '我 (wǒ)', 
        'x': '喜 (xǐ)', 
        'y': '月 (yuè)',
        'z': '子 (zǐ)'
    }
    
    # Translate text to Chinese meaning
    translated_text = ''
    for char in text:
        if char.lower() in translation_dict:
            translated_text += translation_dict[char.lower()] + ' '
        else:
            translated_text += char + ' '
    return translated_text

# Example usage
english_text = input("Enter text to translate to Chinese meaning: ")
chinese_meaning_text = translate_to_chinese_meaning(english_text)
print("Translated text in Chinese meaning:", chinese_meaning_text)

