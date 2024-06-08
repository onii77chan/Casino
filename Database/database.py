"""Признаться я пока не уверен стоит ли создавать бд оставлю это на потом
но даже если я и буду создавать бд то знаю что буду делать на базе ORM(SQLAlchemy)
пока что просто установлю библиотеку но не факт что до этого дойдёт"""

from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://my_user:tilek005@localhost:5432/test_db", echo=True)

with engine.connect() as connection:
    result = connection.execute(text("select 'hello world'"))
    for row in result:
        print(row)
