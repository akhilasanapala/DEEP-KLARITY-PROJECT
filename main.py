from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}


@app.post("/extract-recipe")
def extract_recipe(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    
    title = soup.title.string if soup.title else "No title found"

    ingredients = []
    for item in soup.find_all(["li", "span"]):
        text = item.get_text().strip()
        if any(word in text.lower() for word in ["cup", "tsp", "tbsp", "kg", "g"]):
            ingredients.append(text)

    
    instructions = []
    for step in soup.find_all(["p", "li"]):
        text = step.get_text().strip()
        if len(text) > 50:  # filter meaningful steps
            instructions.append(text)

    return {
        "title": title,
        "ingredients": ingredients[:10],
        "instructions": instructions[:5]
    }