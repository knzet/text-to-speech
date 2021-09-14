files = [
    "AE1.mp3", "AH0.mp3", "AY1.mp3", "CH.mp3", "CH.wav", "D.mp3", "EH1.mp3",
    "EPS.mp3", "G.mp3", "HH.mp3", "IY0.mp3", "IY1.mp3", "K.mp3", "L.mp3",
    "M.mp3", "N.mp3", "OW2.mp3", "R.mp3", "S.mp3", "Z.mp3"
]
import pydub
from pydub import AudioSegment
for file in files:
    AudioSegment.from_mp3("assets/" + file).export(file[0, -4] + '.ogg',
                                                   format='ogg')
