from pydub import AudioSegment
from pydub.playback import play
clip = AudioSegment.empty()
clip.append(AudioSegment.from_mp3('../assets/CH.mp3'))
clip.append(AudioSegment.from_mp3('../assets/IY1.mp3'))
clip.append(AudioSegment.from_mp3('../assets/Z.mp3'))

for cl in clip:
    play(cl)