# fast-api-template
A boilerplate to create api with Python FastAPI framework
Includes:
- Dockerfile
- Settings with dynaconf and dotenv
- Vertical Slice Architecture folder structure
- Basic AuthZ
- Basic liveness and readiness endpoints
- Sample customers endpoint

Created with FASTAPI
https://fastapi.tiangolo.com/

## Local Dev

### Activate venv
.\.venv\Scripts\Activate.ps1

### Restore deps
pip install -r requirements.txt

### Run locally for dev
uvicorn app.main:app --reload

### Run tests
pytest

### Linter
pylint app --errors-only

## Production

### Run for PROD
uvicorn app.main:app

## Build docker image
docker build -t <image-name> .

## Run docker
docker run -d --name <container-name> -p 5001:5000 <image-name>


