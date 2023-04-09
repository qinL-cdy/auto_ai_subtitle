import ffmpeg


def audio_extract(input, output):
    ffmpeg.input(input, vn=None).output(output).run()
