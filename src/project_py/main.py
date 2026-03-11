from fastapi import FastAPI


app = FastAPI(title="project-py")


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
