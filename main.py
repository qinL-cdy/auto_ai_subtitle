import yaml

from script import translate_tool, audio_tool, whisper_tool

if __name__ == '__main__':
    with open('config.yaml') as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)

    print("audio extract begin")
    audio_tool.audio_extract(config['input'], config['output'])
    print("audio extract success")

    print("whisper begin")
    whisper_tool.do_whisper(config['output'], config['srt_path'])
    print("whisper success")

    print("translate begin")
    translate_tool.do_translate(config['srt_path'], config['srt_translate_path'], config['from'], config['to'])
    print("translate success")

    print("success")
