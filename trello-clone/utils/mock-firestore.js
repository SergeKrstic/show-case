import MockFirebase from 'mock-cloud-firestore';
import { MOCK_USER_ID } from './constants';
import { cloneDeep } from 'lodash';

const fixtureData = {
  __collection__: {
    agents: { __doc__: {} },
    'third-parties': { __doc__: {} },
    users: {
      __doc__: {
        [MOCK_USER_ID]: {
          createdAt: '20 August 2019 at 17:07:06 UTC+8',
          displayName: 'Mock User',
          email: 'user@mock.com',
          __collection__: {
            agents: {
              __doc__: {
                GGRvO9ToyqlucCqrmXdw: {
                  name: 'SmartKanban',
                  __collection__: {
                    boards: {
                      __doc__: {
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
                          listIds: [
                            'b-next-l-next',
                            'b-next-l-doing',
                            'b-next-l-today'
                          ],
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
                    cards: {
                      __doc__: {
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
                    },
                    domains: {
                      __doc__: {
                        WEkAT5DVhTlP24s8Bc0L: {
                          name: 'Domain 1',
                          description: 'This is a domain',
                          boardIds: [
                            'qY4mlACYKOVvWKozrL9f',
                            'gyU21eTIafag5MkbUjNC'
                          ]
                        }
                      }
                    },
                    lists: {
                      __doc__: {
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
                          cardIds: [
                            'card-3',
                            'card-7',
                            'card-11',
                            'card-18',
                            'card-19'
                          ],
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
                    }
                  }
                }
              }
            },
            entries: { __doc__: {} },
            'third-parties': { __doc__: {} }
          }
        },
        Rwc20oNDgKQ32bwVOOKbPYzndrG3: {
          createdAt: '20 August 2019 at 12:16:11 UTC+8',
          displayName: 'Srdjan Krstic',
          email: 'srdjankrstic@gmail.com',
          __collection__: {
            agents: { __doc__: {} },
            entries: { __doc__: {} },
            'third-parties': { __doc__: {} }
          }
        }
      }
    }
  }
};

var mockFirebase = (function() {
  var _mockFirestore;

  function createMockFirestore() {
    return new MockFirebase(cloneDeep(fixtureData)).firestore();
  }

  return {
    getFirestore: function() {
      if (!_mockFirestore) {
        _mockFirestore = createMockFirestore();
      }
      return _mockFirestore;
    },
    reset: function() {
      _mockFirestore = null;
    }
  };
})();

export { mockFirebase };
