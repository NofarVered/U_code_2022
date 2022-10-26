
class Event:
    def __init__(self, event_object) -> None:
        self.event_id = event_object["event_id"]
        self.title = event_object["title"]
        self.location = event_object["location"]
        self.event_img = event_object["event_img"]
        self.category_id = event_object["category_id"]
        self.date = event_object["date"]
