async function fetchEvents(category, tags) {
    url = `http://localhost:8000/events/`
    if (category && tags){
      url += `?category=${category}&tags=${tags}`
    }else if(tags){
      url += `?tags=${tags}`
    }else if(category){
      url += `?category=${category}`
    }
    const data = await $.get(url);
    return data;
  }