from decouple import config

from fastapi import FastAPI, Depends, HTTPException, status
#middleware is intended to process any request through a path and every response before returning it.
from fastapi.middleware.cors import CORSMiddleware

#has something to do with viewing the documentation
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from backend.routes import router as 
