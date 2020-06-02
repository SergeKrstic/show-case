import { BASE_API_URL } from '../api.constants';

export default class CommandsApi {
  constructor(userId) {
    this._userId = userId;
  }

  sendWellDoneMessageToUser = () => {
    return fetch(BASE_API_URL + '/trello-clone/task-done', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ userId: this._userId })
    });
  };
}
