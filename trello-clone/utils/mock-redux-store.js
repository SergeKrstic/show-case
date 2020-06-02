import { TEST_USER_ID, TEST_BOARD_ID } from './constants';

const mockStoreInitialState = {
  entities: {
    domains: {
      inProgress: false,
      error: '',
      items: {
        'domain-0': {
          id: 'domain-0',
          name: 'Focus',
          description: '',
          boardIds: ['board-1', 'board-2']
        },
        'domain-2': {
          id: 'domain-1',
          name: 'Domain 1',
          description: '',
          boardIds: [TEST_BOARD_ID, 'board-4']
        },
        'domain-3': {
          id: 'domain-2',
          name: 'Domain 2',
          description: '',
          boardIds: ['board-5']
        }
      }
    },
    boards: {
      inProgress: false,
      error: '',
      items: {
        'board-1': {
          id: 'board-1',
          name: 'Today',
          description: '',
          domainId: 'domain-0',
          domainName: 'Focus',
          isClosed: false,
          isStarred: false,
          listIds: []
        },
        'board-2': {
          id: 'board-2',
          name: 'Next',
          description: '',
          domainId: 'domain-0',
          domainName: 'Focus',
          isClosed: false,
          isStarred: false,
          listIds: []
        },
        [TEST_BOARD_ID]: {
          id: TEST_BOARD_ID,
          name: 'Project 1',
          description: '',
          domainId: 'domain-1',
          domainName: 'Domain 1',
          isClosed: false,
          isStarred: true,
          listIds: ['list-1', 'list-2', 'list-3']
        },
        'board-4': {
          id: 'board-4',
          name: 'Project 2',
          description: '',
          domainId: 'domain-1',
          domainName: 'Domain 1',
          isClosed: false,
          isStarred: false,
          listIds: []
        },
        'board-5': {
          id: 'board-5',
          name: 'Project 3',
          description: '',
          domainId: 'domain-2',
          domainName: 'Domain 2',
          isClosed: false,
          isStarred: true,
          listIds: []
        }
      }
    },
    lists: {
      inProgress: false,
      error: '',
      items: {
        'list-1': {
          id: 'list-1',
          name: 'list 1',
          boardId: TEST_BOARD_ID,
          cardIds: ['card-1', 'card-2', 'card-3', 'card-4']
        },
        'list-2': {
          id: 'list-2',
          name: 'list 2',
          boardId: TEST_BOARD_ID,
          cardIds: ['card-5', 'card-6']
        },
        'list-3': {
          id: 'list-3',
          name: 'list 3',
          boardId: TEST_BOARD_ID,
          cardIds: []
        }
      }
    },
    cards: {
      inProgress: false,
      error: '',
      items: {
        'card-1': { id: 'card-1', name: 'card 1', listId: 'list-1' },
        'card-2': { id: 'card-2', name: 'card 2', listId: 'list-1' },
        'card-3': { id: 'card-3', name: 'card 3', listId: 'list-1' },
        'card-4': { id: 'card-4', name: 'card 4', listId: 'list-1' },
        'card-5': { id: 'card-5', name: 'card 5', listId: 'list-1' },
        'card-6': { id: 'card-6', name: 'card 6', listId: 'list-1' },
        'card-7': { id: 'card-7', name: 'card 7', listId: 'list-2' },
        'card-8': { id: 'card-8', name: 'card 8', listId: 'list-2' },
        'card-9': { id: 'card-9', name: 'card 9', listId: 'list-2' }
      }
    }
  },
  session: {
    userId: TEST_USER_ID,
    userName: 'John Smith'
  },
  views: {
    boardView: {
      boardId: TEST_BOARD_ID,
      // Create card form
      isFocusOnCreateCardForm: false,
      isCreateCardFormOpen: true,
      createCardFormIndexToOpen: 1,
      // Search cards from
      searchTerm: '',
      // Create list form
      isCreateListFormOpen: false,
      isFocusOnCreateListForm: false,
      // Update list name form
      isFocusOnUpdateListNameForm: false,
      isUpdateListNameFormOpen: false,
      updateListNameFormIndexToOpen: 1,
      // Update board name form
      isUpdateBoardNameFormOpen: false,
      isFocusOnUpdateBoardNameForm: false
    },
    boardsMenu: {
      isFocusOnBoardsMenu: false,
      isBoardsMenuOpen: false,

      userInput: ''
    },
    home: {
      errorMessage: '',

      isFetchingHomeSuccessful: true,
      isFetchingHome: false,
      isFetching: false
    },
    modals: {
      isCreateDomainModalOpen: false,
      isCreateBoardModalOpen: false,
      isFocusOnModal: false,
      isModalOpen: false
    },
    notification: {
      errorMessages: []
    },
    popOver: {
      isFocusOnPopHover: false,
      isPopOverOpen: false
    }
  }
};

export default mockStoreInitialState;
