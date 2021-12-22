const CARD_STYLE = {
  border: "1px solid black",
  maxWidth: "300px",
  margin: "10px",
  padding: "10px",
};

function Card(props: any) {
  return (
    <div style={CARD_STYLE}>
      <p>{JSON.stringify(props.card)}</p>
    </div>
  );
}

export default Card;
