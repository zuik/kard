import { useState } from "react";

const CARD_STYLE = {
  border: "1px solid black",
  maxWidth: "300px",
  margin: "10px",
  padding: "10px",
};

const PROMPT_STYLE = {
  fontSize: "2.5em",
  fontWeight: "bold",
};
type CardType = {
  id: number;
  url: string;
  name: string;
  prompt: string;
  answer: string;
  card_type: string;
  added: string;
  updated: string;
};

function Card({ card, onRightAnswer, empty = false }: { card: CardType | undefined, onRightAnswer: (duration: number) => void, empty?: boolean }) {

  const [answer, setAnswer] = useState("");
  const [startTime, _] = useState(Date.now());

  function handleCardSubmit(event: any, startTime: number) {
    event.preventDefault();

    console.log("submit");
    console.log(event);

    console.log("duration", Date.now() - startTime);
    if (card?.answer === answer) {
      onRightAnswer(Date.now() - startTime);
    } else {
      setAnswer("");
    }
  }
  return (
    <div style={CARD_STYLE}>
      {empty ?
        <div>
          <p>Empty card</p>
          <button onClick={(e) => onRightAnswer(Date.now() - startTime)}>Start</button>
        </div> :
        <div>
          <p>{startTime}</p>
          <p>
            <span style={PROMPT_STYLE}>{card ? card.prompt : ""}</span>
          </p>
          <form onSubmit={(e) => handleCardSubmit(e, startTime)}>
            <input
              autoFocus
              type="text"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
            />
          </form>
        </div>}
    </div>
  );
}

export default Card;
