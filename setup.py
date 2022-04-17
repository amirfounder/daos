from setuptools import setup, find_packages

setup(
    name='daos',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'SQLAlchemy==1.4.35',
        'psycopg2==2.9.3'
    ]
)
