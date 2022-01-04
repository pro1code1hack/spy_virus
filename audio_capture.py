import sounddevice as sd
from scipy.io.wavfile import write
fs = 44100  # Частота дискретизации
seconds = 3  # Продолжительность записи
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Дождитесь окончания записи
write('output.wav', fs, myrecording)  # Сохранить как WAV файл