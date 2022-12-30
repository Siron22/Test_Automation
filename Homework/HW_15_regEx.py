"""
Есть фрагмент текста, состоящий из предложений.
Предложение - это строка, которая начинается с большой буквы и заканчивается точкой, вопросительным или восклицательным знаком (или несколькими такими знаками).
Слова состоят только из латинских букв, разделяются/отделяются пробелами или запятыми с пробелами.
Предложение может состоять из одного слова.
Составить предложение из первых слов предложений фрагмента.
Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой.
Предложение должно заканчиваться точкой.
"""

import re
def generate_sentence(text: str) -> str:
    container = []
    sentence_pattern = '[A-Z]{1}[^\.\?\!]*[\.|\?|!]{1}'
    sentences = re.findall(sentence_pattern, text)
    first_word_pattern = '([A-Z]{1}[a-z]*)[\s|,\s\|\.]'
    for one_sentence in sentences:
        first_word = re.findall(first_word_pattern, one_sentence)
        container.append(first_word[0])
    new_sentence = container[0]
    for word in container[1:]:
        new_sentence += ' ' + word.lower()
    new_sentence += '.'
    print(new_sentence)
    return new_sentence











text = "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."
text1 = "Hola..."
assert generate_sentence(text) == "Hello and who or yes claro."
assert generate_sentence(text1) == "Hola."

