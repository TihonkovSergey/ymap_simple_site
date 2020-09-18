import sqlite3
import os
from flask import Flask, render_template, request, url_for, flash, redirect, json
from werkzeug.exceptions import abort
from dbhelper import DBHelper


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ajhskcFSDFygAFDSyfFcDAiuyegiya'
DBNAME = 'database.db'


def delete_mark(mark_id):
    db = DBHelper(DBNAME)
    db.delete_mark(mark_id)


def get_marks():
    db = DBHelper(DBNAME)
    row_mark_list = db.get_all_marks()
    marks = {
        "type": "FeatureCollection",
        "features": [{"type": "Feature",
                      "id": mark['id'],
                      "geometry": json.loads(mark['geometry']),
                      "properties": json.loads(mark['properties'])
                      } for mark in row_mark_list]
    }
    return json.dumps(marks)


def insert_mark(coords, body, title):
    geometry = json.dumps({"type": "Point", "coordinates": coords})
    properties = json.dumps({
        "balloonContentHeader": f"<font size=3><b>{title}</b></font>",
        "balloonContentBody": f"<p>{body}</p>",
        "balloonContentFooter": "<font size=1>Чтобы удалить метку щелкните по ней колесиком</font>",
        "clusterCaption": f"{title[:10]}...",
        "hintContent": f"{title[:10]}..."
        })
    db = DBHelper(DBNAME)
    db.insert_mark(geometry, properties)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        data = json.loads(request.form['javascript_data'])
        if data['event'] == 'add':
            coords = [float(c) for c in data['coords'].split(' ')]
            body_text = data['body']
            title_text = data['title']
            insert_mark(coords, body_text, title_text)
        elif data['event'] == 'delete':
            delete_mark(data['id'])

    return render_template('index.html', marks=get_marks())
