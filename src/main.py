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
    TRANSCRIPT_FOLDER_NAME
)
from utils import (
    create_folder,
    day_time_generator
)
from nlp.TokenUtils import parse


if __name__ == "__main__":
    # load dotenv to configure for os environment
    load_dotenv()

    # define a role
    role_prompt = """
    Act as a English teacher, You have to fix sentence written by student and explain why they are wrong or why you must correct them.\n
    Additionally, If you can teach some grammatical information, please provide it to them.\n
    Follow below rules.\n
    Rules\n
    - If you provide grammatical information, then you must write example that how to use it in conversations.\n
    - I'll write student sentence as below format\n
        - student sentence: 'sentence'\n
    - You have to explain in detail why It is wrong.\n
    - You can just answer whether the sentence is grammatically wrong or correct. You don't need to care about whether the sentence is true or not.\n
    - You don't need to understand that the sentence is true or not. You explain why the sentence is grammatically wrong.\n
    - Your answer must be in this format\n
        - format:\n
            - original sentence(that written by me):\n
            - grammatically correct sentence:\n
            - explain(in-detail): (like bullet-form)\n
            - examples conversation(shortly):\n
    
    You look only below sentence that written by student
    student sentence: {sentence}
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

    # load .txt file
    # replace this code to get fileName from Transcript function
    sentences_of_transcript = parse(f"{TRANSCRIPT_FOLDER_NAME}/transcript_{day_time_generator()}.txt")
    create_folder(REVIEW_FOLDER_NAME)

    for sentence in sentences_of_transcript:
        """
        TODO: Batch Process
        Because, Now we send only one sentence. 
        But, We have to send folding sentence which means fold over two sentences.
        """
        result = chain.predict(sentence=sentence)
        print(result)
        with open(f"{REVIEW_FOLDER_NAME}/fiexed_daytime.txt", "a") as f:
            f.write(result)
            f.write("/n")

