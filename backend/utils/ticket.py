class Ticket:
    def __init__(self, ticket_object) -> None:
        self.ticket_id = ticket_object["ticket_id"]
        self.user_id = ticket_object["user_id"]
        self.price = ticket_object["price"]
        self.ticket_img = ticket_object["ticket_img"]
        self.event_id = ticket_object["event_id"]
        self.seat = ticket_object["seat"]
