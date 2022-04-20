from peewee import TextField
from sqlalchemy import Column, String

from daos.abstracts.database import BaseDBModel, BaseDBRepository

CONN_STRING = 'postgresql://postgres:root@localhost:5432/postgres'


class Car(BaseDBModel):
    __tablename__ = 'cars'

    name = Column(String)
    model = Column(String)
    make = Column(String)


class CarRepository(BaseDBRepository[Car]):
    def __init__(self):
        super().__init__(Car)


car_repository = CarRepository()


def test_creates():
    cars = [Car(name='lol')]
    car_repository.save(cars[0])


def test_puts():
    new_car = Car()
    existing_car = car_repository.get(1)
    new_car.id = existing_car.id

    car_repository.update(new_car)
    updated_car = car_repository.get(1)

    for k, v in updated_car.dict().items():
        assert getattr(new_car, k) == v


def test_deletes():
    pass


def test_gets():
    car = car_repository.get(1)
    assert car.id == 1

    cars = car_repository.get_all()
    assert len(cars) > 0
