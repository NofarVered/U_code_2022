SELECT_ALL_EVENTS = "SELECT *\
                      FROM Event\
                      ORDER BY date DESC\
                      LIMIT 5;"

SELECT_EVENTS_BY_CATEGORY = "SELECT *\
                            FROM Event\
                            WHERE category_id = (SELECT category_id\
                                                FROM Category\
                                                WHERE name = '{category_name}')\
                            ORDER BY date DESC;"

SELECT_EVENTS_BY_TAG = "SELECT *\
                        FROM Event\
                        WHERE event_id = (SELECT event_id\
                                            FROM event_tag\
                                            WHERE word = '{word}')\
                        ORDER BY date DESC;"

CREATE_VIEW_TEMP_EVENT = "CREATE OR REPLACE VIEW Temp_event AS\
    SELECT DISTINCT e.event_id\
    FROM Event AS e, Event_tag AS et\
    WHERE (e.event_id = et.event_id) AND (et.word IN ({tags}));"

DROP_VIEW_TEMP_EVENT = "DROP TABLE Temp_event;"

SELECT_EVENTS_BY_TAG = "SELECT *\
    FROM Event, Temp_event\
    WHERE Event.event_id = Temp_event.event_id;"

CREATE_VIEW_EVENT_BY_CATEGORY = "CREATE OR REPLACE VIEW temp_events_by_category AS\
                            SELECT *\
                            FROM Event\
                            WHERE Event.category_id = (SELECT category_id\
                                                        FROM Category\
                                                        WHERE Category.name = '{category}');"

DROP_VIEW_EVENT_BY_CATEGORY = "DROP TABLE temp_events_by_category;"

CREATE_VIEW_EVENT_BY_TAGS = "CREATE OR REPLACE VIEW temp_events_by_tags AS\
                            SELECT DISTINCT e.event_id\
                            FROM temp_events_by_category AS e, Event_tag AS et\
                            WHERE (e.event_id = et.event_id) AND (et.word IN ({tags}));"

DROP_VIEW_EVENT_BY_TAGS = "DROP TABLE temp_events_by_tags;"


SELECT_EVENTS_BY_CATEGORY_AND_TAG = "SELECT *\
                                    FROM Event, temp_events_by_tags\
                                    WHERE Event.event_id = temp_events_by_tags.event_id;"

SELECT_TAGS_BY_EVENT_ID = "SELECT word\
                        FROM Event_tag AS et, Event AS e\
                        WHERE et.event_id = e.event_id\
                        AND e.event_id = {event_id};"

SELECT_TICKET_BY_EVENT = "SELECT *\
                        FROM Ticket\
                        WHERE event_id = {event_id};"
