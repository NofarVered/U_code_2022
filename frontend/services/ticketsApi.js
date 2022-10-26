
async function fetchTickets() {
    const data = await $.get( `http://localhost:8000/tickets/`);
    return data;
  }
  
  