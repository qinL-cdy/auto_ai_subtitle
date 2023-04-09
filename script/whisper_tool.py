import whisper


def reformat_time(second):
    m, s = divmod(second, 60)
    h, m = divmod(m, 60)
    hms = "%02d:%02d:%s" % (h, m, str('%.3f' % s).zfill(6))
    hms = hms.replace('.', ',')
    return hms


def write_srt(seg, srt_path):
    with open(srt_path, 'w', encoding='utf-8') as f:
        write_content = [str(n + 1) + '\n'
                         + reformat_time(i['start'])
                         + ' --> '
                         + reformat_time(i['end']) + '\n'
                         + i['text'] + '\n\n'
                         for n, i in enumerate(seg)]
        f.writelines(write_content)


def do_whisper(audio, srt_path):
    model = whisper.load_model("base")
    print("whisper working...")
    result = model.transcribe(audio)
    print("whisper execute success")
    print("writing srt file...")
    write_srt(result['segments'], srt_path)
    print("write srt success")


if __name__ == '__main__':
    do_whisper("test.mp3", "test.srt")
