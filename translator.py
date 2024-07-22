from translate import Translator

translator = Translator(to_lang='ja')
with open('to-translate.txt', 'r') as f:
    text = f.read()
    translation = translator.translate(text)
    with open('translated.txt', 'w', encoding='utf-8') as t:
        t.write(translation)

print(text)
print(translation)


