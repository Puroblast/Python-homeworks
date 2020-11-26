from translate import Translator

with open("text_4.txt", "r", encoding="utf-8") as file:
    f = file.read()
    translator = Translator(from_lang="English", to_lang="Russian")
    with open("text_44.txt", "w", encoding="utf-8") as new_file:
        new_file.writelines(translator.translate(f"{f}"))
