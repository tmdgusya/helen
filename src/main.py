from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def parse(transcript_file):
    pass


if __name__ == "__main__":
    # load dotenv to configure for os environment
    load_dotenv()

    # define a role
    role_prompt = """
    Act as a English teacher, You have to fix sentence written by student and explain why they are wrong or why you must correct them.
    """

    prompt = PromptTemplate(
        input_variables=["sentence"],
        template="""
    Student sentence: {sentence}
    """
    )

    # set machine
    llm = OpenAI(temperature=0.9)

    # combine machine and template
    chain = LLMChain(llm=llm, prompt=prompt)

    # load .txt file
    transcript_file = open("transcript.txt", "r")

    parse(transcript_file)
