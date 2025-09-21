from datetime import date

from sqlalchemy import func, label, select
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.rooms.models import Rooms
from app.database import async_session_maker


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def get_rooms_by_hotel(
        cls,
        hotel_id: int,
        date_from: date,
        date_to: date,
    ):
        async with async_session_maker() as session:
            # Подзапрос для подсчета забронированных комнат
            subquery = (
                select(func.count(Bookings.id))
                .where(
                    (Bookings.room_id == Rooms.id)
                    & (Bookings.date_from <= date_to)
                    & (Bookings.date_to >= date_from)
                )
                .scalar_subquery()
            )

            # Основной запрос с правильными вычислениями
            query = select(
                label("total_cost", Rooms.price * (date_to - date_from).days),
                label("rooms_left", Rooms.quantity - subquery),
                Rooms.id,
                Rooms.quantity,
                Rooms.price,
                # Добавьте другие необходимые поля модели
            ).where(
                Rooms.hotel_id == hotel_id
            )  # Не забудьте про фильтр по отелю

            result = await session.execute(query)
            return result.mappings().all()
