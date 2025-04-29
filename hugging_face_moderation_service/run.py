# hugging_face_moderation_service/run.py
# script to run the FastAPI application

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",  # Path to your FastAPI app
        host="127.0.0.1",
        port=8001,
        reload=True,
    )
