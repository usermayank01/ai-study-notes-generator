from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from typing import List
import os
import shutil

from app.pdf_processor import process_pdf
from app.vector_store import create_vector_store
from app.ai_generator import (
    ask_question,
    generate_summary,
    generate_revision_notes,
    generate_quiz,
    generate_key_points
)


app = FastAPI(title="AI Study Notes Generator")


@app.post("/upload")
async def upload_documents(
    files: List[UploadFile] = File(...)
):

    os.makedirs("data/uploads", exist_ok=True)

    all_chunks = []

    uploaded_files = []

    for file in files:

        file_path = os.path.join(
            "data/uploads",
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        chunks = process_pdf(file_path)

        all_chunks.extend(chunks)

        uploaded_files.append(file.filename)

    create_vector_store(all_chunks)

    return {
        "message": "Documents processed successfully!",
        "files": uploaded_files,
        "chunks": len(all_chunks)
    }


@app.post("/ask")
async def ask(request: dict):

    question = request.get("question", "")

    return {
        "answer": ask_question(question)
    }


@app.get("/summary")
def summary():

    return {
        "answer": generate_summary()
    }


@app.get("/revision")
def revision():

    return {
        "answer": generate_revision_notes()
    }


@app.get("/quiz")
def quiz():

    return {
        "answer": generate_quiz()
    }


@app.get("/key-points")
def key_points():

    return {
        "answer": generate_key_points()
    }


app.mount(
    "/",
    StaticFiles(
        directory="frontend",
        html=True
    ),
    name="frontend"
)