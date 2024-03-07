import vertexai
from vertexai.language_models import TextGenerationModel
import requests
from bs4 import BeautifulSoup

parameters = {
    "max_output_tokens": 256,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 1
}


def writeURLData():
    links = ['https://www.geeksforgeeks.org/python-programming-language/',
             'https://www.geeksforgeeks.org/machine-learning/?ref=ghm']
    fullpage = ""
    for link in links:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        s = soup.find('div', class_='entry-content')
        print(s)
        if s is not None:
            lines = s.find_all('p')

        for line in lines:
            fullpage = fullpage + line.text

    return fullpage


def vertexAiQes(question):
    vertexai.init(project="dcs-parent-project", location="us-central1")
    scalpedData = writeURLData()
    model = TextGenerationModel.from_pretrained("text-bison@001")
    while True:
        #question = input("Ask a question about the context, or press 1 to exit: ")
        if question == "1":
            break
        response = model.predict(
            str(scalpedData) + " Q: " + question,
            **parameters)
    print(f"Response from Model: {response.text}")
    return response.text