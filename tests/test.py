from sqlalchemy import Integer, Column, String

from pgsql_repository import Entity, Repository


CONN_STRING = 'postgresql://postgres:root@localhost:5432/postgres'


class Car(Entity):
    __tablename__ = "cars"

    name = Column(String)


class CarRepository(Repository[Car]):
    def __init__(self):
        super().__init__(CONN_STRING, Car)


def test():
    r = CarRepository()
    r.create(Car())

    cars = r.get_all()
    print(cars)
