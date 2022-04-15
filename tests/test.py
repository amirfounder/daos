from sqlalchemy import Integer, Column, String

from pgsql_repository import Entity, Repository


class Car(Entity):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class CarRepository(Repository[Car]):
    def __init__(self):
        super().__init__(Car, 'postgresql://postgres:root@localhost:5432/postgres')


def test():
    r = CarRepository()
    c = Car()
    c.name = '12'
    r.create(c)

    car = r.get_all(1)
    print(car)
