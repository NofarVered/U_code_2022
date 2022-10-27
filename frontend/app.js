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

async function openNotificationHandler() {
    try {
    await model.loadEvents("music", "");
      renderer.renderTemplateModal("events", "event-template", {
        events: model.getEvents(),
      });
    } catch (e) {
      console.log(e);
    }

}

async function getEventsByUser() {
  let category = $("#select-form option:selected").text();
  if (category === "Select Category") {
    category = "";
  }
  let textInput = $("#input-search").val();
  let tagsArray = textInput.split(" ").join("%20");
  await model.loadEvents(category, tagsArray);
  renderer.render("events-container", "event-template", {
    events: model.getEvents(),
  });
}
async function showTicketsHandler(el) {
  const id = $(el).closest(".event-body").attr("id");
  try {
    await model.loadTickets(id);
    const tickets_data = model.getTickets();
    renderer.renderTemplateModal("", "ticket-template", {
      tickets: tickets_data,
    });
  } catch (e) {
    console.log(e);
  }
}

function addWishHandler() {
  renderer.renderTemplateModal(
    "Couldn't find what you where looking for?",
    "wish-form-template",
    {}
  );
}

function sendWishHandler() {
  renderer.removeModal();
  renderer.renderModal(
    "Thank you!",
    "We will let you knon when we have tickets for you!"
  );
}

$("#btn-search").on("click", getEventsByUser);
$("#notification-btn").on("click", openNotificationHandler);
$("#events-container").on("click", ".event-body", ({ target }) =>
  showTicketsHandler(target)
);
$("#events-container").on("click", "#wish-btn", addWishHandler);
$("#demo-modal").on("click", ".send-wish-btn", sendWishHandler);
$("#demo-modal").on("click", ".close-btn", renderer.removeModal);

renderEvents();
