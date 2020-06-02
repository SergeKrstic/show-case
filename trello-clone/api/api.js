import { firestore } from 'firebase/utils/firebase.utils';
import BaseApi from 'firebase/api/base.api';

import CommandsApi from './models/commands.api';
import BoardsApi from './models/boards.api';
import CardsApi from './models/cards.api';
import DomainsApi from './models/domains.api';
import ListsApi from './models/lists.api';

import { BOARDS_URL, CARDS_URL, DOMAINS_URL, LISTS_URL } from './api.constants';

class Api {
  constructor(userId, mockFirestore = null) {
    this.firestore = mockFirestore ? mockFirestore : firestore;

    this.boardsRef = this.firestore.collection(`users/${userId}/${BOARDS_URL}`);
    this.cardsRef = this.firestore.collection(`users/${userId}/${CARDS_URL}`);
    this.listsRef = this.firestore.collection(`users/${userId}/${LISTS_URL}`);
    this.domainsRef = this.firestore.collection(
      `users/${userId}/${DOMAINS_URL}`
    );

    this.baseApi = new BaseApi();
    this.commands = new CommandsApi(userId);
    this.boards = new BoardsApi(this.baseApi, this.boardsRef);
    this.cards = new CardsApi(this.baseApi, this.cardsRef);
    this.domains = new DomainsApi(this.baseApi, this.domainsRef);
    this.lists = new ListsApi(this.baseApi, this.listsRef);
  }
}

export default Api;
