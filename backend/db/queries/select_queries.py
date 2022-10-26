SELECT_ALL_EVENTS = "SELECT *\
                      FROM Event\
                      ORDER BY date DESC;"
SELECT_EVENTS_BY_CATEGORY = "SELECT *\
                            FROM Event\
                            WHERE category_id = (SELECT category_id\
                                                FROM Category\
                                                WHERE name = '{category_name}')\
                            ORDER BY date DESC;"
SELECT_EVENTS_BY_TAGS = ""
SELECT_EVENTS_BY_CATEGORY_AND_TAGS = ""

SELECT_TAGS_BY_EVENT_ID ="SELECT word\
                        FROM Event_tag AS et, Event AS e\
                        WHERE et.event_id = e.event_id\
                        AND e.event_id = {event_id};"
                        
SELECT_TICKET_BY_EVENT = "SELECT *\
                        FROM Ticket\
                        WHERE event_id = {event_id};"
