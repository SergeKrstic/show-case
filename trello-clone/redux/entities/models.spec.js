import { expectSaga } from 'redux-saga-test-plan';
import { createStore, applyMiddleware } from 'redux';
import createSagaMiddleware from 'redux-saga';

import * as actions from './models.actions';
import { calculateNewCardOrder } from './models.utils';

import rootReducer from '../root.reducer';
import rootSaga from '../root.saga';
import { mockFirebase } from '../../utils/mock-firestore';
import { MOCK_USER_ID } from '../../utils/constants';
import { convertCollectionsSnapshotToMap } from 'firebase/utils/firestore.utils';

const initialState = {
  entities: {
    boards: {
      inProgress: false,
      error: '',
      items: {
        'b-project': {
          id: 'b-project',
          name: 'Project',
          listIds: [
            'b-project-l-backlog',
            'b-project-l-next',
            'b-project-l-today',
            'b-project-l-doing',
            'b-project-l-done',
            'b-project-l-discarded'
          ],
          isClosed: false,
          isStarred: true,
          domainId: ''
        },
        'b-next': {
          id: 'b-next',
          name: 'Next',
          listIds: ['b-next-l-next', 'b-next-l-doing', 'b-next-l-today'],
          isClosed: false,
          isStarred: true,
          domainId: ''
        },
        'b-today': {
          id: 'b-today',
          name: 'Today',
          listIds: [
            'b-today-l-today',
            'b-today-l-in-progress',
            'b-today-l-done'
          ],
          isClosed: false,
          isStarred: true,
          domainId: ''
        }
      }
    },
    lists: {
      inProgress: false,
      error: '',
      items: {
        // Project board lists
        'b-project-l-backlog': {
          id: 'b-project-l-backlog',
          name: 'Backlog',
          cardIds: ['card-1', 'card-26', 'card-27'],
          boardId: 'b-project',
          isClosed: false
        },
        'b-project-l-next': {
          id: 'b-project-l-next',
          name: 'Next',
          cardIds: ['card-4', 'card-5', 'card-10'],
          boardId: 'b-project',
          isClosed: false
        },
        'b-project-l-today': {
          id: 'b-project-l-today',
          name: 'Today',
          cardIds: ['card-3', 'card-7', 'card-11'],
          boardId: 'b-project',
          isClosed: false
        },
        'b-project-l-doing': {
          id: 'b-project-l-doing',
          name: 'Doing',
          cardIds: ['card-2', 'card-12', 'card-13'],
          boardId: 'b-project',
          isClosed: false
        },
        'b-project-l-done': {
          id: 'b-project-l-done',
          name: 'Done',
          cardIds: ['card-8', 'card-14', 'card-15'],
          boardId: 'b-project',
          isClosed: false
        },
        'b-project-l-discarded': {
          id: 'b-project-l-discarded',
          name: 'Discarded',
          cardIds: [],
          boardId: 'b-project',
          isClosed: false
        },
        // Other project board lists
        'b-other-l-backlog': {
          id: 'b-other-l-backlog',
          name: 'Backlog',
          cardIds: ['card-28', 'card-29', 'card-30'],
          boardId: 'b-project',
          isClosed: false
        },
        'b-other-l-next': {
          id: 'b-other-l-next',
          name: 'Next',
          cardIds: ['card-6', 'card-16', 'card-17'],
          boardId: 'b-other',
          isClosed: false
        },
        'b-other-l-today': {
          id: 'b-other-l-today',
          name: 'Today',
          cardIds: ['card-18', 'card-19', 'card-20'],
          boardId: 'b-other',
          isClosed: false
        },
        'b-other-l-doing': {
          id: 'b-other-l-doing',
          name: 'Doing',
          cardIds: ['card-21', 'card-22', 'card-23'],
          boardId: 'b-other',
          isClosed: false
        },
        'b-other-l-done': {
          id: 'b-other-l-done',
          name: 'Done',
          cardIds: ['card 9', 'card-24', 'card-25'],
          boardId: 'b-other',
          isClosed: false
        },
        'b-other-l-discarded': {
          id: 'b-other-l-discarded',
          name: 'Discarded',
          cardIds: [],
          boardId: 'b-other',
          isClosed: false
        },
        // Next board lists
        'b-next-l-next': {
          id: 'b-next-l-next',
          name: 'Next',
          cardIds: [
            'card-4',
            'card-5',
            'card-6',
            'card-10',
            'card-16',
            'card-17'
          ],
          boardId: 'b-next',
          isClosed: false
        },
        'b-next-l-today': {
          id: 'b-next-l-today',
          name: 'Today',
          cardIds: [
            'card-3',
            'card-7',
            'card-11',
            'card-18',
            'card-19',
            'card-20'
          ],
          boardId: 'b-next',
          isClosed: false
        },
        'b-next-l-doing': {
          id: 'b-next-l-doing',
          name: 'Doing',
          cardIds: [
            'card-2',
            'card-12',
            'card-13',
            'card-21',
            'card-22',
            'card-23'
          ],
          boardId: 'b-next',
          isClosed: false
        },
        'b-next-l-done': {
          id: 'b-next-l-done',
          name: 'Done',
          cardIds: [
            'card-8',
            'card-9',
            'card-14',
            'card-15',
            'card-24',
            'card-25'
          ],
          boardId: 'b-next',
          isClosed: false
        },
        // Today board lists
        'b-today-l-today': {
          id: 'b-today-l-today',
          name: 'Today',
          cardIds: ['card-3', 'card-7', 'card-11', 'card-18', 'card-19'],
          boardId: 'b-today',
          isClosed: false
        },
        'b-today-l-in-progress': {
          id: 'b-today-l-in-progress',
          name: 'In Progress',
          cardIds: ['card-20'],
          boardId: 'b-today',
          isClosed: false
        },
        'b-today-l-done': {
          id: 'b-today-l-done',
          name: 'Done',
          cardIds: [
            'card-8',
            'card-9',
            'card-14',
            'card-15',
            'card-24',
            'card-25'
          ],
          boardId: 'b-today',
          isClosed: false
        }
      }
    },
    cards: {
      inProgress: false,
      error: '',
      items: {
        'card-1': {
          id: 'card-1',
          name: 'card 1',
          listId: 'b-project-l-backlog',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-2': {
          id: 'card-2',
          name: 'card 2',
          listId: 'b-project-l-doing',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-3': {
          id: 'card-3',
          name: 'card 3',
          listId: 'b-project-l-today',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-4': {
          id: 'card-4',
          name: 'card 4',
          listId: 'b-project-l-next',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-5': {
          id: 'card-5',
          name: 'card 5',
          listId: 'b-project-l-next',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-6': {
          id: 'card-6',
          name: 'card 6',
          listId: 'b-other-l-next',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-7': {
          id: 'card-7',
          name: 'card 7',
          listId: 'b-project-l-today',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-8': {
          id: 'card-8',
          name: 'card 8',
          listId: 'b-project-l-done',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-9': {
          id: 'card-9',
          name: 'card 9',
          listId: 'b-other-l-done',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-10': {
          id: 'card-10',
          name: 'card 10',
          listId: 'b-project-l-next',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-11': {
          id: 'card-11',
          name: 'card 11',
          listId: 'b-project-l-today',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-12': {
          id: 'card-12',
          name: 'card 12',
          listId: 'b-project-l-doing',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-13': {
          id: 'card-13',
          name: 'card 13',
          listId: 'b-project-l-doing',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-14': {
          id: 'card-14',
          name: 'card 14',
          listId: 'b-project-l-done',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-15': {
          id: 'card-15',
          name: 'card 15',
          listId: 'b-project-l-done',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-16': {
          id: 'card-16',
          name: 'card 16',
          listId: 'b-other-l-next',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-17': {
          id: 'card-17',
          name: 'card 17',
          listId: 'b-other-l-next',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-18': {
          id: 'card-18',
          name: 'card 18',
          listId: 'b-other-l-today',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-19': {
          id: 'card-19',
          name: 'card 19',
          listId: 'b-other-l-today',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-20': {
          id: 'card-20',
          name: 'card 20',
          listId: 'b-other-l-today',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-21': {
          id: 'card-21',
          name: 'card 21',
          listId: 'b-other-l-doing',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-22': {
          id: 'card-22',
          name: 'card 22',
          listId: 'b-other-l-doing',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-23': {
          id: 'card-23',
          name: 'card 23',
          listId: 'b-other-l-doing',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-24': {
          id: 'card-24',
          name: 'card 24',
          listId: 'b-other-l-done',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-25': {
          id: 'card-25',
          name: 'card 25',
          listId: 'b-other-l-done',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-26': {
          id: 'card-26',
          name: 'card 26',
          listId: 'b-project-l-backlog',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-27': {
          id: 'card-27',
          name: 'card 27',
          listId: 'b-project-l-backlog',
          boardId: 'b-project',
          isClosed: false,
          description: ''
        },
        'card-28': {
          id: 'card-28',
          name: 'card 28',
          listId: 'b-other-l-backlog',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-29': {
          id: 'card-29',
          name: 'card 29',
          listId: 'b-other-l-backlog',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        },
        'card-30': {
          id: 'card-30',
          name: 'card 30',
          listId: 'b-other-l-backlog',
          boardId: 'b-other',
          isClosed: false,
          description: ''
        }
      }
    }
  },
  session: { userId: MOCK_USER_ID, userName: 'Mock User' },
  form: {},
  views: {
    boardView: {
      boardId: 'b-project',
      isCreateCardFormOpen: false,
      isFocusOnCreateCardForm: false,
      createCardFormIndexToOpen: 0,
      isCreateListFormOpen: false,
      isFocusOnCreateListForm: false,
      isUpdateListNameFormOpen: false,
      isFocusOnUpdateListNameForm: false,
      updateListNameFormIndexToOpen: 0,
      isUpdateBoardNameFormOpen: false,
      isFocusOnUpdateBoardNameForm: false
    }

    // modals: {
    //   isCreateDomainModalOpen: false,
    //   isCreateBoardModalOpen: false,
    //   isFocusOnModal: false,
    //   isModalOpen: false
    // },
    // popOver: {
    //   isPopOverOpen: false,
    //   isFocusOnPopOver: false
    // },
    // notification: {
    //   errorMessages: []
    // },
    // boardsMenu: {
    //   isFocusOnBoardsMenu: false,
    //   isBoardsMenuOpen: false,
    //   userInput: ''
    // }
  }
};

describe('boardView integration', () => {
  let pathToLists = 'users/MOCK_USER_ID/agents/GGRvO9ToyqlucCqrmXdw/lists';
  let pathToCards = 'users/MOCK_USER_ID/agents/GGRvO9ToyqlucCqrmXdw/cards';

  const assertCardArrangement = async (
    { cardArrangements, cardDetails },
    storeState
  ) => {
    let mockFirestore = mockFirebase.getFirestore();

    // Assert the card
    let cardsQuery = await mockFirestore.collection(pathToCards).get();
    let remoteCards = convertCollectionsSnapshotToMap(cardsQuery);
    let localCards = storeState.entities.cards.items;
    let { cardId, listId } = cardDetails;
    try {
      expect(localCards[cardId].listId).toBe(listId);
      expect(remoteCards[cardId].listId).toBe(listId);
    } catch (error) {
      console.log(
        `failed:\n  - listId  = ${listId}\n  - cardId  = ${cardId}\n`
      );
      throw error;
    }

    // Assert the lists
    let listsQuery = await mockFirestore.collection(pathToLists).get();
    let remoteLists = convertCollectionsSnapshotToMap(listsQuery);
    let localLists = storeState.entities.lists.items;

    for (let cardArrangement of cardArrangements) {
      let { listId, hasCard, cardId, cardPos } = cardArrangement;
      try {
        if (hasCard) {
          expect(localLists[listId].cardIds).toContain(cardId);
          expect(localLists[listId].cardIds.indexOf(cardId)).toBe(cardPos);
          expect(remoteLists[listId].cardIds).toContain(cardId);
          expect(remoteLists[listId].cardIds.indexOf(cardId)).toBe(cardPos);
        } else {
          expect(localLists[listId].cardIds).not.toContain(cardId);
          expect(localLists[listId].cardIds.indexOf(cardId)).toBe(cardPos);
          expect(remoteLists[listId].cardIds).not.toContain(cardId);
          expect(remoteLists[listId].cardIds.indexOf(cardId)).toBe(cardPos);
        }
      } catch (error) {
        console.log(
          `failed:\n  - listId  = ${listId}\n  - hasCard = ${hasCard}\n  - cardId  = ${cardId}\n  - cardPos = ${cardPos}`
        );
        throw error;
      }
    }
  };

  const getCardIs = (state, listId) => {
    return state.entities.lists.items[listId].cardIds;
  };

  beforeEach(() => {
    mockFirebase.reset();
  });

  describe('events originating from Project board', () => {
    describe('update Next board', () => {
      it('should add the card ID to the "Next" board when a new card is "CREATED" in a monitored list', async () => {
        const newCard = {
          name: 'Card 31',
          description: 'a new card',
          isClosed: false,
          boardName: 'Project',
          boardId: 'b-project',
          listId: 'b-project-l-next'
        };

        expect(getCardIs(initialState, 'b-project-l-next').length).toBe(3);
        expect(getCardIs(initialState, 'b-next-l-next').length).toBe(6);

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.addCard(newCard))
          .silentRun();

        // expect(getCardIs(storeState, 'b-project-l-next').length).toBe(4);
        // expect(getCardIs(storeState, 'b-next-l-next').length).toBe(7);
      });

      // it('should remove the card ID from the "Next" board when a card is "DELETED" in a monitored list', async () => {});

      it('should add the card ID to the "Next" board when a card is "MOVED INTO" a monitored list', async () => {
        let dragResult = {
          draggableId: 'card-1',
          type: 'card',
          reason: 'DROP',
          source: {
            droppableId: 'b-project-l-backlog',
            index: 0
          },
          destination: {
            droppableId: 'b-project-l-next',
            index: 2
          }
        };

        await assertCardArrangement(
          {
            cardDetails: { cardId: 'card-1', listId: 'b-project-l-backlog' },
            cardArrangements: [
              {
                listId: 'b-project-l-backlog',
                hasCard: true,
                cardId: 'card-1',
                cardPos: 0
              },
              {
                listId: 'b-project-l-next',
                hasCard: false,
                cardId: 'card-1',
                cardPos: -1
              },
              {
                listId: 'b-next-l-next',
                hasCard: false,
                cardId: 'card-1',
                cardPos: -1
              }
            ]
          },
          initialState
        );

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-project' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: { cardId: 'card-1', listId: 'b-project-l-next' },
            cardArrangements: [
              {
                listId: 'b-project-l-backlog',
                hasCard: false,
                cardId: 'card-1',
                cardPos: -1
              },
              {
                listId: 'b-project-l-next',
                hasCard: true,
                cardId: 'card-1',
                cardPos: 2
              },
              {
                listId: 'b-next-l-next',
                hasCard: true,
                cardId: 'card-1',
                cardPos: 6
              }
            ]
          },
          storeState
        );
      });

      it('should remove the card ID from the "Next" board when a card is "MOVED OUT OF" a monitored list', async () => {
        let dragResult = {
          draggableId: 'card-12',
          type: 'card',
          reason: 'DROP',
          source: {
            droppableId: 'b-project-l-doing',
            index: 1
          },
          destination: {
            droppableId: 'b-project-l-backlog',
            index: 2
          }
        };

        await assertCardArrangement(
          {
            cardDetails: { cardId: 'card-12', listId: 'b-project-l-doing' },
            cardArrangements: [
              {
                listId: 'b-project-l-doing',
                hasCard: true,
                cardId: 'card-12',
                cardPos: 1
              },
              {
                listId: 'b-project-l-backlog',
                hasCard: false,
                cardId: 'card-12',
                cardPos: -1
              },
              {
                listId: 'b-next-l-doing',
                hasCard: true,
                cardId: 'card-12',
                cardPos: 1
              }
            ]
          },
          initialState
        );

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-project' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: { cardId: 'card-12', listId: 'b-project-l-backlog' },
            cardArrangements: [
              {
                listId: 'b-project-l-doing',
                hasCard: false,
                cardId: 'card-12',
                cardPos: -1
              },
              {
                listId: 'b-project-l-backlog',
                hasCard: true,
                cardId: 'card-12',
                cardPos: 2
              },
              {
                listId: 'b-next-l-doing',
                hasCard: false,
                cardId: 'card-12',
                cardPos: -1
              }
            ]
          },
          storeState
        );
      });

      it('should update the card ID location in the "Next" board when a card is "MOVED BETWEEN" monitored lists ', async () => {
        let dragResult = {
          draggableId: 'card-13',
          type: 'card',
          reason: 'DROP',
          source: {
            droppableId: 'b-project-l-doing',
            index: 2
          },
          destination: {
            droppableId: 'b-project-l-today',
            index: 0
          }
        };

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-13',
              listId: 'b-project-l-doing'
            },
            cardArrangements: [
              {
                listId: 'b-project-l-doing',
                hasCard: true,
                cardId: 'card-13',
                cardPos: 2
              },
              {
                listId: 'b-project-l-today',
                hasCard: false,
                cardId: 'card-13',
                cardPos: -1
              },
              {
                listId: 'b-next-l-doing',
                hasCard: true,
                cardId: 'card-13',
                cardPos: 2
              },
              {
                listId: 'b-next-l-today',
                hasCard: false,
                cardId: 'card-13',
                cardPos: -1
              }
            ]
          },
          initialState
        );

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-project' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-13',
              listId: 'b-project-l-today'
            },
            cardArrangements: [
              {
                listId: 'b-project-l-doing',
                hasCard: false,
                cardId: 'card-13',
                cardPos: -1
              },
              {
                listId: 'b-project-l-today',
                hasCard: true,
                cardId: 'card-13',
                cardPos: 0
              },
              {
                listId: 'b-next-l-doing',
                hasCard: false,
                cardId: 'card-13',
                cardPos: -1
              },
              {
                listId: 'b-next-l-today',
                hasCard: true,
                cardId: 'card-13',
                cardPos: 6
              }
            ]
          },
          storeState
        );
      });
    });

    describe('update Today board', () => {
      it('should add the card ID to the "Today" board when a new card is "CREATED" in a monitored list', async () => {
        const newCard = {
          name: 'Card 31',
          description: 'a new card',
          isClosed: false,
          boardName: 'Project',
          boardId: 'b-project',
          listId: 'b-project-l-today'
        };

        expect(getCardIs(initialState, 'b-project-l-today').length).toBe(3);
        expect(getCardIs(initialState, 'b-next-l-today').length).toBe(6);
        expect(getCardIs(initialState, 'b-today-l-today').length).toBe(5);

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.addCard(newCard))
          .silentRun();

        expect(getCardIs(storeState, 'b-project-l-today').length).toBe(4);
        expect(getCardIs(storeState, 'b-next-l-today').length).toBe(7);
        expect(getCardIs(storeState, 'b-today-l-today').length).toBe(6);
      });

      it('should add the card ID to the "Today" board when a card is "MOVED INTO" a monitored list', async () => {
        let dragResult = {
          draggableId: 'card-27',
          type: 'card',
          reason: 'DROP',
          source: { droppableId: 'b-project-l-backlog', index: 2 },
          destination: { droppableId: 'b-project-l-done', index: 1 }
        };

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-27',
              listId: 'b-project-l-backlog'
            },
            cardArrangements: [
              {
                listId: 'b-project-l-backlog',
                hasCard: true,
                cardId: 'card-27',
                cardPos: 2
              },
              {
                listId: 'b-project-l-done',
                hasCard: false,
                cardId: 'card-27',
                cardPos: -1
              },
              {
                listId: 'b-today-l-done',
                hasCard: false,
                cardId: 'card-27',
                cardPos: -1
              }
            ]
          },
          initialState
        );

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-project' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-27',
              listId: 'b-project-l-done'
            },
            cardArrangements: [
              {
                listId: 'b-project-l-backlog',
                hasCard: false,
                cardId: 'card-27',
                cardPos: -1
              },
              {
                listId: 'b-project-l-done',
                hasCard: true,
                cardId: 'card-27',
                cardPos: 1
              },
              {
                listId: 'b-today-l-done',
                hasCard: true,
                cardId: 'card-27',
                cardPos: 0
              }
            ]
          },
          storeState
        );
      });

      it('should remove the card ID from the "Today" board when a card is "MOVED OUT OF" a monitored list', async () => {
        let dragResult = {
          draggableId: 'card-25',
          type: 'card',
          reason: 'DROP',
          source: { droppableId: 'b-other-l-done', index: 2 },
          destination: { droppableId: 'b-other-l-backlog', index: 0 }
        };

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-25',
              listId: 'b-other-l-done'
            },
            cardArrangements: [
              {
                listId: 'b-other-l-done',
                hasCard: true,
                cardId: 'card-25',
                cardPos: 2
              },
              {
                listId: 'b-other-l-backlog',
                hasCard: false,
                cardId: 'card-25',
                cardPos: -1
              },
              {
                listId: 'b-next-l-done',
                hasCard: true,
                cardId: 'card-25',
                cardPos: 5
              },
              {
                listId: 'b-today-l-done',
                hasCard: true,
                cardId: 'card-25',
                cardPos: 5
              }
            ]
          },
          initialState
        );

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-project' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-25',
              listId: 'b-other-l-backlog'
            },
            cardArrangements: [
              {
                listId: 'b-other-l-done',
                hasCard: false,
                cardId: 'card-25',
                cardPos: -1
              },
              {
                listId: 'b-other-l-backlog',
                hasCard: true,
                cardId: 'card-25',
                cardPos: 0
              },
              {
                listId: 'b-next-l-done',
                hasCard: false,
                cardId: 'card-25',
                cardPos: -1
              },
              {
                listId: 'b-today-l-done',
                hasCard: false,
                cardId: 'card-25',
                cardPos: -1
              }
            ]
          },
          storeState
        );
      });

      it('should update the card ID location in the "Project" board when a card out of the "In Progress" list ', async () => {
        let dragResult = {
          draggableId: 'card-20',
          type: 'card',
          reason: 'DROP',
          source: {
            droppableId: 'b-other-l-today',
            index: 2
          },
          destination: {
            droppableId: 'b-other-l-done',
            index: 1
          }
        };

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-20',
              listId: 'b-other-l-today'
            },
            cardArrangements: [
              {
                listId: 'b-other-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 2
              },
              {
                listId: 'b-other-l-done',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-next-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 5
              },
              {
                listId: 'b-today-l-in-progress',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 0
              }
            ]
          },
          initialState
        );

        expect(getCardIs(initialState, 'b-other-l-today').length).toBe(3);
        expect(getCardIs(initialState, 'b-other-l-done').length).toBe(3);
        expect(getCardIs(initialState, 'b-next-l-today').length).toBe(6);
        expect(getCardIs(initialState, 'b-next-l-done').length).toBe(6);
        expect(getCardIs(initialState, 'b-today-l-in-progress').length).toBe(1);
        expect(getCardIs(initialState, 'b-today-l-done').length).toBe(6);

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-other' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-20',
              listId: 'b-other-l-done'
            },
            cardArrangements: [
              {
                listId: 'b-other-l-today',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-other-l-done',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 1
              },
              {
                listId: 'b-next-l-today',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-next-l-done',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 0
              },
              {
                listId: 'b-today-l-in-progress',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              }
            ]
          },
          storeState
        );

        expect(getCardIs(storeState, 'b-other-l-today').length).toBe(2);
        expect(getCardIs(storeState, 'b-other-l-done').length).toBe(4);
        expect(getCardIs(storeState, 'b-next-l-today').length).toBe(5);
        expect(getCardIs(storeState, 'b-next-l-done').length).toBe(7);
        expect(getCardIs(storeState, 'b-today-l-in-progress').length).toBe(0);
        expect(getCardIs(storeState, 'b-today-l-done').length).toBe(7);
      });

      // it('should update the card ID location in the "Today" board when a card is "MOVED BETWEEN" monitored lists ', async () => {});
    });
  });

  describe('events originating from Next board', () => {
    describe('update Project board', () => {
      // it('should add the card ID to the "Project" board when a card is "MOVED INTO" into a monitored list', async () => {});
      // it('should remove the card ID from the "Project" board when a card is "MOVED OUT OF" out of a monitored list', async () => {});
      it('should update the card ID location in the "Project" board when a card is "MOVED BETWEEN" monitored lists ', async () => {
        let dragResult = {
          draggableId: 'card-7',
          type: 'card',
          reason: 'DROP',
          source: {
            droppableId: 'b-next-l-today',
            index: 1
          },
          destination: {
            droppableId: 'b-next-l-doing',
            index: 4
          }
        };

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-7',
              listId: 'b-project-l-today'
            },
            cardArrangements: [
              {
                listId: 'b-next-l-today',
                hasCard: true,
                cardId: 'card-7',
                cardPos: 1
              },
              {
                listId: 'b-next-l-doing',
                hasCard: false,
                cardId: 'card-7',
                cardPos: -1
              },
              {
                listId: 'b-project-l-today',
                hasCard: true,
                cardId: 'card-7',
                cardPos: 1
              },
              {
                listId: 'b-project-l-doing',
                hasCard: false,
                cardId: 'card-7',
                cardPos: -1
              }
            ]
          },
          initialState
        );

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-next' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-7',
              listId: 'b-project-l-doing'
            },
            cardArrangements: [
              {
                listId: 'b-next-l-today',
                hasCard: false,
                cardId: 'card-7',
                cardPos: -1
              },
              {
                listId: 'b-next-l-doing',
                hasCard: true,
                cardId: 'card-7',
                cardPos: 4
              },
              {
                listId: 'b-project-l-today',
                hasCard: false,
                cardId: 'card-7',
                cardPos: -1
              },
              {
                listId: 'b-project-l-doing',
                hasCard: true,
                cardId: 'card-7',
                cardPos: 3
              }
            ]
          },
          storeState
        );
      });
    });

    describe('update Today board', () => {
      // it('should add the card ID to the "Today" board when a card is "MOVED INTO" into a monitored list', async () => {});
      // it('should remove the card ID from the "Today" board when a card is "MOVED OUT OF" out of a monitored list', async () => {});
      // it('should update the card ID location in the "Today" board when a card is "MOVED BETWEEN" monitored lists ', async () => {});
      it('should update the card ID location in the "Project" board when a card out of the "In Progress" list ', async () => {
        let dragResult = {
          draggableId: 'card-20',
          type: 'card',
          reason: 'DROP',
          source: {
            droppableId: 'b-next-l-today',
            index: 5
          },
          destination: {
            droppableId: 'b-next-l-done',
            index: 1
          }
        };

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-20',
              listId: 'b-other-l-today'
            },
            cardArrangements: [
              {
                listId: 'b-other-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 2
              },
              {
                listId: 'b-other-l-done',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-next-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 5
              },
              {
                listId: 'b-today-l-in-progress',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 0
              }
            ]
          },
          initialState
        );

        expect(getCardIs(initialState, 'b-other-l-today').length).toBe(3);
        expect(getCardIs(initialState, 'b-other-l-done').length).toBe(3);
        expect(getCardIs(initialState, 'b-next-l-today').length).toBe(6);
        expect(getCardIs(initialState, 'b-next-l-done').length).toBe(6);
        expect(getCardIs(initialState, 'b-today-l-in-progress').length).toBe(1);
        expect(getCardIs(initialState, 'b-today-l-done').length).toBe(6);

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-next' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-20',
              listId: 'b-other-l-done'
            },
            cardArrangements: [
              {
                listId: 'b-other-l-today',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-other-l-done',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 0
              },
              {
                listId: 'b-next-l-today',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-next-l-done',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 1
              },
              {
                listId: 'b-today-l-in-progress',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-today-l-done',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 0
              }
            ]
          },
          storeState
        );

        expect(getCardIs(storeState, 'b-other-l-today').length).toBe(2);
        expect(getCardIs(storeState, 'b-other-l-done').length).toBe(4);
        expect(getCardIs(storeState, 'b-next-l-today').length).toBe(5);
        expect(getCardIs(storeState, 'b-next-l-done').length).toBe(7);
        expect(getCardIs(storeState, 'b-today-l-in-progress').length).toBe(0);
        expect(getCardIs(storeState, 'b-today-l-done').length).toBe(7);
      });
    });

    it('should move old today card to doing list', async () => {
      expect(
        initialState.entities.lists.items['b-today-l-today'].cardIds
      ).toStrictEqual(['card-3', 'card-7', 'card-11', 'card-18', 'card-19']);

      expect(
        initialState.entities.lists.items['b-today-l-in-progress'].cardIds
      ).toStrictEqual(['card-20']);

      expect(
        initialState.entities.lists.items['b-next-l-today'].cardIds
      ).toStrictEqual([
        'card-3',
        'card-7',
        'card-11',
        'card-18',
        'card-19',
        'card-20'
      ]);

      expect(
        initialState.entities.lists.items['b-next-l-doing'].cardIds
      ).toStrictEqual([
        'card-2',
        'card-12',
        'card-13',
        'card-21',
        'card-22',
        'card-23'
      ]);

      expect(
        initialState.entities.lists.items['b-project-l-today'].cardIds
      ).toStrictEqual(['card-3', 'card-7', 'card-11']);

      expect(
        initialState.entities.lists.items['b-project-l-doing'].cardIds
      ).toStrictEqual(['card-2', 'card-12', 'card-13']);

      expect(
        initialState.entities.lists.items['b-other-l-today'].cardIds
      ).toStrictEqual(['card-18', 'card-19', 'card-20']);

      expect(
        initialState.entities.lists.items['b-other-l-doing'].cardIds
      ).toStrictEqual(['card-21', 'card-22', 'card-23']);

      const { storeState } = await expectSaga(rootSaga)
        .withReducer(rootReducer, initialState)
        .dispatch(actions.moveOldTodayCardsToDoingList({ moveAll: true }))
        .silentRun();

      expect(
        storeState.entities.lists.items['b-today-l-today'].cardIds
      ).toStrictEqual([]);

      expect(
        storeState.entities.lists.items['b-today-l-in-progress'].cardIds
      ).toStrictEqual([]);

      expect(
        storeState.entities.lists.items['b-next-l-today'].cardIds
      ).toStrictEqual([]);

      expect(
        storeState.entities.lists.items['b-next-l-doing'].cardIds
      ).toStrictEqual([
        'card-3',
        'card-7',
        'card-11',
        'card-18',
        'card-19',
        'card-20',
        'card-2',
        'card-12',
        'card-13',
        'card-21',
        'card-22',
        'card-23'
      ]);

      expect(
        storeState.entities.lists.items['b-project-l-today'].cardIds
      ).toStrictEqual([]);

      expect(
        storeState.entities.lists.items['b-project-l-doing'].cardIds
      ).toStrictEqual([
        'card-2',
        'card-12',
        'card-13',
        'card-11',
        'card-7',
        'card-3'
      ]);

      expect(
        storeState.entities.lists.items['b-other-l-today'].cardIds
      ).toStrictEqual([]);

      expect(
        storeState.entities.lists.items['b-other-l-doing'].cardIds
      ).toStrictEqual([
        'card-21',
        'card-22',
        'card-23',
        'card-20',
        'card-19',
        'card-18'
      ]);
    });
  });

  describe('events originating from Today board', () => {
    describe('update Project board', () => {
      // it('should add the card ID to the "Project" board when a card is "MOVED INTO" into a monitored list', async () => {});
      // it('should remove the card ID from the "Project" board when a card is "MOVED OUT OF" out of a monitored list', async () => {});
      // it('should update the card ID location in the "Project" board when a card is "MOVED BETWEEN" monitored lists ', async () => {});
      it('should NOT update the card ID location in the "Project" board when a card is moved into the "In Progress" list from "Today" list', async () => {
        let dragResult = {
          draggableId: 'card-11',
          type: 'card',
          reason: 'DROP',
          source: {
            droppableId: 'b-today-l-today',
            index: 2
          },
          destination: {
            droppableId: 'b-today-l-in-progress',
            index: 1
          }
        };

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-11',
              listId: 'b-project-l-today'
            },
            cardArrangements: [
              {
                listId: 'b-today-l-today',
                hasCard: true,
                cardId: 'card-11',
                cardPos: 2
              },
              {
                listId: 'b-today-l-in-progress',
                hasCard: false,
                cardId: 'card-11',
                cardPos: -1
              },
              {
                listId: 'b-project-l-today',
                hasCard: true,
                cardId: 'card-11',
                cardPos: 2
              },
              {
                listId: 'b-next-l-today',
                hasCard: true,
                cardId: 'card-11',
                cardPos: 2
              }
            ]
          },
          initialState
        );

        expect(getCardIs(initialState, 'b-today-l-today').length).toBe(5);
        expect(getCardIs(initialState, 'b-today-l-in-progress').length).toBe(1);
        expect(getCardIs(initialState, 'b-project-l-today').length).toBe(3);
        expect(getCardIs(initialState, 'b-next-l-today').length).toBe(6);

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-today' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-11',
              listId: 'b-project-l-today'
            },
            cardArrangements: [
              {
                listId: 'b-today-l-today',
                hasCard: false,
                cardId: 'card-11',
                cardPos: -1
              },
              {
                listId: 'b-today-l-in-progress',
                hasCard: true,
                cardId: 'card-11',
                cardPos: 1
              },
              {
                listId: 'b-project-l-today',
                hasCard: true,
                cardId: 'card-11',
                cardPos: 2
              },
              {
                listId: 'b-next-l-today',
                hasCard: true,
                cardId: 'card-11',
                cardPos: 2
              }
            ]
          },
          storeState
        );

        expect(getCardIs(storeState, 'b-today-l-today').length).toBe(4);
        expect(getCardIs(storeState, 'b-today-l-in-progress').length).toBe(2);
        expect(getCardIs(storeState, 'b-project-l-today').length).toBe(3);
        expect(getCardIs(storeState, 'b-next-l-today').length).toBe(6);
      });

      it('should update the card ID location in the "Project" board when a card out of the "In Progress" list to "Done" list', async () => {
        let dragResult = {
          draggableId: 'card-20',
          type: 'card',
          reason: 'DROP',
          source: {
            droppableId: 'b-today-l-in-progress',
            index: 0
          },
          destination: {
            droppableId: 'b-today-l-done',
            index: 1
          }
        };

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-20',
              listId: 'b-other-l-today'
            },
            cardArrangements: [
              {
                listId: 'b-today-l-in-progress',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 0
              },
              {
                listId: 'b-today-l-done',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-other-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 2
              },
              {
                listId: 'b-next-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 5
              }
            ]
          },
          initialState
        );

        expect(getCardIs(initialState, 'b-today-l-in-progress').length).toBe(1);
        expect(getCardIs(initialState, 'b-today-l-done').length).toBe(6);
        expect(getCardIs(initialState, 'b-other-l-today').length).toBe(3);
        expect(getCardIs(initialState, 'b-other-l-done').length).toBe(3);
        expect(getCardIs(initialState, 'b-next-l-today').length).toBe(6);
        expect(getCardIs(initialState, 'b-next-l-done').length).toBe(6);

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-today' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-20',
              listId: 'b-other-l-done'
            },
            cardArrangements: [
              {
                listId: 'b-today-l-in-progress',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-today-l-done',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 1
              },
              {
                listId: 'b-other-l-today',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-other-l-done',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 0
              },
              {
                listId: 'b-next-l-done',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 0
              }
            ]
          },
          storeState
        );

        expect(getCardIs(storeState, 'b-today-l-in-progress').length).toBe(0);
        expect(getCardIs(storeState, 'b-today-l-done').length).toBe(7);
        expect(getCardIs(storeState, 'b-other-l-today').length).toBe(2);
        expect(getCardIs(storeState, 'b-other-l-done').length).toBe(4);
        expect(getCardIs(storeState, 'b-next-l-today').length).toBe(5);
        expect(getCardIs(storeState, 'b-next-l-done').length).toBe(7);
      });

      it('should update the card ID location in the "Project" board when a card out of the "In Progress" list to "Done" list', async () => {
        let dragResult = {
          draggableId: 'card-20',
          type: 'card',
          reason: 'DROP',
          source: {
            droppableId: 'b-today-l-in-progress',
            index: 0
          },
          destination: {
            droppableId: 'b-today-l-today',
            index: 1
          }
        };

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-20',
              listId: 'b-other-l-today'
            },
            cardArrangements: [
              {
                listId: 'b-today-l-in-progress',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 0
              },
              {
                listId: 'b-today-l-done',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-other-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 2
              },
              {
                listId: 'b-next-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 5
              }
            ]
          },
          initialState
        );

        expect(getCardIs(initialState, 'b-today-l-in-progress').length).toBe(1);
        expect(getCardIs(initialState, 'b-today-l-today').length).toBe(5);
        expect(getCardIs(initialState, 'b-other-l-today').length).toBe(3);
        expect(getCardIs(initialState, 'b-next-l-today').length).toBe(6);

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-today' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-20',
              listId: 'b-other-l-today'
            },
            cardArrangements: [
              {
                listId: 'b-today-l-in-progress',
                hasCard: false,
                cardId: 'card-20',
                cardPos: -1
              },
              {
                listId: 'b-today-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 1
              },
              {
                listId: 'b-other-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 2
              },
              {
                listId: 'b-next-l-today',
                hasCard: true,
                cardId: 'card-20',
                cardPos: 5
              }
            ]
          },
          storeState
        );

        expect(getCardIs(storeState, 'b-today-l-in-progress').length).toBe(0);
        expect(getCardIs(storeState, 'b-today-l-today').length).toBe(6);
        expect(getCardIs(storeState, 'b-other-l-today').length).toBe(3);
        expect(getCardIs(storeState, 'b-next-l-today').length).toBe(6);
      });

      it('should update the card ID location in the "Project" board when a card into the "In Progress" list from "Done" list', async () => {
        let dragResult = {
          draggableId: 'card-15',
          type: 'card',
          reason: 'DROP',
          source: {
            droppableId: 'b-today-l-done',
            index: 3
          },
          destination: {
            droppableId: 'b-today-l-in-progress',
            index: 1
          }
        };

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-15',
              listId: 'b-project-l-done'
            },
            cardArrangements: [
              {
                listId: 'b-today-l-done',
                hasCard: true,
                cardId: 'card-15',
                cardPos: 3
              },
              {
                listId: 'b-today-l-in-progress',
                hasCard: false,
                cardId: 'card-15',
                cardPos: -1
              },
              {
                listId: 'b-next-l-done',
                hasCard: true,
                cardId: 'card-15',
                cardPos: 3
              },
              {
                listId: 'b-project-l-done',
                hasCard: true,
                cardId: 'card-15',
                cardPos: 2
              }
            ]
          },
          initialState
        );

        expect(getCardIs(initialState, 'b-today-l-done').length).toBe(6);
        expect(getCardIs(initialState, 'b-today-l-in-progress').length).toBe(1);
        expect(getCardIs(initialState, 'b-project-l-done').length).toBe(3);
        expect(getCardIs(initialState, 'b-project-l-today').length).toBe(3);
        expect(getCardIs(initialState, 'b-next-l-done').length).toBe(6);
        expect(getCardIs(initialState, 'b-next-l-today').length).toBe(6);

        const { storeState } = await expectSaga(rootSaga)
          .withReducer(rootReducer, initialState)
          .dispatch(actions.moveCard({ dragResult, boardId: 'b-today' }))
          .silentRun();

        await assertCardArrangement(
          {
            cardDetails: {
              cardId: 'card-15',
              listId: 'b-project-l-today'
            },
            cardArrangements: [
              {
                listId: 'b-today-l-done',
                hasCard: false,
                cardId: 'card-15',
                cardPos: -1
              },
              {
                listId: 'b-today-l-in-progress',
                hasCard: true,
                cardId: 'card-15',
                cardPos: 1
              },
              {
                listId: 'b-next-l-done',
                hasCard: false,
                cardId: 'card-15',
                cardPos: -1
              },
              {
                listId: 'b-next-l-today',
                hasCard: true,
                cardId: 'card-15',
                cardPos: 6
              },
              {
                listId: 'b-project-l-done',
                hasCard: false,
                cardId: 'card-15',
                cardPos: -1
              },
              {
                listId: 'b-project-l-today',
                hasCard: true,
                cardId: 'card-15',
                cardPos: 3
              }
            ]
          },
          storeState
        );

        expect(getCardIs(storeState, 'b-today-l-done').length).toBe(5);
        expect(getCardIs(storeState, 'b-today-l-in-progress').length).toBe(2);
        expect(getCardIs(storeState, 'b-project-l-done').length).toBe(2);
        expect(getCardIs(storeState, 'b-project-l-today').length).toBe(4);
        expect(getCardIs(storeState, 'b-next-l-done').length).toBe(5);
        expect(getCardIs(storeState, 'b-next-l-today').length).toBe(7);
      });
    });

    describe('update Next board', () => {
      // it('should add the card ID to the "Next" board when a card is "MOVED INTO" into a monitored list', async () => {});
      // it('should remove the card ID from the "Next" board when a card is "MOVED OUT OF" out of a monitored list', async () => {});
      // it('should update the card ID location in the "Next" board when a card is "MOVED BETWEEN" monitored lists ', async () => {});
    });
  });
});
