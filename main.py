from greets import greetings
from translate import Translator

translator = Translator(to_lang="es")

for g in greetings:
    print(g+' - ', translator.translate(g).title())