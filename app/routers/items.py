from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from app.models import Query
from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
import chromadb
from tika import parser

router = APIRouter()
chroma_client = chromadb.PersistentClient(path="./chromadb")

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/pdf")
async def add_pdf(pdf_file: UploadFile = File(...)):
    raw = parser.from_buffer(pdf_file.file.read())
    collection = chroma_client.get_or_create_collection(name="test") # Get a collection object from an existing collection, by name. If it doesn't exist, create it.
    collection.add(documents=[raw['content']], ids=[pdf_file.filename])
    
    with open(f"files/{pdf_file.filename}", "wb") as file_object:
        file_object.write(pdf_file.file.read())

    return {"added": pdf_file.filename}

@router.post("/search")
async def search_pdf(query: Query):
    collection = chroma_client.get_collection(name="test")

    results = collection.query(
        query_texts=[query.query],
        n_results=query.neighbours
    )

    return {"results": results}