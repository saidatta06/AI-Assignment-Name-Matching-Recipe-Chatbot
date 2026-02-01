# AI-Assignment-Name-Matching-Recipe-Chatbot

AI Assignment – Name Matching & Recipe Chatbot
----------------------------------------------------
Overview

This project contains two AI tasks:

Task 1 – Name Matching System
Finds the most similar person names from a dataset using string similarity.

Task 2 – Local Recipe Chatbot
A locally running AI chatbot that suggests recipes based on user-provided ingredients, exposed through a FastAPI server and accessible via CLI.

The entire project runs locally on Windows/Linux, without requiring cloud services or GPUs.
------------------------------------------------------
Technologies Used

Python 3.9+

FastAPI

Uvicorn

RapidFuzz (string similarity)

Requests (CLI chatbot)
-------------------------------------------------------
Project Structure
ai_assignment/
│
├── task1_name_matching/
│   ├── name_matcher.py
│   └── names.py
│
├── task2_local_llm_chatbot/
│   ├── app.py
│   ├── model.py
│   ├── recipes.json
│   └── cli_chatbot.py
│
├── requirements.txt
└── README.md
--------------------------------------------------------
TASK 1: Name Matching System

Objective

Given a user-entered name, find the closest matching names from a dataset using similarity scores.

How to Run Task 1
Step 1: Open Terminal

Navigate to project root:

cd ai_assignment

Step 2: Run the Program
python task1_name_matching/name_matcher.py

Sample Input
Enter name: Geeta

 Sample Output
{
  "best_match": {
    "name": "Geeta",
    "score": 91
  },
  "other_matches": [
    {"name": "Geeta", "score": 91},
    {"name": "Gita", "score": 88},
    {"name": "Geetha", "score": 85}
  ]
}
------------------------------------------------------
TASK 2: Local Recipe Chatbot

Objective

Build a local AI chatbot that:

Accepts ingredients as input

Suggests a suitable recipe

Runs using a local server

Communicates via JSON API

Includes a chatbot UI (CLI)

Setup Instructions
Step 1: Install Python

Ensure Python 3.9 or higher is installed:

python --version

Installation Commands

Install required dependencies:

pip install -r requirements.txt

How to Run Task 2

1️ Start the FastAPI Server
cd task2_local_llm_chatbot
uvicorn app:app --reload


Server will run at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

2️ Run the CLI Chatbot (New Terminal)
cd task2_local_llm_chatbot
python cli_chatbot.py

Sample CLI Interaction
Input
You: Egg, Onion

Output
Bot: Suggested Recipe → Egg Omelette with Onions

Another Example
You: Potato, Onion
Bot: Suggested Recipe → Aloo Onion Fry

API Sample (Verification)
Endpoint
POST /chat

Request Body
{
  "ingredients": ["Egg", "Onion"]
}

Response
{
  "ingredients": ["Egg", "Onion"],
  "suggested_recipe": "Egg Omelette with Onions"
}
-------------------------------------------------------
Features Summary

Fully local execution

Lightweight AI model

Custom recipe dataset

FastAPI backend

JSON-based API

CLI chatbot interface

Works on Windows & Linux
--------------------------------------------------
Notes

The system uses a custom recipe dataset (recipes.json) to simulate fine-tuned AI behavior.

The architecture is modular and can be extended to real LLMs (LLaMA, Mistral) if required.
