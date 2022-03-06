import axios from "axios";

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;


/**
 * createReviewSession
 * POST to /api/review_sessions
 */
export const createReviewSession = async (
  userId: number
): Promise<any> => {
  const date = new Date();
  try {
    const response = await axios.post(`${API_BASE_URL}/review_sessions/`,
      {
        started: date.toISOString()
      }
    );
    return response.data;
  }
  catch (err) {
    console.log(err);
    return {};
  }
};
/**
 * endReviewSession
 * PUT to /api/review_sessions/:id
 * Will set the current time as the end date of the review session
 * @param reviewSessionId
 * @returns
 */
export const endReviewSession = async (
  reviewSessionId: number
): Promise<any> => {
  const date = new Date();
  try {
    const response = await axios.put(
      `${API_BASE_URL}/review_sessions/${reviewSessionId}/`,
      { ended: date.toISOString() }
    );
    return response.data;
  }
  catch (err) {
    console.log(err);
    return {};
  }
};

