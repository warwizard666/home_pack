import pyjokes
from translate import Translator


def translator_jokes():
    translator = Translator(from_lang="English", to_lang="russian")
    text_eng = pyjokes.get_joke()
    text_rus = translator.translate(text_eng)
    print(text_rus)


if __name__ == '__main__':
    translator_jokes()
