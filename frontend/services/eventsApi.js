async function fetchEvents(category, tags) {
    url = f`http://localhost:8000/events/?category=${category}&tags=${tags}`
    const data = await $.get(url);
    return data;
  }