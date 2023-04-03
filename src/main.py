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


def parse(transcript_file):
    """
    parse function can separate a long sentence into a small sentence using a newline separator.
    :param transcript_file:
    :return:
    """
    pass


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
    - You can just answer whether the sentence grammatically wrong or correct. You don't care about whether the sentence true or not.\n
    - You don't need to understand that the sentence is true or not. You explain why the sentence is grammatically wrong.\n
    - Your answer must look something like this format(must!!)\n
        - format:\n
            - original sentence(that written by me):\n
            - grammatically correct sentence:\n
            - explain(in-detail): (like bullet-form)\n
            - examples conversation(shortly):\n
    \n
    
    You look only below sentence that written by student
    student sentence: {sentence}
    """

    prompt = PromptTemplate(
        input_variables=["sentence"],
        template=role_prompt,
    )

    # set machine
    chat = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # combine machine and template
    chain = LLMChain(llm=chat, prompt=prompt, verbose=True, memory=ConversationBufferWindowMemory(k=2))

    # load .txt file
    # transcript_file = open("transcript.txt", "r")
    # parse(transcript_file)

    result = chain.predict(sentence="""
        'I'll type like below format'
    """)

    print(result)
