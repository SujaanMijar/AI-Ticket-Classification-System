// src/api.js
export async function createTicket(text) {
  const response = await fetch("http://127.0.0.1:8000/api/tickets/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
  });

  if (!response.ok) {
    throw new Error("Failed to create ticket");
  }

  return await response.json();
}
