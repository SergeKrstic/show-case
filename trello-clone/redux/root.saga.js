import { all } from 'redux-saga/effects';
import { metaTypes } from './entities/models.types';
import { regeneratingSaga } from 'redux/saga.utils';
import * as firestoreSagas from 'firebase/redux/firestore.sagas';
import * as modelSagas from './entities/models.sagas';

const watchAllFirestoreSagas = firestoreSagas.createWatchAllSaga(metaTypes);

export default function* rootSagas() {
  yield all([watchAllFirestoreSagas(), modelSagas.watchAll()]);
}

export const regeneratingRootSaga = regeneratingSaga([
  watchAllFirestoreSagas(),
  modelSagas.watchAll
]);
