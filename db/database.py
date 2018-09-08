import sqlite3


def create_database(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    create_user_table = '{}{}{}{}{}{}{}'.format(
        ' CREATE TABLE IF NOT EXISTS',
        ' user(id INTEGER PRIMARY KEY,',
        ' name text NOT NULL,',
        ' address text,',
        ' email text,',
        ' bio text,',
        ' username text NOT NULL,'
        ' password text NOT NULL);'
    )

    cursor.execute(create_user_table)

    cursor.execute('INSERT OR REPLACE INTO user VALUES(1,"Neeraj Bansal", "Chandigarh Area", "bansal.neeraj94@gmail.com", "Full Stack Developer, AI is love", "neeraj_bansal", "demo");')


    create_notification_table = '{}{}{}{}{}{}{}{}'.format(
        ' CREATE TABLE IF NOT EXISTS',
        ' notification(id INTEGER PRIMARY KEY,',
        ' user_id INTEGER NOT NULL REFERENCES user(id),',
        ' type_id INTEGER NOT NULL,',
        ' msg text NOT NULL,',
        ' active boolean NOT NULL,',
        ' cancel_event_handler text NOT NULL,',
        ' see_more_handler text NOT NULL);'
    )

    cursor.execute(create_notification_table)
    connection.commit()
    connection.close()

    print('Database successfully created and populated with data!')
