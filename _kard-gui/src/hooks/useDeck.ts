import axios from "axios";
import { useQuery } from "react-query";

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

export async function fetchDecks() {
  const response = await axios.get(`${API_BASE_URL}/decks`);
  return response.data;
}

export async function fetchDeck(deckId: number) {
  const response = await axios.get(`${API_BASE_URL}/decks/${deckId}/`);
  return response.data;
}

export default function useDeck(deckId: number) {
  return useQuery(["deck", deckId], () => fetchDeck(deckId));
}
