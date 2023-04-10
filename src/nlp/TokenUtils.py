from nltk import sent_tokenize
from src.audio.const import TRANSCRIPT_FOLDER_NAME
from src.utils import day_time_generator


def parse(transcript_file_name) -> list[str]:
    """
    parse function can separate a long sentence into a small sentence using a nltk.
    :param transcript_file:
    :return:
    """
    transcript_file = open(transcript_file_name, "r")
    transcript = transcript_file.read()
    return sent_tokenize(text=transcript, language="english")


if __name__ == "__main__":
    txt = parse(f"{TRANSCRIPT_FOLDER_NAME}/transcript_{day_time_generator()}.txt")
    print(txt)