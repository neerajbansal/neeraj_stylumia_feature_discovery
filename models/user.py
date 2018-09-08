import sqlite3


class UserModel:
    def __init__(self, id, name, address, email, bio, username, password):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.bio = bio
        self.username = username
        self.password = password

    @classmethod
    def find_by_name(cls, name, db_path='./db/datashop.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM user WHERE username=?;'
        result = cursor.execute(query, (name,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                user = UserModel(row[0], row[1], row[2],
                                 row[3], row[4], row[5], row[6])
            connection.close()
            return user

    @classmethod
    def find_by_id(cls, id, db_path='./db/datashop.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM user WHERE id=?'
        result = cursor.execute(query, (id,))
        rows = result.fetchall()
        if rows:
            return True

    def json(self):
        return {"id": self.id,
                "name": self.name,
                "address": self.address,
                "email": self.email,
                "bio": self.bio}
