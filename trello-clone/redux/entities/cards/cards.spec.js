import { firestoreTypes } from 'firebase/redux/firestore.types';
import { metaTypes } from '../models.types';
import * as actions from './cards.actions';

import { TEST_USER_ID } from '../../../utils/constants';

describe('cards actions', () => {
  const metaType = { type: metaTypes.cards };
  const cardId = 'card-01';
  const cardData = {
    id: cardId,
    name: 'New card',
    description: 'New card description',
    isClosed: false,
    boardName: 'Board 1',
    boardId: 'board-01',
    listId: 'list-01',
    due: null,
    dueCompleted: false,
    labels: [],
    dateCreated: '',
    dateListChanged: '',
    dateModified: ''
  };

  it('should create addCard action', () => {
    const action = actions.addCard(TEST_USER_ID, cardId, cardData, null, false);
    expect(action.type).toEqual(firestoreTypes.SET_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.data).toEqual(cardData);
  });

  it('should create updateCard action', () => {
    const cardData = {
      name: 'Card name updated',
      description: 'Card description updated',
      dateModified: ''
    };
    const action = actions.updateCard(
      TEST_USER_ID,
      cardId,
      cardData,
      null,
      false
    );
    expect(action.type).toEqual(firestoreTypes.UPDATE_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.id).toEqual(cardId);
    expect(action.payload.data).toEqual(cardData);
  });

  it('should create deleteCard action', () => {
    const action = actions.deleteCard(TEST_USER_ID, cardData);
    expect(action.type).toEqual(firestoreTypes.REMOVE_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.id).toEqual(cardId);
    expect(action.payload.data).toEqual(cardData);
  });

  it('should create listenToAllCards action', () => {
    const action = actions.listenToAllCards(TEST_USER_ID);
    expect(action.type).toEqual(firestoreTypes.ADD_LISTENER_REQUEST);
    expect(action.meta).toEqual(metaType);
  });

  it('should create listenToCards action', () => {
    const boardId = 'board-01';
    const action = actions.listenToCards(TEST_USER_ID, boardId);
    expect(action.type).toEqual(firestoreTypes.ADD_LISTENER_REQUEST);
    expect(action.meta).toEqual(metaType);
  });

  it('should create removeCardsListener action', () => {
    const action = actions.removeCardsListener();
    expect(action.type).toEqual(firestoreTypes.REMOVE_LISTENER_REQUEST);
    expect(action.meta).toEqual(metaType);
  });
});
