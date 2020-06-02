import { call, select, put } from '../mySagaImpl';
import { getUser } from './api';
import { selectUserId } from './store';

export function* mySaga02() {
  const userId = yield select(selectUserId);
  const user = yield call(getUser, userId);
  yield put({ type: 'getUserSuccess', payload: user });
}
