from dotenv import load_dotenv
from langchain.llms import OpenAI

if __name__ == "__main__":
    # load dotenv to configure for os environment
    load_dotenv()

    # set machine
    llm = OpenAI(temperature=0.9)

    prompt = """
    What would be a good company name for a company that makes colorful socks?
    """

    print(llm(prompt))