import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="ticket_arena",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

query = "CREATE OR REPLACE VIEW Temp_event AS\
    SELECT DISTINCT e.event_id\
    FROM Event AS e, Event_tag AS et\
    WHERE (e.event_id = et.event_id) AND (et.word IN ('Bon', 'coldplay'));"

select = "SELECT *\
    FROM Event, Temp_event\
    WHERE Event.event_id = Temp_event.event_id;"

with connection.cursor() as cursor:
    cursor.execute(query)
    cursor.execute(select)
    print(cursor.fetchall())
# except Exception as e:
#     print(e)
