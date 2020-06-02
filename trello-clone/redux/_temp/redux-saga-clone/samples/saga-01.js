import { call } from '../mySagaImpl';
import { getUser } from './api';

const showUserName = user => {
  console.log('User:', user.name);
};

export function* mySaga01() {
  const user = yield call(getUser, 1);
  yield call(showUserName, user);
}
