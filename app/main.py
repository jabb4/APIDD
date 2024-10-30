from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/test_get")
async def test1():
    return {"GET": "Test"}

@app.post("/test_post")
async def test2(request: Request):
    # Access request json data
    if request.headers.get("Content-Type") == "application/json":
        json_data = await request.json()  # Parses JSON body
        print(json_data)
    
    # Access headers
    print(request.headers)
    user_agent = request.headers.get('user-agent')
    return {
        "user_agent": user_agent
    }