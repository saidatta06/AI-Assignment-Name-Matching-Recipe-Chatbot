from fastapi import FastAPI
from model import suggest_recipe

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Recipe Chatbot API is running"}

@app.post("/chat")
def chat(data: dict):
    ingredients = data.get("ingredients", [])
    recipe = suggest_recipe(ingredients)

    return {
        "ingredients": ingredients,
        "suggested_recipe": recipe
    }
