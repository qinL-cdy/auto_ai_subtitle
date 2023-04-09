from translate import Translator
import re


def __translate(translator, text, n):
    print("\rtranslate line in: ", n + 1, end="")
    if not re.match(r"[^->\d\n]", text):
        return text
    return translator.translate(text)


def translate_file(translator_fun, file1, file2, translator=None):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'w', encoding='utf-8') as f2:
        lines = f1.readlines()
        print("translate file total lines: ", len(lines))
        f2.writelines([translator_fun(translator, line, n) for n, line in enumerate(lines)])


def do_translate(file1, file2, form, to):
    translator = Translator(from_lang=form, to_lang=to)
    translate_file(__translate, file1, file2, translator)


if __name__ == '__main__':
    do_translate('test.srt', 'test1.srt', 'ja', 'zh')
