# Code Review Agent

A GitHub App that automatically reviews Pull Requests using
static analysis and an LLM.

Status: work in progress (Day 1 - project skeleton).

## Run locally

```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://localhost:8000/health
