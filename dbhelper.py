from flask import json
from pprint import pprint
import sqlite3


class DBHelper:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row

    def insert_mark(self, geometry, properties):
        self.conn.execute("INSERT INTO marks (geometry, properties) VALUES (?, ?)",
                          (geometry, properties))
        self.conn.commit()

    def get_all_marks(self):
        return self.conn.execute('SELECT * FROM marks ').fetchall()

    def get_mark(self, mark_id):
        return self.conn.execute('SELECT * FROM marks WHERE id= ?', (mark_id,)).fetchone()

    def update_mark(self, mark_id, geometry, properties):
        self.conn.execute('UPDATE marks SET geometry = ?, properties = ?'
                          ' WHERE id = ?',
                          (geometry, properties, mark_id))
        self.conn.commit()

    def delete_mark(self, mark_id):
        try:
            self.conn.execute('DELETE FROM marks WHERE id = ?', (mark_id,))
            self.conn.commit()
        except e:
            return e


def get_marks():
    db = DBHelper('database.db')
    row_mark_list = db.get_all_marks()
    marks = {
        "type": "FeatureCollection",
        "features": [{"type": "Feature",
                      "id": mark['id'],
                      "geometry": json.loads(mark['geometry']),
                      "properties": json.loads(mark['properties'])
                      } for mark in row_mark_list]
    }
    return marks


if __name__ == '__main__':
    pass
