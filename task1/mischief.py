import re
from datetime import datetime

def date_mischief(day: int) -> str:
    if 11 <= day <= 13:
        return f"{day}th"
    if day % 10 == 1:
        return f"{day}st"
    if day % 10 == 2:
        return f"{day}nd"
    if day % 10 == 3:
        return f"{day}rd"
    return f"{day}th"

def number_mischief(num: str) -> str:
  roman_map = {
        '0': '',
        '1': 'I', 
        '2': 'II', 
        '3': 'III',
        '4': 'IV', 
        '5': 'V', 
        '6': 'VI', 
        '7': 'VII',
        '8': 'VIII', 
        '9': 'IX'}
  return ''.join(roman_map.get(d, '') for d in num)

def lang_mischief(text: str) -> str:
  # simple dictionary-driven replacement (handles lowercase and Capitalized)
  lang_map = {'python': '🐍',
                'java': '☕',
                'ruby': '♦️ ',
                'C#': '🎼'}
  for lang, emoji in lang_map.items():
        text = text.replace(lang, emoji)
        text = text.replace(lang.capitalize(), emoji) #for captial first letter
  return text

def transform_text(text: str) -> str:
    # first map language names to emojis
    text = lang_mischief(text)

    #convert date to more readable format
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    def date_to_words(m):
        dt = datetime.strptime(m.group(0), "%Y-%m-%d")
        return f"{date_mischief(dt.day)} {dt.strftime('%B')} {dt.year}"
    text = re.sub(date_pattern, date_to_words, text)

    # then convert any 10-digit number starting with '9' to roman-per-digit
    transoformed_text = []
    i = 0
    length = len(text)
    while i < length:
        if text.startswith('9', i) and i + 10 <= length and text[i:i+10].isdigit():
            transoformed_text.append(number_mischief(text[i:i+10]))
            i += 10
        else:
            transoformed_text.append(text[i])
            i += 1
    return ''.join(transoformed_text)

text="Call me at 9812345678 on 2025-08-23. I love Python more than Java. Maye ruby and C# are good too."
print(transform_text(text)) 
