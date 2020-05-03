from fastapi import FastAPI, HTTPException, Response, Cookie, Depends, status, Request
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Item_tracks(BaseModel):
    page:int
    per_page:int



@app.get("/tracks")
def trucks(item:Item_tracks):
    with sqlite3.connect('chinook.db') as connection:
        first_element=item.per_page*item.page
        last_element=first_element+item.per_page
        cursor = connection.cursor()
        data = cursor.execute(
            f"SELECT trackid,name,albumid,mediatypeid, genreid, composer, milliseconds, bytes, unitprice FROM tracks WHERE trackid BETWEEN {first_element} AND {last_element}").fetchall()
        return data
    
@app.get("/tracks/test")
async def root():
    with sqlite3.connect('chinook.db') as connection:
        cursor = connection.cursor()
        tracks = cursor.execute("SELECT name FROM tracks").fetchall()
        return {
            "tracks": tracks,
            "tracks_counter": len(tracks)
        }