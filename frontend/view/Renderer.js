class Renderer{
    render(tickets) {
        const container = $("#tickets-container");
        container.empty();
        let newTicketsEl = this.createTemplateEl("ticket-template", {tickets});
        container.append(newTicketsEl);
      }

      renderModal(title, content) {
        const container = $("#demo-modal");
        container.css("display", "flex");
        let newModalEl = this.createTemplateEl("modal-template", {
          title,
          content,
        });
    
        container.append(newModalEl);
      }
    
      removeModal() {
        const container = $("#demo-modal");
        container.css("display", "none");
        container.empty();
      }

      createTemplateEl(id, data) {
        let source = $(`#${id}`).html();
        let template = Handlebars.compile(source);
        let newEl = template(data);
        return newEl;
      }
}