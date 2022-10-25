class TicketsModel {
  #tickets = [];

  getTickets() {
    return JSON.parse(JSON.stringify(this.#tickets));
  }

  cleanTickets() {
    this.#tickets.length = 0;
  }

  async loadTickets() {
    const data = await fetchTickets();
    this.cleanTickets();
    this.#tickets = data;
  }
}
