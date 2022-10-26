SELECT_ALL_TICKETS = "SELECT *\
                      FROM Ticket\
                      ORDER BY date DESC;"
SELECT_TICKETS_BY_CATEGORY = "SELECT *\
                            FROM Ticket\
                            WHERE category_id = (SELECT category_id\
                                                FROM Category\
                                                WHERE name = '{category_name}')\
                            ORDER BY date DESC;"
SELECT_TICKETS_BY_TAGS = ""
SELECT_TICKETS_BY_CATEGORY_AND_TAGS = ""
