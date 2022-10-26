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

SELECT_EVENTS_BY_CATEGORY_AND_TAG = "SELECT *\
                                    FROM Event\
                                    WHERE event_id = (SELECT event_id\
                                                    FROM event_tag\
                                                    WHERE word = '{word}')\
                                    AND category_id = (SELECT category_id\
                                                FROM Category\
                                                WHERE name = '{category_name}')\
                                    ORDER BY date DESC;"

SELECT_TICKET_BY_EVENT = "SELECT *\
                        FROM Ticket\
                        WHERE event_id = {event_id};"
