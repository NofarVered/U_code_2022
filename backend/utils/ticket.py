
class Ticket:
    def __init__(self, ticket_object) -> None:
        self.ticket_id = ticket_object["ticket_id"]
        self.title = ticket_object["title"]
        self.price = ticket_object["price"]
        self.location = ticket_object["location"]
        self.ticket_img = ticket_object["ticket_img"]
        self.category_id = ticket_object["category_id"]
        self.date = ticket_object["date"]
