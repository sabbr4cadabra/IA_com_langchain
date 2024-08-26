from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
chave_api = os.getenv("OPENAI_API_KEY")

# Criando o template de prompt com as mensagens
template_message = ChatPromptTemplate.from_messages([
    SystemMessage(content="Translate the following text to {language}"),
    HumanMessage(content="I want to translate this: {text}")
])

# Inserindo o modelo escolhido do ChatGPT
model = ChatOpenAI(model="gpt-3.5-turbo-16k", api_key=chave_api)
parser = StrOutputParser()

# Formatar as mensagens usando o template
formatted_prompt = template_message.format_prompt(
    language="Português", text="Follow the page and keep stay up with the news"
)

# Criando a chain e invocando o modelo
response = model.invoke(formatted_prompt.to_messages())

# Obtendo o texto da resposta e exibindo
text = parser.parse(response)
print(text)
