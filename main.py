#phones={'K', 'EH1', 'N', 'AH0', 'D', 'IY0', '<eps>', 'AH0', 'L', 'AE1', 'S', '<eps>', 'CH', 'IY1', 'Z', '<eps>'}
from playsound import playsound
# import pygame
# from pygame import mixer
from pydub import AudioSegment
from pydub.playback import play
sounds = AudioSegment.from_mp3('assets/EPS.mp3')
# sounds = AudioSegment.empty()

f = open("output.txt", "r")
# pygame.init()
# mixer.init()
phones = f.read().replace('\n', '').split(' ')
print(phones)
# playsound('assets/K.mp3')
# trackone = './assets/' + phones[0] + '.ogg'
# mixer.music.load(trackone)
# for phone in phones:
#     track = 'assets/' + phone + '.mp3'

# tracks = map(lambda phone: 'assets/' + phone + '.mp3', phones)
# [mixer.music.queue(track) for track in tracks]
# mixer.music.play()

for phone in phones:
    if phone == '<eps>':
        print(phone)
        sounds += AudioSegment.from_mp3('assets/EPS.mp3')
    else:
        print(phone)
        sound = AudioSegment.from_mp3('assets/' + phone + '.mp3')
        # print(sound.duration_seconds)
        # sounds = sounds + sound
        sounds = sounds.append(sound, crossfade=150)

sounds.export('tts.mp3', format="mp3")
play(sounds)
# play(AudioSegment.from_mp3('assets/T.mp3'))
# play(AudioSegment.from_wav('tts.wav'))
# playsound('tts.wav')
# for phone in phones:
#     if phone == '<eps>':
#         playsound('assets/EPS.mp3')  #todo: short pause
#     else:
#         playsound('assets/' + phone + '.mp3')
