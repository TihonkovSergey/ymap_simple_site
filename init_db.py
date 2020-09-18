import sqlite3
from flask import json

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO marks (geometry, properties) VALUES (?, ?)",
            (json.dumps({"type": "Point", "coordinates": [59.874901, 29.827274]}),
             json.dumps({"balloonContentHeader": "<font size=3><b>12шка</b></font>",
                         "balloonContentBody": "<p>Здесь я живу</p>",
                         "balloonContentFooter": "<font size=1>Чтобы удалить метку щелкните по ней колесиком</font>",
                         "clusterCaption": "12",
                         "hintContent": "12"}))
            )

cur.execute("INSERT INTO marks (geometry, properties) VALUES (?, ?)",
            (json.dumps({"type": "Point", "coordinates": [59.874232, 29.830302]}),
             json.dumps({"balloonContentHeader": "<font size=3><b>15шка</b></font>",
                         "balloonContentBody": "<p><strong>Реклама кинопарапета</strong></p>",
                         "balloonContentFooter": "<font size=1>Чтобы удалить метку щелкните по ней колесиком</font>",
                         "clusterCaption": "15",
                         "hintContent": "15"}))
            )

cur.execute("INSERT INTO marks (geometry, properties) VALUES (?, ?)",
            (json.dumps({"type": "Point", "coordinates": [59.874855, 29.830275]}),
             json.dumps({"balloonContentHeader": "<font size=3><b>14ка</b></font>",
                         "balloonContentBody": "<p>Здесь я жил</p>",
                         "balloonContentFooter": "<font size=1>Чтобы удалить метку щелкните по ней колесиком</font>",
                         "clusterCaption": "14",
                         "hintContent": "14"}))
            )

cur.execute("INSERT INTO marks (geometry, properties) VALUES (?, ?)",
            (json.dumps({"type": "Point", "coordinates": [59.873236, 29.829472]}),
             json.dumps({"balloonContentHeader": "<font size=3><b>Короткий путь</b></font>",
                         "balloonContentBody": "<p>Чтобы быстро добраться в Ленту</p>" +
                                               "<p>перелезайте через забор здесь.</p>",
                         "balloonContentFooter": "<font size=1>Чтобы удалить метку щелкните по ней колесиком</font>",
                         "clusterCaption": "Путь",
                         "hintContent": "Короткий путь"}))
            )

connection.commit()
connection.close()
