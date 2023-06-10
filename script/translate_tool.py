from translate import Translator
import re
import threading


def __translate(translator, text, n):
    # print("\rtranslate line in: ", n + 1, end="")
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


def translate_task(lines, translator_fun, result_map, i, translator):
    print("thread id: ", i, "lines num: ", len(lines))
    result_map[i] = [translator_fun(translator, line, n) for n, line in enumerate(lines)]


def translate_file(translator_fun, file1, file2, thread_nums, translator=None):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'w', encoding='utf-8') as f2:
        lines = f1.readlines()
        print("translate file total lines: ", len(lines))
        result = get_translate_result(lines, thread_nums, translator, translator_fun)
        f2.writelines(result)
        print("\ntranslate write file done")


def get_translate_result(lines, thread_nums, translator, translator_fun):
    result_map = get_translate_threads_result(lines, thread_nums, translator, translator_fun)
    result = []
    for key in sorted(result_map):
        result.extend(result_map.get(key))
    return result


def get_translate_threads_result(lines, thread_nums, translator, translator_fun):
    result_map = {}
    threads = []
    n = len(lines) // thread_nums
    for i in range(1, thread_nums + 1):
        threads.append(
            threading.Thread(target=translate_task, args=(
                get_split_lines(i, lines, n, thread_nums), translator_fun, result_map, i, translator)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return result_map


def get_split_lines(i, lines, n, thread_nums):
    if n * i <= len(lines):
        split_line = lines[(i - 1) * n:i * n]
    else:
        split_line = lines[(i - 1) * n:]
    if i == thread_nums and n * i < len(lines):
        split_line = lines[(i - 1) * n:]
    return split_line


def do_translate(file1, file2, form, to, thread_nums):
    translator = Translator(from_lang=form, to_lang=to)
    translate_file(__translate, file1, file2, thread_nums, translator)


if __name__ == '__main__':
    do_translate('test.srt', 'test1.srt', 'ja', 'zh')
