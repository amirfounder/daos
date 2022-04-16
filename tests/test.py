import datetime

from sqlalchemy import Column, String

from pgsql_repository import Entity, Repository
from pgsql_repository.factory.factory import Factory

CONN_STRING = 'postgresql://postgres:root@localhost:5432/postgres'


class Car(Entity):
    __tablename__ = "cars"

    model = Column(String)


class CarRepository(Repository[Car]):
    def __init__(self):
        super().__init__(CONN_STRING, Car)


class CarFactory(Factory[Car]):
    pass


car_factory = CarFactory()
car_repository = CarRepository()


def test_creates():
    cars = car_factory.create_many(25)
    car_repository.create(cars[0])
    car_repository.create_in_batch(cars[1:])


def test_gets():
    car_repository.create(Car())

    cars = car_repository.get_all()
    print(cars)
