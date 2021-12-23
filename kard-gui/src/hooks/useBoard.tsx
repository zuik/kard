import axios from "axios";

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
const API_PASSWORD = process.env.REACT_APP_API_PASSWORD || "";

/**
 * createReviewSession
 * POST to /api/review_sessions
 */
export const createReviewSession = async (
  userId: number
): Promise<any> => {
  const response = await axios.post(
    `${API_BASE_URL}/review_sessions/`,
    {
      user: `${API_BASE_URL}/users/${userId}/`,
    },
    { auth: { username: "zui", password: API_PASSWORD } }
  );
  return response.data;
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

  const response = await axios.patch(
    `${API_BASE_URL}/review_sessions/${reviewSessionId}/`,
    { ended: date.toISOString() },
    { auth: { username: "zui", password: API_PASSWORD } }
  );
  return response.data;
};

