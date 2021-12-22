import React from "react";
import axios from "axios";
import { useQuery } from "react-query";

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
const API_PASSWORD = process.env.REACT_APP_API_PASSWORD || "";

export const fetchCard = (cardId: String) =>
  axios
    .get(`${API_BASE_URL}/cards/${cardId}`, {
      auth: { username: "zui", password: API_PASSWORD },
    })
    .then((response) => response.data);

export default function useCard(cardId: String) {
  return useQuery(["card", cardId], () => fetchCard(cardId));
}
