from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain
from quiz_module import generate_quiz
from summary_module import summarize
from learning_path import recommend_learning_path


# --------------------------------------------------
# Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


# --------------------------------------------------
# Static files
# --------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# --------------------------------------------------
# HTML templates
# --------------------------------------------------

templates = Jinja2Templates(
    directory="templates"
)


# --------------------------------------------------
# Request Models
# --------------------------------------------------

class TextRequest(BaseModel):
    text: str


class QuizRequest(BaseModel):
    topic: str
    num_questions: int = 5


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "message": "EduGenie is running"
    }


# --------------------------------------------------
# Question & Answer
# --------------------------------------------------

@app.post("/qa")
async def qa(data: TextRequest):

    try:
        answer = answer_question(data.text)

        return {
            "success": True,
            "answer": answer
        }

    except Exception as e:

        return {
            "success": False,
            "answer": "AI service is temporarily unavailable. Please try again.",
            "error": str(e)
        }


# --------------------------------------------------
# Concept Explanation
# --------------------------------------------------

@app.post("/explain")
async def explain_topic(data: TextRequest):

    try:
        explanation = explain(data.text)

        return {
            "success": True,
            "explanation": explanation
        }

    except Exception as e:

        return {
            "success": False,
            "explanation": "AI service is temporarily unavailable. Please try again.",
            "error": str(e)
        }


# --------------------------------------------------
# Quiz Generation
# --------------------------------------------------

@app.post("/quiz")
async def quiz(data: QuizRequest):

    try:
        result = generate_quiz(
            data.topic,
            data.num_questions
        )

        return {
            "success": True,
            "quiz": result
        }

    except Exception as e:

        return {
            "success": False,
            "quiz": "AI service is temporarily unavailable. Please try again.",
            "error": str(e)
        }


# --------------------------------------------------
# Summary
# --------------------------------------------------

@app.post("/summary")
async def summary(data: TextRequest):

    try:
        result = summarize(data.text)

        return {
            "success": True,
            "summary": result
        }

    except Exception as e:

        return {
            "success": False,
            "summary": "AI service is temporarily unavailable. Please try again.",
            "error": str(e)
        }


# --------------------------------------------------
# Learning Path
# --------------------------------------------------

@app.post("/learning-path")
async def learning_path(data: TextRequest):

    try:
        result = recommend_learning_path(data.text)

        return {
            "success": True,
            "learning_path": result
        }

    except Exception as e:

        return {
            "success": False,
            "learning_path": "AI service is temporarily unavailable. Please try again.",
            "error": str(e)
        }


# --------------------------------------------------
# Run using:
# python -m uvicorn main:app --reload
# --------------------------------------------------