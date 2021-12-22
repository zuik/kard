import { useState } from "react";
import Card from "./Card";

import useCard from "./hooks/useCard";

function Board() {
  const [cardId, setCardId] = useState("1");

  const query = useCard(cardId);
  return (
    <div style={{ margin: "10px" }}>
      <h1>A review board!</h1>

      <input
        type="text"
        placeholder="Type the id of the card to fetch"
        value={cardId}
        onChange={(e) => {
          setCardId(e.target.value);
        }}
      />
      <button>Show card</button>

      {query.isLoading ? (
        <p>Loading...</p>
      ) : query.isError ? (
        <p>Error!</p>
      ) : (
        <Card card={query.data} />
      )}
    </div>
  );
}
export default Board;
