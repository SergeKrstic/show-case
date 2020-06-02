import Api from './api';

import { mockFirebase } from '../utils/mock-firestore';
import { MOCK_USER_ID } from '../utils/constants';

export function api(userId) {
  return userId === MOCK_USER_ID
    ? new Api(userId, mockFirebase.getFirestore())
    : new Api(userId);
}

export default Api;
