from fastapi import FastAPI, HTTPException, Response, Cookie, Depends, status, Request
from pydantic import BaseModel
import sqlite3
import requests

app = FastAPI()

class Item_tracks(BaseModel):
    page:int
    per_page:int



class CustomerStat(BaseModel):
	CustomerId: int = None
	Email: str = None
	Phone: str = None
	Sum: float = None

class GenresStat(BaseModel):
	Name: str = None
	Sum: int = None

class Category404(BaseModel):
	detail: Error = Error(error="No such Category")



@app.get("/sales")
async def db_task_5(category: str=None):
	if category == "customers":
		cursor = app.db_connection.cursor()
		data = cursor.execute("""
			SELECT CustomerId, Email, Phone, SUM(Total) as Sum FROM(
			SELECT * FROM invoices  
			JOIN customers ON customers.CustomerId = invoices.CustomerId
			)GROUP BY CustomerId ORDER BY Sum DESC, CustomerId ASC
			""").fetchall()
		content = []
		for i in data:
			content.append(CustomerStat(
				CustomerId = i[0],
				Email = i[1],
				Phone = i[2],
				Sum = round(i[3],2)
				))
		return content
	elif category == "genres":
		cursor = app.db_connection.cursor()
		data = cursor.execute("""
			SELECT Name, COUNT(GenreId) AS SUM FROM (
			SELECT * FROM genres 
			JOIN tracks ON tracks.GenreId = genres.GenreId
			JOIN invoice_items ON invoice_items.TrackId = tracks.TrackId
			)GROUP BY GenreId ORDER BY Sum DESC, Name ASC
			""").fetchall()
		content = []
		for i in data:
			content.append(GenresStat(
				Name = i[0],
				Sum = i[1],
				))
		return content
	else:
		return JSONResponse(status_code=404,content=jsonable_encoder(Category404()))