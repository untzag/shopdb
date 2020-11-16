from fastapi import FastAPI

app = FastAPI()


@app.get("/part")
def get_parts():
    pass
