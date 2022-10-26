class Model {
  #events = []
  #tickets = [];


  getEvents() {
    return JSON.parse(JSON.stringify(this.#events));
  }

  getTickets() {
    return JSON.parse(JSON.stringify(this.#tickets));
  }

  cleanTickets() {
    this.#tickets.length = 0;
  }

  cleanEvents() {
    this.#events.length = 0;
  }

  async loadEvents(category, tags) {
    const data = await fetchEvents(category, tags);
    this.cleanEvents();
    this.#events = data["events"];
  }

  async loadTickets(event_id) {
    const data = await fetchTickets(event_id);
    this.cleanTickets();
    this.#tickets = data["tickets"];
  }
}
