import os
from dotenv import load_dotenv
import openai
import json

from django.shortcuts import render
from django.http.response import StreamingHttpResponse

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.proxyapi.ru/openai/v1",
)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def chat_page(request):
    return render(request, 'chat_page.html')


def generate_response(question):
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield (chunk.choices[0].delta.content)


def answer(request):
    data = json.loads(request.body)
    message = data["message"]
    response = StreamingHttpResponse(generate_response(message), status=200,
                                     content_type="text/plain")
    return response
