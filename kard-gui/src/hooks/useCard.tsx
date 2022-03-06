import axios from "axios";
import { useQuery } from "react-query";


const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;


export const fetchCardDeck = async (deckId: number) => {
  const response = await axios.get(`${API_BASE_URL}/decks/${deckId}/`);
  return response.data;
};

type CardType = {
  cardId: number,
  deckId: number,
  reviewSessionId: number,
  correct: boolean,
  timeTaken: number,
  otherMetrics: object,
}

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
  card: CardType
): Promise<any> => {
  const response = await axios.post(
    `${API_BASE_URL}/reviewed_cards/`,
    {
      card_id: card.cardId,
      review_session_id: card.reviewSessionId,
      correct: card.correct,
      time_taken: card.timeTaken,
      other_metrics: card.otherMetrics,

    }
  );
  return response.data;
};

export const fetchCard = async (cardId: number) => {
  if (cardId === undefined) {
    return undefined;
  }

  const resp = await axios
    .get(`${API_BASE_URL}/cards/${cardId}`);

  return resp.data;
}
export default function useCard(cardId: number) {

  return useQuery(["card", cardId], () => fetchCard(cardId));
}
