from fastapi import FastAPI
from datetime import datetime
from db.database import db_context
from db.models import Base, Person
from db.database import engine
from sqlalchemy import update
import json
import ast
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/result")
async def get_Person(id: str):
    with db_context() as s:
        t = s.query(Person).filter(Person.id == id).first()
    return t

@app.get("/upload")
async def run_upload(input_a: str, input_b: str):
    with db_context() as s:
        t = Person(name=input_a, intro=input_b)
        s.add(t)
        s.commit()
        s.refresh(t)
    return t

@app.get("/get_interest")
async def run_get_interest(id: str):
    with db_context() as s:
        t =  s.query(Person).filter(Person.id == id).first()
        if t.Interest is None:
           return []
        else:
            return ast.literal_eval(t.Interest)


@app.get("/upload_interest")
async def run_upload_interest(id: str, input_a: str, input_b: str):
    with db_context() as s:
        t =  s.query(Person).filter(Person.id == id).first()
        if t.Interest is None:
            Interests = []
            Interests.append([input_a, input_b])
            t.Interest = json.dumps(Interests, ensure_ascii=False)
        else:
            try:
                Interests = json.loads(t.Interest)
            except json.JSONDecodeError:
                Interests = []
            Interests.append([input_a, input_b])
            t.Interest = json.dumps(Interests, ensure_ascii=False)
        s.commit()
        s.refresh(t)
        t.Interest = json.loads(t.Interest)
    return t.Interest


@app.get("/delete_interest")
async def delete_interest(id: str, input_a: str):
    with db_context() as s:
        t = s.query(Person).filter(Person.id == id).first()
        if t is None:
            return {"message": "Data not found"}
        if t.Interest is None:
            return {"message": "Data does not have any Interestifications"}
        interests = ast.literal_eval(t.Interest)
        matching_data = [data for data in interests if data[0] == input_a]
        if not matching_data:
            return {"message": "No matching data found"}
        interests.remove(matching_data[0])
        t.Interest = json.dumps(interests, ensure_ascii=False)
        s.commit()
        s.refresh(t)
        t.Interest = json.loads(t.Interest)
    return t.Interest


@app.get("/delete_qual")
async def delete_qual(id: str, input_a: str):
    with db_context() as s:
        t = s.query(Person).filter(Person.id == id).first()
        if t is None:
            return {"message": "Data not found"}
        if t.Qual is None:
            return {"message": "Data does not have any qualifications"}
        quals = ast.literal_eval(t.Qual)
        matching_data = [data for data in quals if data[0] == input_a]
        if not matching_data:
            return {"message": "No matching data found"}
        quals.remove(matching_data[0])
        t.Qual = json.dumps(quals, ensure_ascii=False)
        s.commit()
        s.refresh(t)
        t.Qual = json.loads(t.Qual)
    return t.Qual


@app.get("/get_qual")
async def run_get_qual(id: str):
    with db_context() as s:
        t =  s.query(Person).filter(Person.id == id).first()
        if t.Qual is None:
           return []
        else:
            return ast.literal_eval(t.Qual)

@app.get("/upload_qual")
async def run_upload_qual(id: str, input_a: str, input_b: str):
    with db_context() as s:
        t =  s.query(Person).filter(Person.id == id).first()
        if t.Qual is None:
            quals = []
            quals.append([input_a, input_b])
            t.Qual = json.dumps(quals, ensure_ascii=False)
        else:
            try:
                quals = json.loads(t.Qual)
            except json.JSONDecodeError:
                quals = []
            quals.append([input_a, input_b])
            t.Qual = json.dumps(quals, ensure_ascii=False)
        s.commit()
        s.refresh(t)
        t.Qual = json.loads(t.Qual)
    return t.Qual


@app.get("/get_major")
async def run_get_major(id: str):
    with db_context() as s:
        t =  s.query(Person).filter(Person.id == id).first()
        if t.Major is None:
           return []
        else:
            return ast.literal_eval(t.Major)
            
@app.get("/upload_major")
async def run_upload_major(id: str, input_a: str, input_b: str):
    with db_context() as s:
        t =  s.query(Person).filter(Person.id == id).first()
        if t.Major is None:
            Majors = []
            Majors.append([input_a, input_b])
            t.Major = json.dumps(Majors, ensure_ascii=False)
        else:
            try:
                Majors = json.loads(t.Major)
            except json.JSONDecodeError:
                Majors = []
            Majors.append([input_a, input_b])
            t.Major = json.dumps(Majors, ensure_ascii=False)
        s.commit()
        s.refresh(t)
        t.Major = json.loads(t.Major)
    return t.Major

@app.get("/delete_major")
async def delete_major(id: str, input_a: str):
    with db_context() as s:
        t = s.query(Person).filter(Person.id == id).first()
        if t is None:
            return {"message": "Data not found"}

        if t.Major is None:
            return {"message": "Data does not have any interests"}

        majors = ast.literal_eval(t.Major)
        matching_data = [data for data in majors if data[0] == input_a]
        if not matching_data:
            return {"message": "No matching data found"}

        majors.remove(matching_data[0])
        t.Major = json.dumps(majors, ensure_ascii=False)
        s.commit()
        s.refresh(t)
        t.Major = json.loads(t.Major)
    return t.Major

@app.get("/get_competition")
async def run_get_competition(id: str):
    with db_context() as s:
        t =  s.query(Person).filter(Person.id == id).first()
        if t.Competition is None:
           return []
        else:
            return ast.literal_eval(t.Competition)
            
@app.get("/upload_competition")
async def run_upload_competition(id: str, input_a: str, input_b: str):
    with db_context() as s:
        t =  s.query(Person).filter(Person.id == id).first()
        if t.Competition is None:
            Competitions = []
            Competitions.append([input_a, input_b])
            t.Competition = json.dumps(Competitions, ensure_ascii=False)
        else:
            try:
                Competitions = json.loads(t.Competition)
            except json.JSONDecodeError:
                Competitions = []
            Competitions.append([input_a, input_b])
            t.Competition = json.dumps(Competitions, ensure_ascii=False)
        s.commit()
        s.refresh(t)
        t.Competition = json.loads(t.Competition)
    return t.Competition

@app.get("/delete_competition")
async def delete_competition(id: str, input_a: str):
    with db_context() as s:
        t = s.query(Person).filter(Person.id == id).first()
        if t is None:
            return {"message": "Data not found"}

        if t.Competition is None:
            return {"message": "Data does not have any interests"}

        competitions = ast.literal_eval(t.Competition)
        matching_data = [data for data in competitions if data[0] == input_a]
        if not matching_data:
            return {"message": "No matching data found"}

        competitions.remove(matching_data[0])
    
        t.Competition = json.dumps(competitions, ensure_ascii=False)
        s.commit()
        s.refresh(t)
        t.Competition = json.loads(t.Competition)
    return t.Competition

