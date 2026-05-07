from fastapi import FastAPI

app=FastAPI(
    title="DubaiNest AI",
    description="Intelligent Dubai Real Estate Platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message":"DubaiNest AI is running"}

@app.get("/health")
def health_check():
    return {"status":"healthy"}