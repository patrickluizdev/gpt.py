import openai
import configparser
import os


# Define a chave da API do OpenAI
config = configparser.ConfigParser()
config.read('config.ini')
openai.api_key = config.get('api', "api_key")
# Pegue sua chave da APT no site "https://chat.openai.com/"


# Define o modelo que será utilizado
model_engine = "text-davinci-003"


# Faz uma Requisição para o ChatGPT
def ask(question):
    
    response = openai.Completion.create(
        engine=model_engine,
        prompt=question + ".",
        max_tokens=300,
        n=1,
        stop=".",
        temperature=0.2,
    )

    return response.choices[0].text.strip()

# Pede ao usuário uma entrada e obtém uma resposta do ChatGPT

while True:
    before = "explique em poucas palavras "
    question = input("Qual a sua pergunta? ")
    answer = ask(before + question)
    print(answer)
