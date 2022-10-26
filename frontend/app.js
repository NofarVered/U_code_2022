const renderer = new Renderer();
const ticketsClass = new TicketsModel();

async function renderTickets() {
  try {
    await ticketsClass.loadTickets();
    renderer.render(ticketsClass.getTickets());
  } catch (e) {
    console.log(e)
}
}

renderTickets();

async function openNotificationHandler(){
  try {
    renderer.renderModal("We found some tickets for you..","tickets, tickets,tickets")
  } catch (e) {
    console.log(e)
}
}

$("#notification-btn").on("click",openNotificationHandler );
$("#demo-modal").on("click", ".close-btn", renderer.removeModal);
