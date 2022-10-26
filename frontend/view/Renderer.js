class Renderer {

  render(containerId,templateId,data) {
    const container = $('#'+containerId);
    container.empty();
    let newEl = this.createTemplateEl(templateId, data );
    container.append(newEl);
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

  renderTemplateModal(title,templateId,data ){
    let newTemplateEl = this.createTemplateEl(templateId, data);
    this.renderModal(title,newTemplateEl);
  };

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
