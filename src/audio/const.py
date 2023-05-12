from src import utils

def transcript_folder_format(date, resource_file_path="resources"):
    return f"{resource_file_path}/{date}/transcript"

def audio_folder_format(date, resource_file_path="resources"):
    return f"{resource_file_path}/{date}/audio"

def original_audio_folder_format(date, resource_file_path="resources"):
    return f"{resource_file_path}/{date}/audio/original"

def review_folder_format(date, resource_file_path="resources"):
    return f"{resource_file_path}/{date}/review"

ORIGINAL_AUDIO_FOLDER_NAME = original_audio_folder_format(utils.day_time_generator())
AUDIO_FOLDER_NAME = audio_folder_format(utils.day_time_generator())
TRANSCRIPT_FOLDER_NAME = transcript_folder_format(utils.day_time_generator())
REVIEW_FOLDER_NAME = review_folder_format(utils.day_time_generator())