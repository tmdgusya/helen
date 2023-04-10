import os
import openai
from dotenv import load_dotenv
from src.audio import const
from src import utils


class Whisper:

    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = "whisper-1"
        self.pre_fix = f"transcript_{utils.day_time_generator()}"
        self.ext = ".txt"

    def createTranscript(self, audio_file_name):
        """
        Make Transcript And Save Transcript to file
        """
        audio_file = open(audio_file_name, "rb")
        utils.create_folder(const.TRANSCRIPT_FOLDER_NAME)
        transcript = openai.Audio.transcribe(self.model, audio_file)
        print(transcript.text)
        file = open(f"{const.TRANSCRIPT_FOLDER_NAME}/{self.pre_fix}{self.ext}", "a")
        file.write(transcript.text)
        file.close()


if __name__ == "__main__":
    whisper = Whisper()

    files = utils.get_files(const.AUDIO_FOLDER_NAME)
    """sort by natural order"""
    files.sort()
    for file in files:
        print(file)
        whisper.createTranscript(f"{const.AUDIO_FOLDER_NAME}/{file}")
