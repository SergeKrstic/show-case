import { call, select, put, take } from '../mySagaImpl';
import { getUser } from './api';
import { selectUserId } from './store';

export function* mySaga03() {
  yield take('getUser');
  const userId = yield select(selectUserId);
  const user = yield call(getUser, userId);
  yield put({ type: 'getUserSuccess', payload: user });
}
