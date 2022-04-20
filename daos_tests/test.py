from peewee import TextField

from daos.abstracts.database import BaseDBModel, BaseDBRepository

CONN_STRING = 'postgresql://postgres:root@localhost:5432/postgres'


class Car(BaseDBModel):
    name = TextField()
    model = TextField()
    make = TextField()

    class Meta:
        table_name = 'cars'


class CarRepository(BaseDBRepository[Car]):
    def __init__(self):
        super().__init__(Car)


car_repository = CarRepository()


def test_creates():
    cars = [Car.create(name='lol')]
    car_repository.save(cars[0])


def test_puts():
    existing_car = car_repository.get(1)
    nebw_car.id = existing_car.id

    car_repository.update(new_car)
    updated_car = car_repository.get(1)

    for k, v in updated_car.dict().items():
        assert getattr(new_car, k) == v


def test_deletes():
    pass


def test_gets():
    car = car_repository.get_by_id(1)
    assert car.id == 1

    cars = car_repository.get_by_id_in_batch([1, 2, 3, 4, 5])
    assert len(cars) == 5
    car_ids = [c.id for c in cars]
    assert 1 in car_ids
    assert 2 in car_ids
    assert 3 in car_ids
    assert 4 in car_ids
    assert 5 in car_ids

    cars = car_repository.get_all()
    assert len(cars) > 0
