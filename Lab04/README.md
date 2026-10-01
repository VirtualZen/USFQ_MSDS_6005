# Lab04: NHL API

## Create the project environment

Use one virtual environment for this folder. Python 3.14 is supported by the
scikit-learn version required for the saved model.

```bash
uv venv --python 3.14 .venv
source .venv/bin/activate
uv pip install -r requirements-notebook.txt
```

In VS Code, select `.venv/bin/python` as the notebook kernel, then run the
notebook from top to bottom. The notebook scrapes the NHL data and writes
`equipos.csv`, `equipos.parquet`, and `modelos/modelo.joblib`.

## Run the API in Docker

From this folder:

```bash
docker build -t nhl-api .
docker run --rm -p 8000:8000 nhl-api
```

Open <http://localhost:8000/docs> and try `/predecir?gf=300&ga=250`. The current
Dockerfile copies `modelos/` into the image, so this Docker build does not need
a host volume. For a local Python run instead, activate `.venv` and run:

```bash
uvicorn servir:app --reload
```
