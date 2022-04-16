import datetime

from sqlalchemy import Column, String

from pgsql_repository import BaseModel, BaseModelRepository
from pgsql_repository.factory.random_model_factory import BaseRandomModelFactory

CONN_STRING = 'postgresql://postgres:root@localhost:5432/postgres'


class Car(BaseModel):
    __tablename__ = "cars"

    model = Column(String)


class CarRepository(BaseModelRepository):
    def __init__(self):
        super().__init__(CONN_STRING, Car)


class CarFactory(BaseRandomModelFactory):
    pass


car_factory = CarFactory(Car)
car_repository = CarRepository()


def test_creates():
    cars = car_factory.create_many(25)
    car_repository.create(cars[0])
    car_repository.create_in_batch(cars[1:])


def test_gets():
    car_repository.create(Car())

    cars = car_repository.get_all()
    print(cars)
