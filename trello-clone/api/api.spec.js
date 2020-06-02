import Api from './api';
import { mockFirebase } from '../utils/mock-firestore';
import { TEST_USER_ID } from '../utils/constants';

let api;

beforeEach(() => {
  mockFirebase.reset();
  api = new Api(TEST_USER_ID, mockFirebase.getFirestore());
});

describe('api.base', () => {
  it('should construct', () => {
    expect(api.baseApi).toBeDefined();
    expect(api.boards._collectionRef._id).toBe('boards');
    expect(api.cards._collectionRef._id).toBe('cards');
    expect(api.domains._collectionRef._id).toBe('domains');
    expect(api.lists._collectionRef._id).toBe('lists');
  });
});

describe('api.lists', () => {
  it('should get all the lists', async () => {
    let allLists = await api.lists.getAll();
    expect(allLists.length).toBe(6);
  });

  it('should get all the lists for board', async () => {
    let boardLists = await api.lists.getAllForBoard('qY4mlACYKOVvWKozrL9f');
    expect(boardLists.length).toBe(3);
  });

  it('should add a new list', async () => {
    let allListBefore = await api.lists.getAll();
    expect(allListBefore.length).toBe(6);

    let list = await api.lists.add({
      name: 'list 7',
      closed: false,
      idBoard: 'qY4mlACYKOVvWKozrL9f',
      position: 7
    });

    expect(list.name).toEqual('list 7');
    expect(list.id).toBeDefined();

    let allListAfter = await api.lists.getAll();
    expect(allListAfter.length).toBe(7);
  });

  const expectedListData = {
    id: 'O43oGS30rUhObqHXGhUt',
    closed: false,
    idBoard: 'qY4mlACYKOVvWKozrL9f',
    name: 'list 2',
    position: 2
  };

  it('should get a list', async () => {
    let list = await api.lists.get('O43oGS30rUhObqHXGhUt');
    expect(list).toStrictEqual(expectedListData);
  });

  it('should update a list', async () => {
    let listBefore = await api.lists.get('O43oGS30rUhObqHXGhUt');
    expect(listBefore).toStrictEqual(expectedListData);

    const updatedList = await api.lists.update('O43oGS30rUhObqHXGhUt', {
      closed: true
    });

    let listAfter = await api.lists.get('O43oGS30rUhObqHXGhUt');
    expect(listAfter).toStrictEqual({ ...expectedListData, closed: true });
  });

  it('should delete a list', async () => {
    let allListBefore = await api.lists.getAll();
    expect(allListBefore.length).toBe(7);

    await api.lists.delete('O43oGS30rUhObqHXGhUt');

    let allListAfter = await api.lists.getAll();
    expect(allListAfter.length).toBe(6);
  });
});

describe('api.boards', () => {
  it('should get all the boards', async () => {
    let allBoards = await api.boards.getAll();
    expect(allBoards.length).toBe(6);
  });

  it('should get all the boards for domain', async () => {
    let domainBoards = await api.boards.getAllForDomain('WEkAT5DVhTlP24s8Bc0L');
    expect(domainBoards.length).toBe(2);
  });

  it('should add a new board', async () => {
    let allBoardsBefore = await api.boards.getAll();
    expect(allBoardsBefore.length).toBe(6);

    let board = await api.boards.add({
      name: 'board 7',
      isClosed: false,
      isStarred: false,
      idDomain: 'WEkAT5DVhTlP24s8Bc0L'
    });

    expect(board.name).toEqual('board 7');
    expect(board.id).toBeDefined();

    let allBoardsAfter = await api.boards.getAll();
    expect(allBoardsAfter.length).toBe(7);
  });

  const expectedBoardData = {
    id: 'qY4mlACYKOVvWKozrL9f',
    name: 'Board 1',
    isClosed: false,
    isStarred: false,
    idDomain: 'WEkAT5DVhTlP24s8Bc0L'
  };

  it('should get a board', async () => {
    let board = await api.boards.get('qY4mlACYKOVvWKozrL9f');
    expect(board).toStrictEqual(expectedBoardData);
  });

  it('should update a board', async () => {
    let boardBefore = await api.boards.get('qY4mlACYKOVvWKozrL9f');
    expect(boardBefore).toStrictEqual(expectedBoardData);

    await api.boards.update('qY4mlACYKOVvWKozrL9f', { closed: true });

    let boardAfter = await api.boards.get('qY4mlACYKOVvWKozrL9f');
    expect(boardAfter).toStrictEqual({ ...expectedBoardData, closed: true });
  });

  it('should delete a board', async () => {
    let allBoardsBefore = await api.boards.getAll();
    expect(allBoardsBefore.length).toBe(7);

    await api.boards.delete('qY4mlACYKOVvWKozrL9f');

    let allBoardsAfter = await api.boards.getAll();
    expect(allBoardsAfter.length).toBe(6);
  });
});

describe('api.cards', () => {
  it('should get all the cards', async () => {
    let allCards = await api.cards.getAll();
    expect(allCards.length).toBe(6);
  });

  it('should get all the cards for board', async () => {
    let boardCards = await api.cards.getAllForBoard('qY4mlACYKOVvWKozrL9f');
    expect(boardCards.length).toBe(6);
  });

  it('should add a new card', async () => {
    let allCardsBefore = await api.cards.getAll();
    expect(allCardsBefore.length).toBe(6);

    let card = await api.cards.add({
      name: 'card 7',
      description: 'Description for card 7',
      idBoard: 'qY4mlACYKOVvWKozrL9f',
      idList: '4Ec9RcEH6tfmY5CmSV94',
      position: 7
    });

    expect(card.name).toEqual('card 7');
    expect(card.id).toBeDefined();

    let allCardsAfter = await api.cards.getAll();
    expect(allCardsAfter.length).toBe(7);
  });

  const expectedCardData = {
    id: 'LGlh5LNKdaJ7HuudM8RI',
    name: 'Card 1',
    description: 'Description for card 1',
    idBoard: 'qY4mlACYKOVvWKozrL9f',
    idList: '4Ec9RcEH6tfmY5CmSV94',
    position: 1
  };

  it('should get a card', async () => {
    let card = await api.cards.get('LGlh5LNKdaJ7HuudM8RI');
    expect(card).toStrictEqual(expectedCardData);
  });

  it('should update a card', async () => {
    let cardBefore = await api.cards.get('LGlh5LNKdaJ7HuudM8RI');
    expect(cardBefore).toStrictEqual(expectedCardData);

    await api.cards.update('LGlh5LNKdaJ7HuudM8RI', { closed: true });

    let cardAfter = await api.cards.get('LGlh5LNKdaJ7HuudM8RI');
    expect(cardAfter).toStrictEqual({ ...expectedCardData, closed: true });
  });

  it('should delete a card', async () => {
    let allCardsBefore = await api.cards.getAll();
    expect(allCardsBefore.length).toBe(7);

    await api.cards.delete('LGlh5LNKdaJ7HuudM8RI');

    let allCardsAfter = await api.cards.getAll();
    expect(allCardsAfter.length).toBe(6);
  });
});

describe('api.domains', () => {
  it('should get all the domains', async () => {
    let allDomains = await api.domains.getAll();
    expect(allDomains.length).toBe(2);
  });

  it('should add a new domain', async () => {
    let allDomainsBefore = await api.domains.getAll();
    expect(allDomainsBefore.length).toBe(2);

    // Todo: return board
    let domain = await api.domains.add({
      name: 'Domain 3',
      description: 'Description for domain 3',
      idBoards: []
    });

    expect(domain.name).toEqual('Domain 3');
    expect(domain.id).toBeDefined();

    let allDomainsAfter = await api.domains.getAll();
    expect(allDomainsAfter.length).toBe(3);
  });

  const expectedDomainData = {
    id: 'WEkAT5DVhTlP24s8Bc0L',
    name: 'Domain 1',
    description: 'This is a domain',
    idBoards: ['qY4mlACYKOVvWKozrL9f', 'gyU21eTIafag5MkbUjNC']
  };

  it('should get a domain', async () => {
    let domain = await api.domains.get('WEkAT5DVhTlP24s8Bc0L');
    expect(domain).toStrictEqual(expectedDomainData);
  });

  it('should update a domain', async () => {
    let domainBefore = await api.domains.get('WEkAT5DVhTlP24s8Bc0L');
    expect(domainBefore).toStrictEqual(expectedDomainData);

    await api.domains.update('WEkAT5DVhTlP24s8Bc0L', { closed: true });

    let domainAfter = await api.domains.get('WEkAT5DVhTlP24s8Bc0L');
    expect(domainAfter).toStrictEqual({ ...expectedDomainData, closed: true });
  });

  it('should delete a domain', async () => {
    let allDomainsBefore = await api.domains.getAll();
    expect(allDomainsBefore.length).toBe(3);

    await api.domains.delete('WEkAT5DVhTlP24s8Bc0L');

    let allDomainsAfter = await api.domains.getAll();
    expect(allDomainsAfter.length).toBe(2);
  });
});
