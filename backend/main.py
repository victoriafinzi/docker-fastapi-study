from decouple import config
import uvicorn
import logging

if __name__ == "__main__":
    # Use this for debugging purposes only
    uvicorn.run("backend:", host="0.0.0.0", port=3000, log_level="debug")