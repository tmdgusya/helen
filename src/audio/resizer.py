from pydub import AudioSegment
import math
from const import (
    AUDIO_FOLDER_NAME
)


class Resizer:

    def __init__(self, audio_file_name: str):
        """
        TODO: If not exist file in directory, then raise Error
        :param audio_file_name: voice file
        """
        split_file_name = audio_file_name.split("/")
        self.file_name = split_file_name[len(split_file_name) - 1]
        print(f'fileName : {self.file_name}')
        self.window_size = 10 * 60 * 1000  # 10 minutes
        self.audio = AudioSegment.from_wav(audio_file_name)

    def get_resize_window(self) -> int:
        """
        To calculate maximum window size for sending whisper.

        If maximum size is one, then you don't need to resize the voice file.
        But, If maximum size is over one, then you must need to resize the voice file using [resize] function.
        :return: window_size
        """
        duration = self.audio.duration_seconds
        minutes = duration / 60
        return int(math.ceil(minutes / 10))

    def resize(self):
        """
        Properly resize the duration of wav file to be within 10 minutes.
        :return: nothing
        """
        windows = self.get_resize_window()
        if windows == 0:
            print("You have an audio which is properly size")
            pass
        acc = 0
        for i in range(0, windows):
            resize_file_name = f"{self.file_name}_{i}.wav"
            print(f"resizing... {acc} to {self.window_size} : file_name: {resize_file_name}")
            segment = self.audio[acc:(self.window_size * (i + 1))]
            folder_name = AUDIO_FOLDER_NAME
            segment.export(f"{folder_name}/{resize_file_name}", format="wav")
            acc += self.window_size
        return


if __name__ == "__main__":
    resizer = Resizer("../../test.wav")
    resizer.resize()
