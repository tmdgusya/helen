import pyaudio
import wave
from src import utils
from const import (
    ORIGINAL_AUDIO_FOLDER_NAME
)


class Audio:
    """
    Audio class can record your voice.
    And make .wav file from your voices.
    """
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.sound_channel = 1
        self.buffer_size = 1024
        self.format = pyaudio.paInt16
        self.frame_late = 44100

    def record(self):
        """
        record the voice using desired device.
        :return:
        """
        print("Recording...")
        frames = []

        stream = self.audio.open(
            format=self.format,
            channels=self.sound_channel,
            rate=self.frame_late,
            input=True,
            # chunk size
            frames_per_buffer=self.buffer_size
        )
        try:
            while True:
                data = stream.read(self.buffer_size)
                frames.append(data)
        except KeyboardInterrupt:
            print("Recording is finished.")
            pass

        stream.stop_stream()
        stream.close()
        self.audio.terminate()

        utils.create_folder(ORIGINAL_AUDIO_FOLDER_NAME)
        sound_file = wave.open(f"{ORIGINAL_AUDIO_FOLDER_NAME}/{utils.day_time_generator()}.wav", "wb")
        sound_file.setnchannels(self.sound_channel)
        sound_file.setsampwidth(self.audio.get_sample_size(self.format))
        sound_file.setframerate(self.frame_late)

        sound_file.writeframes(b''.join(frames))
        sound_file.close()


if __name__ == "__main__":
    audio = Audio()
    audio.record()
