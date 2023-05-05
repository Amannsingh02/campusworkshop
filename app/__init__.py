"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chabd2rhp8u791h58cb0-a.oregon-postgres.render.com",
        database="postgresql_al8i",
        user="postgresql_al8i_user",
        password="Bjh8CZEB8zfHp84hrelaCeT9vTpPVgqj")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
