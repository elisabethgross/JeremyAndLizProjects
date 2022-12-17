# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import soundfile as sf
import pyloudnorm as pyln
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
import moviepy.editor as mp


def measure_loudness():

    for filename in os.listdir('/Users/elisabethgross/Video'):
        if not filename.endswith(".mp4") and not filename.endswith(".mov"):
            continue

        print(filename)
        clip = mp.VideoFileClip(f'/Users/elisabethgross/Video/{filename}')
        noext = os.path.splitext(filename)[0]
        print(f'noext {noext}')
        print(f'writing file')
        clip.audio.write_audiofile(f'/Users/elisabethgross/Audio/{noext}.mp3')

    for filename in os.listdir('/Users/elisabethgross/Audio'):
        if not filename.endswith(".mp3"):
            continue
        data, rate = sf.read(f'/Users/elisabethgross/Audio/{filename}')  # load audio (with shape (samples, channels))
        meter = pyln.Meter(rate)  # create BS.1770 meter
        loudness = meter.integrated_loudness(data)  # measure loudness
        print(filename)
        print('loudness')
        print(loudness)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    measure_loudness()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
