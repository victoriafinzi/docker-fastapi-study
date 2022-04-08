from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Created some example recipe data in the recipe list of dictionaries.
Recipes = [
    {
        "id": 1,
        "title": "Spaghetti with Tomato Sauce",
        "ingredients": ["Spaghetti", "Tomato Sauce", "Cheese"],
        "steps": [
            "Boil water",
            "Cook pasta until done",
            "Drain",
            "While pasta is cooking, cook sauce",
            "Add pasta to sauce",
            "Cook until pasta is no longer pink",
            "Enjoy!"]
    },
    {
        "id": 2,
        "title": "Milkshake",
        "ingredients": ["Milk", "Ice cream", "Sugar"],
        "steps": [
            "Combine ingredients",
            "Stir",
            "Enjoy!"]
    }]