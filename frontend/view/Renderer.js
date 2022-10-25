class Renderer{
    render(tickets) {
        const container = $("#tickets-container");
        container.empty();
        let newTicketsEl = this.createTemplateEl("ticket-template", {tickets});
        container.append(newTicketsEl);
      }

      createTemplateEl(id, data) {
        let source = $(`#${id}`).html();
        let template = Handlebars.compile(source);
        let newEl = template(data);
        return newEl;
      }
}