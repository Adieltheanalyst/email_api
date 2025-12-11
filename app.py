from fastapi import FastAPI
from pydantic import BaseModel
from email_service import get_email


app=FastAPI(
    title="Email Scraper API",
    description= "API that logs in and retrieves the latest email message.",
    version="1.0.0"
)

class EmailRequest(BaseModel):
    username:str
    password:str

@app.post("/get-email")
def fetch_email(data: EmailRequest):
    try:
        message=get_email(data.username, data.password)
        return {"status":"success", "email_content": message}
    
    except Exception as e:
        return {"status":"error", "message":str(e)}
    