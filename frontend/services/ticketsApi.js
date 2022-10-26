
async function fetchTickets(event_id) {
    const data = await $.get( f`http://localhost:8000/tickets/?event_id=${event_id}`);
    return data;
  }
  
  