"""
Description:
This project is an individual study of how to use FastAPI and Docker. 
The objective of the project is to be a site to put cooking recipes that I adore!

Author:
Victória Finzi

Version:
1.0
"""
from fastapi import FastAPI, APIRouter
from recipes import Recipes #entender pq deu errado

# Instantiate a FastAPI app object that provides all the functionality for the API
app = FastAPI(titles="Recipe API", openapi_url="/openapi.json")

# Instantiate a router object that will be used to add routes to the API (endpoints)
api_router = APIRouter()

#Defined a basic get endpoint for our API
@api_router.get("/", status_code=200)
def root() -> dict:
    """
    This function returns the root of the API.
    """
    return {"message": "Welcome to the Recipe API!"}

#fetching data by ID from the database and returning it as a JSON object
@api_router.get("/recipe/{recipe_id}", status_code=200)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    This function returns a recipe based on the recipe_id.
    """
    result = [recipe for recipe in Recipes if recipe["id"] == recipe_id]
    if result: #entender pq do if
        return result[0]

@api_router.get("/search/", status_code=200)
def search_recipe(*, q: str) -> dict:

# Add the router object to the app object
    app.include_router(api_router)
