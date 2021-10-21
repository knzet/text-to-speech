from pydub import AudioSegment
from pydub.playback import play
import sys

if (len(sys.argv) > 1):
    # print(type(int(sys.argv[1])))
    fadeMs = ((int(sys.argv[1])))
    print('delay time: %d', fadeMs)

else:
    fadeMs = 150
# sounds = AudioSegment.from_mp3('assets/EPS.mp3')
sounds = AudioSegment.empty()
startFlag = True
f = open("output.txt", "r")
phones = f.read().replace('\n', '').split(' ')
# print(phones)

for phone in phones:
    if phone == '<eps>':
        print(" ")
        sounds = sounds.append(AudioSegment.from_mp3('assets/EPS.mp3'),
                               crossfade=400)
    else:
        # print(phone, end=" ")
        print(phone)
        sound = AudioSegment.from_mp3('assets/' + phone + '.mp3')
        # print(sound.duration_seconds)
        # sounds = sounds + sound
        if startFlag:
            sounds = sounds.append(sound, crossfade=0)
            startFlag = False
        else:
            sounds = sounds.append(sound, crossfade=fadeMs)
# print("")
sounds.export('tts.mp3', format="mp3")
play(sounds)