import React from "react";
import axios from "axios";
import { useQuery } from "react-query";

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
const API_PASSWORD = process.env.REACT_APP_API_PASSWORD || "";

export const fetchCardDeck = async (deckId: number) => {
  const response = await axios.get(`${API_BASE_URL}/decks/${deckId}/`, {
    auth: { username: "zui", password: API_PASSWORD },
  });
  return response.data;
};

/**
 * createReviewedCard
 * POST to /api/reviewed_cards
 * @param cardId
 * @param reviewSessionId
 * @param correct: boolean: whether the user answered the card correctly
 * @param timeTaken: number: the time taken to answer the card (in seconds)
 * @param otherMetrics: object: other metrics to be stored
 */
export const createReviewedCard = async (
  cardId: number,
  reviewSessionId: number,
  correct: boolean,
  timeTaken: number,
  otherMetrics: object = {}
): Promise<any> => {
  const response = await axios.post(
    `${API_BASE_URL}/reviewed_cards/`,
    {
      card: `${API_BASE_URL}/cards/${cardId}/`,
      review_session: `${API_BASE_URL}/review_sessions/${reviewSessionId}/`,
      correct: correct,
      time_taken: timeTaken,
      other_metrics: otherMetrics,
    },
    { auth: { username: "zui", password: API_PASSWORD } }
  );
  return response.data;
};

export const fetchCard = async (cardId: number) => {
  if (cardId === undefined) {
    return undefined;
  }

  const resp = await axios
    .get(`${API_BASE_URL}/cards/${cardId}`, {
      auth: { username: "zui", password: API_PASSWORD },
    });

  return resp.data;
}
export default function useCard(cardId: number) {

  return useQuery(["card", cardId], () => fetchCard(cardId));
}
