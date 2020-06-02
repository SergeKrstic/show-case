import { delay } from 'redux-saga';
import { call, put, select, take } from 'redux-saga/effects';

import { getFlashQueue } from './getters';
import { ADD_FLASH_MESSAGE, SHOW_FLASH, CLEAR_FLASH } from './actions';

const FIVE_SECONDS = 5000;

export function* showFlashMessage() {
  yield put({ type: SHOW_FLASH });
  yield call(delay, FIVE_SECONDS); // wait 5 secs
  yield put({ type: CLEAR_FLASH });
}

export function* onAddFlashMessage() {
  while (true) {
    const flashQueue = yield select(getFlashQueue);

    // empty what's in the queue first
    if (flashQueue.length > 0) {
      while (true) {
        const queue = yield select(getFlashQueue);
        if (queue.length === 0) {
          break;
        }

        yield showFlashMessage();
      }
    }

    // wait until we get a new ADD_FLASH_MESSAGE action
    yield take(ADD_FLASH_MESSAGE);
    yield showFlashMessage();
  }
}
