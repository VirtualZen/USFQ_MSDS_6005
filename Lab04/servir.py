from pathlib import Path
import joblib
from fastapi import FastAPI

MODEL_PATH = Path(__file__).resolve().parent / "modelos" / "modelo.joblib"
modelo = joblib.load(MODEL_PATH)
app = FastAPI(title="Temporada ganadora")

@app.get("/predecir")
def predecir(gf: int, ga: int):
    x = [[gf, ga, gf - ga]]
    return {"ganadora": bool(modelo.predict(x)[0]),
            "probabilidad": round(float(modelo.predict_proba(x)[0][1]), 3)}