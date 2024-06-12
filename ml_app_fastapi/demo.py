from fastapi import FastAPI

app = FastAPI()

@app.get("/") # home page --> path operation decorator
async def root():
    return {"message":"Hello fastApi"}

@app.get('/demo')
def demo_func():
    return {"message":"This is a demo get operation"}

@app.post("/post_demo")
def post_func():
    return {"message":"This is a demo post operation"}