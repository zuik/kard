import { useEffect, useState } from 'react'
import Card from './Card'

import useCard, { fetchCardDeck, createReviewedCard } from './hooks/useCard'
import { createReviewSession, endReviewSession } from './hooks/useBoard'
import { fetchDeck, fetchDecks } from './hooks/useDeck';


import _ from 'lodash'

type ReviewSession = {
  id: number
  url: string
  user: string
  started: string
  ended: string | null
}
/**
 * selectCards
 * Randomly select a number of cards from the deck
 * @param deckId
 * @param noCards : number : number of card to be selected from the deck. -1 means all cards
 */
async function selectCards(deckId: number, noCards: number) {
  const deck = await fetchDeck(deckId)
  const cardIds = deck.cards.map((card: any) => card.id);
  if (noCards === -1) {
    return cardIds
  } else {
    return _.sampleSize(cardIds, noCards)
  }
}

type DeckType = {
  id: number,
  name: string,
  description: string,
  added: string,
  updated: string,
}

function DeckSelector(props: any) {
  const [decks, setDecks] = useState<Array<DeckType> | null>(null);

  useEffect(() => {
    const decksResp = fetchDecks();
    decksResp.then((decks) => {
      setDecks(decks);
    });
  }, []);



  return (<div>
    Deck select: <select>
      {decks && decks.map((d: DeckType, ix) => <option key={ix} value={d.name}>{d.name}</option>)}
    </select>
  </div>)
}


function Board() {
  const [cardId, setCardId] = useState<any | undefined>(undefined)
  const [board, setBoard] = useState<ReviewSession | undefined>(undefined)
  const [cards, setCards] = useState<number[] | undefined>(undefined)
  const [currentCard, setCurrentCard] = useState<number>(-1)
  const [cardTimings, setCardTimings] = useState<any>({})

  function submitCardMetrics(duration: number) {
    if (board) {
      createReviewedCard(
        {
          cardId: cardId,
          deckId: 2,
          reviewSessionId: board.id,
          correct: true,
          timeTaken: duration,
          otherMetrics: {}
        })
        .then(resp => { console.log(resp) })
    }
  }

  if (cards && currentCard >= 0 && currentCard < cards.length && cardId !== cards[currentCard]) {
    console.log(`Setting cardId to ${cards[currentCard]}`)
    setCardId(cards[currentCard])
  }

  if (board && cards === undefined) {
    // If board is loaded, we can select the cards from the deck by 
    // calling selectCards and loads 10 cards into cards
    console.log(board)
    selectCards(2, 10).then(cardIds => {
      setCards(cardIds)
    })
  }
  const query = useCard(cardId)
  return (
    <div style={{ margin: '10px' }}>
      <h1>A review board!</h1>
      <DeckSelector />
      <div>
        {board ? (
          <div>
            <p>
              <span style={{ fontWeight: 'bold' }}>
                Board {board.id} loaded 👍
              </span>
            </p>
          </div>
        ) : (
          <p>Loading...</p>
        )}
        <button
          onClick={async () => {
            const data = await createReviewSession(1)
            setBoard(data)
          }}
        >
          Create Review Session
        </button>

        <button
          onClick={async () => {
            if (!board) return
            const data = await endReviewSession(board.id)

            setCards(undefined)
            setCardId(undefined)
            setCardTimings({})
            setCurrentCard(-1)

            console.log('Ended Review Session', data)
          }}
        >
          End Review Session
        </button>
      </div>
      <div>
        <span style={{ fontWeight: 'bold' }}>
          Card list
        </span>
        <ul>
          {cards ? cards.map((cardId, cardIdx) =>
            cardIdx === currentCard ? <li key={cardId} style={{ fontWeight: "bold" }}>👉Card {cardId}</li> : <li key={cardId}>Card {cardId}{cardId in cardTimings ? ` | ⏰ ${cardTimings[cardId]}ms` : ""}</li>
          ) : <li>Loading...</li>}
        </ul>
      </div>

      {cardId ? (query.isLoading ? (
        <p>Loading...</p>
      ) : query.isError ? (
        <p>Error!</p>
      ) : (
        <Card card={query.data} onRightAnswer={(duration: number) => {
          setCurrentCard(currentCard + 1);
          setCardTimings({ ...cardTimings, [cardId]: duration })
          // cardTimings[cardId] = duration;
          submitCardMetrics(duration);
        }} />
      )) : <Card card={undefined} onRightAnswer={(_) => {
        setCurrentCard(0);
      }} empty />}
    </div>
  )
}
export default Board
