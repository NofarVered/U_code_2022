const renderer = new Renderer();
const ticketsClass = new Model();

async function renderTickets() {
  try {
    await ticketsClass.loadTickets();
    renderer.render(ticketsClass.getTickets());
  } catch (e) {
    console.log(e);
  }
}

renderTickets();

function openNotificationHandler() {
  renderer.renderModal(
    "We found some tickets for you..",
    "tickets, tickets,tickets"
  );
}

async function showTicketsHandler(el) {
  const id = $(el).attr("id");
  try {
    await ticketsClass.loadTickets();
    const tickets_data = renderer.getTickets();
    renderer.renderTemplateModal(tickets, tickets_data);
  } catch (e) {}
}

$("#notification-btn").on("click", openNotificationHandler);
$("#events-container").on("click", ".event-body", ({ target }) =>
  showTicketsHandler(target)
);

$("#demo-modal").on("click", ".close-btn", renderer.removeModal);
