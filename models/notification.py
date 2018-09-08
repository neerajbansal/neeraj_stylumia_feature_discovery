import sqlite3


class NotificationModel:

    def __init__(self, id, user_id, type_id, msg, active, see_more_handler):
        self.id = id
        self.user_id = user_id
        self.type_id = type_id
        self.msg = msg
        self.active = active
        self.see_more_handler = see_more_handler

    @classmethod
    def insert_new_user_notification(cls, user_id, type_id, msg, active, cancel_event_handler, see_more_handler, db_path='./db/datashop.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'INSERT INTO notification VALUES(NULL, ?, ?, ?, ?, ?, ?)'
        cursor.execute(query, (user_id, type_id, msg, active,
                               cancel_event_handler, see_more_handler))
        connection.commit()
        connection.close()

    @classmethod
    def find_all_user_notifications(cls, id,  db_path='./db/datashop.db'):
        print(id)
        notifications = list()
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM notification where user_id = ? AND active = 1;'
        result = cursor.execute(query, (id,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                print(row)
                notifications.append(NotificationModel(row[0], row[1], row[2],
                                                       row[3], row[4], row[6]))
            return notifications
        connection.close()

    @classmethod
    def delete_user_notification_by_id(self, id, db_path='./db/datashop.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        query = 'UPDATE notification SET active = 0 WHERE id = ?'
        result = cursor.execute(query, (id,))
        rows = result.fetchall()

        connection.commit()
        connection.close()

    def json(self):
        return {"id": self.id,
                "msg": self.msg,
                "see_more_handler": self.see_more_handler}
