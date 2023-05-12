import sys
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)
from audio.const import (
    REVIEW_FOLDER_NAME,
    TRANSCRIPT_FOLDER_NAME,
    transcript_folder_format,
    review_folder_format,
)
from utils import (
    create_folder,
    day_time_generator
)
from nlp.TokenUtils import parse


if __name__ == "__main__":
    # load dotenv to configure for os environment
    load_dotenv()

    print("Check the number of arguments", sys.argv)

    folder_name = ""

    if len(sys.argv) > 1:
        print("User wants to use the date as an folder name")
        folder_name = sys.argv[1]
        print("User wants to use the date as an folder name : ", folder_name)

    # define a role
    role_prompt = """
    As an English teacher, your task is to correct the sentence written by the student and provide an explanation for why it is incorrect or why it needs to be corrected. Additionally, if you can provide any relevant grammatical information, please do so and provide an example of how it can be used in conversations. Please follow the rules below:
    Rules:
    - If you provide grammatical information, please include an example of how it can be used in conversations.
    - The student sentence will be presented in the following format:
        - Student sentence: 'sentence'
    - You must provide a detailed explanation for why the sentence is incorrect.
    - You do not need to evaluate whether the sentence is true or not, but rather focus on why it is grammatically incorrect.
    - Your answer should follow this format:
        - Original sentence (written by the student):
        - Grammatically correct sentence:
        - Explanation (in bullet point form):
        - Example conversation (briefly):
    Please only focus on the sentence written by the student provided in the following format:
        - Student sentence: {sentence}
    """

    prompt = PromptTemplate(
        input_variables=["sentence"],
        template=role_prompt,
    )

    # set machine
    chat = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    memory = ConversationBufferWindowMemory(k=2)
    # combine machine and template
    chain = LLMChain(llm=chat, prompt=prompt, verbose=True, memory=memory)
    
    print("folder name : ", folder_name)

    if folder_name != "":
        print("User wants to use the date as an folder name : ", folder_name)
        sentences_of_transcript = parse(f"{transcript_folder_format(folder_name, 'resources')}/transcript_{folder_name}.txt")
        review_folder_name = review_folder_format(folder_name, 'resources')
    else:
        sentences_of_transcript = parse(f"{TRANSCRIPT_FOLDER_NAME}/transcript_{day_time_generator()}.txt")
        review_folder_name = REVIEW_FOLDER_NAME

    create_folder(review_folder_name)
    print(review_folder_name)

    for sentence in sentences_of_transcript:
        """
        TODO: Batch Process
        Because, Now we send only one sentence. 
        But, We have to send folding sentence which means fold over two sentences.
        """
        result = chain.predict(sentence=sentence)
        print(result)
        with open(f"{review_folder_name}/fiexed_daytime.txt", "a") as f:
            f.write(result)
            f.write("\n")
            f.write("\n")

