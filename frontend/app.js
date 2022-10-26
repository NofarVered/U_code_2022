const renderer = new Renderer();
const ticketsClass = new TicketsModel();

async function renderTickets() {
  print("dddd");
  try {
    await ticketsClass.loadTickets();
    renderer.render(ticketsClass.getTickets());
  } catch (e) {
    console.log(e);
  }
}

renderTickets();
