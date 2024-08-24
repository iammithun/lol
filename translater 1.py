# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:27:31 2024

@author: iamrs
"""

import pyttsx3

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

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage
english_text = input("Enter text to translate and speak: ")
japanese_text = translate_to_japanese(english_text)
print("Translated text in Japanese:", japanese_text)
speak(japanese_text)
