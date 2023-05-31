from fastapi import FastAPI
from datetime import datetime
from db.database import db_context
from db.models import Base, Person
from db.database import engine
from sqlalchemy import update
import json
Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/result")
async def get_Person(id: str):
    with db_context() as s:
        t = s.query(Person).filter(Person.id == id).first()
    return t.Interest[1]

@app.get("/upload")
async def run_upload(input_a: str, input_b: str):
    with db_context() as s:
        t = Person(name=input_a, intro=input_b)
        s.add(t)
        s.commit()
        s.refresh(t)
    return t.id

@app.get("/upload_interest")
async def run_upload_interest(id: str, input_a: str, input_b: str):
    with db_context() as s:
        t =  s.query(Person).filter(Person.id == id).first()
        if t.Interest is None:
            # t.Interest = [input_a, input_b]
            t.Interest = json.dumps([input_a, input_b],  ensure_ascii=False)
        else:
            #t.Interest += [input_a, input_b]
            t.Interest += json.dumps([input_a, input_b],  ensure_ascii=False)
            setattr(t, 'Interest', t.Interest)
        s.commit()
        s.refresh(t)
        #I = json.load(t.Interest)
        #I.append([input_a, input_b]))
    return t.Interest

@app.get("/upload_qual")
async def run_upload_qual(id: str, input_a: str, input_b: str):
    with db_context() as s:
        t = Person(id = id, Qual=json.dump([input_a, input_b]))
        s.add(t)
        s.commit()
        s.refresh(t)
    return t

@app.get("/upload_major")
async def run_upload_major(id: str, input_a: str, input_b: str):
    with db_context() as s:
        t = Person(id = id,Major=json.dump([input_a, input_b]))
        s.add(t)
        s.commit()
        s.refresh(t)
    return t

@app.get("/upload_competition")
async def run_upload_competition(id: str, input_a: str, input_b: str):
    with db_context() as s:
        t = Person(id = id, Competition=json.dump([input_a, input_b]))
        s.add(t)
        s.commit()
        s.refresh(t)
    return t