from sqlalchemy import Column, String, select

from daos.base.database import BaseDatabaseModel, BaseDatabaseDao
from daos.base.database.extensions.factory.factory import BaseModelFactory

CONN_STRING = 'postgresql://postgres:root@localhost:5432/postgres'


class Car(BaseDatabaseModel):
    __tablename__ = "cars"

    name = Column(String)
    model = Column(String)
    make = Column(String)


class CarRepository(BaseDatabaseDao):
    def __init__(self):
        super().__init__(CONN_STRING, Car)

    def get_count(self):
        with self.session_builder.open() as session:
            return session.execute(select(self.model).count())


class CarFactory(BaseModelFactory):
    pass


car_factory = CarFactory(Car)
car_repository = CarRepository()


def test_creates():
    cars = car_factory.create_many(25)
    car_repository.create(cars[0])
    car_repository.create_in_batch(cars[1:])


def test_puts():
    existing_car = car_repository.get_by_id(1)
    new_car = car_factory.create()
    new_car.id = existing_car.id

    car_repository.update(new_car)
    updated_car = car_repository.get_by_id(1)

    for k, v in updated_car.dict().items():
        assert getattr(new_car, k) == v


def test_deletes():
    pass


def test_gets():
    car = car_repository.get_by_id(1)
    assert car.id == 1

    cars = car_repository.get_by_id_in_batch([1,2,3,4,5])
    assert len(cars) == 5
    car_ids = [c.id for c in cars]
    assert 1 in car_ids
    assert 2 in car_ids
    assert 3 in car_ids
    assert 4 in car_ids
    assert 5 in car_ids

    cars = car_repository.get_all()
    assert len(cars) > 0
