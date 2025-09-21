from datetime import date
from fastapi import Query
from app.hotels.rooms.dao import RoomsDAO
from app.hotels.router import router


@router.get("/{hotel_id}/rooms")
async def get_rooms(
    hotel_id: int, 
    date_from: date = Query(..., description="Дата заезда"),
    date_to: date = Query(..., description="Дата выезда"),
):
    return await RoomsDAO.get_rooms_by_hotel(hotel_id, date_from, date_to)


# @router.get("/{hotel_id}/room id")
# async def get_room_id(room_id: int):
#     return await RoomsDAO.find_by_id(room_id)
