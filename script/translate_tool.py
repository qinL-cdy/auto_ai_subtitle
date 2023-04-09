from translate import Translator
import re


def __translate(translator, text, n):
    print("\rtranslate line in: ", n + 1, end="")

    if text == "" or text == '\n':
        return text

    text = text.rstrip('\n')
    if re.match(r"^[0-9]+$", text):
        return add_newline_if_missing(text)

    if re.match(r"\d{2}:\d{2}:\d{2},\d{3}\s-->\s\d{2}:\d{2}:\d{2},\d{3}", text):
        return add_newline_if_missing(text)

    return add_newline_if_missing(translator.translate(text))


def add_newline_if_missing(s):
    if not s.endswith('\n'):
        s += '\n'
    return s


def translate_file(translator_fun, file1, file2, translator=None):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'w', encoding='utf-8') as f2:
        lines = f1.readlines()
        print("translate file total lines: ", len(lines))
        f2.writelines([translator_fun(translator, line, n) for n, line in enumerate(lines)])
        print("\ntranslate write file done")


def do_translate(file1, file2, form, to):
    translator = Translator(from_lang=form, to_lang=to)
    translate_file(__translate, file1, file2, translator)


if __name__ == '__main__':
    do_translate('test.srt', 'test1.srt', 'ja', 'zh')
