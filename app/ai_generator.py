from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama

from app.prompts import (
    SUMMARY_PROMPT,
    REVISION_PROMPT,
    QUIZ_PROMPT,
    KEY_POINTS_PROMPT,
    QUESTION_PROMPT
)


# =========================
# LOCAL EMBEDDINGS
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================
# LOCAL LLM
# =========================

llm = ChatOllama(
    model="llama3.2"
)


# =========================
# RETRIEVE DOCUMENT CONTEXT
# =========================

def get_context(query, k=8):

    vector_store = FAISS.load_local(
        "data/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    results = vector_store.similarity_search(
        query,
        k=k
    )

    context_parts = []

    for document in results:
        source = document.metadata.get("source", "Unknown source")
        page = document.metadata.get("page")

        if page is not None:
            source_info = f"Source: {source}, Page: {page + 1}"
        else:
            source_info = f"Source: {source}"

        context_parts.append(
            f"{source_info}\n{document.page_content}"
        )

    return "\n\n".join(context_parts)


# =========================
# ASK QUESTION
# =========================

def ask_question(question):

    context = get_context(
        question,
        k=5
    )

    prompt = QUESTION_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content


# =========================
# SUMMARY
# =========================

def generate_summary():

    context = get_context(
        "main topics important concepts definitions course content",
        k=10
    )

    prompt = SUMMARY_PROMPT.format(
        context=context
    )

    response = llm.invoke(prompt)

    return response.content


# =========================
# REVISION NOTES
# =========================

def generate_revision_notes():

    context = get_context(
        "important topics exam revision key concepts definitions",
        k=10
    )

    prompt = REVISION_PROMPT.format(
        context=context
    )

    response = llm.invoke(prompt)

    return response.content


# =========================
# QUIZ
# =========================

def generate_quiz():

    context = get_context(
        "important concepts topics facts questions",
        k=10
    )

    prompt = QUIZ_PROMPT.format(
        context=context
    )

    response = llm.invoke(prompt)

    return response.content


# =========================
# KEY POINTS
# =========================

def generate_key_points():

    context = get_context(
        "key points important concepts definitions facts",
        k=10
    )

    prompt = KEY_POINTS_PROMPT.format(
        context=context
    )

    response = llm.invoke(prompt)

    return response.content