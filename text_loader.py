from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv()

# Groq-hosted model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

prompt = PromptTemplate(
    template="Write a summary for the following poem:\n{poem}",
    input_variables=["poem"]
)


parser = StrOutputParser()


loader = TextLoader(BASE_DIR / "cricket.txt",encoding="utf-8")

doc = loader.load()


print(type(doc))
print(len(doc))

print(doc[0].page_content)
print(doc[0].metadata)


chain = prompt | model | parser

print(chain.invoke({"poem": doc[0].page_content}))