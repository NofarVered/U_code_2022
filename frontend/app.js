const renderer = new Renderer();
const model = new Model();

async function renderEvents() {
  try {
    await model.loadEvents("", "");
    renderer.render("events-container", "event-template", {
      events: model.getEvents(),
    });
  } catch (e) {
    console.log(e);
  }
}

function openNotificationHandler() {
  renderer.renderModal(
    "We found some tickets for you..",
    "tickets, tickets,tickets"
  );
}

async function openNotificationHandler() {
  try {
    renderer.renderModal(
      "We found some tickets for you..",
      "tickets, tickets,tickets"
    );
  } catch (e) {
    console.log(e);
  }
}

async function getEventsByUser() {
  let category = $("#select-form option:selected").text();
  let textInput = $("#input-search").val();
  let tagsArray = textInput.split(" ");
  for (tag of tagsArray) console.log(tag, category);
}
async function showTicketsHandler(el) {
  const id = $(el).closest(".event-body").attr("id");
  try {
    await model.loadTickets(id);
    const tickets_data = model.getTickets();
    renderer.renderTemplateModal("tickets", "ticket-template", {
      tickets: tickets_data,
    });
  } catch (e) {
    console.log(e);
  }
}

$("#btn-search").on("click", getEventsByUser);
$("#notification-btn").on("click", openNotificationHandler);
$("#events-container").on("click", ".event-body", ({ target }) =>
  showTicketsHandler(target)
);
$("#demo-modal").on("click", ".close-btn", renderer.removeModal);

renderEvents();
