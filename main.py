from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import json
import pdfManager as pdfManager
import jsonManager as jsonManager

app = FastAPI()
pdfM = pdfManager.PdfManager()
jsonM = jsonManager.JsonManager()

# CORSを回避するために追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   
    allow_methods=["*"],      
    allow_headers=["*"]       
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/json")
async def read_sheet():
  pdfM.get_pdf_from_web()
  json = jsonM.new_json()
  return json