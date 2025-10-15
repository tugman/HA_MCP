# Build Docker Image
FROM python:3.11.2

ADD main.py .



RUN pip install "mcp[cli]" httpx requests "pydantic-ai[logfire]" "fastapi[standard]" 

CMD [“python”, “./main.py”] 

