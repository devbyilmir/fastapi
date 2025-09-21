from fastapi import FastAPI, Query, Depends
from fastapi.staticfiles import StaticFiles
from typing import Optional
from datetime import date
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as route_hotels
from app.hotels.rooms.router import router as route_rooms

from app.pages.router import router as router_pages
from app.static.router import router as router_images


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(route_hotels)
app.include_router(route_rooms)
app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_pages)
app.include_router(router_images)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow_Origin",
        "Autorization",
    ],
)

# class HotelsSearchArgs:
#     def __init__(
#         self,
#         location: str,
#         date_from: date,
#         date_to: date,
#         has_spa: Optional[bool] = None,
#         stars: Optional[int] = Query(None, ge=1, le=5),
#     ):
#         self.location = location
#         self.date_from = date_from
#         self.date_to = date_to
#         self.has_spa = has_spa
#         self.stars = stars


# @app.get("/hotels/{hotel_id}")
# def get_hotels(search_args: HotelsSearchArgs = Depends()):
#     return search_args
