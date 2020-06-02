import { firestoreTypes } from 'firebase/redux/firestore.types';
import { metaTypes } from '../models.types';
import * as actions from './domains.actions';

import { TEST_USER_ID } from '../../../utils/constants';

describe('domains actions', () => {
  const metaType = { type: metaTypes.domains };
  const domainId = 'domain-01';
  const domainData = {
    id: domainId,
    name: 'New domain',
    description: 'New domain description',
    boardIds: ['board-01'],
    dateCreated: '',
    dateModified: ''
  };

  it('should create addDomain action', () => {
    const action = actions.addDomain(
      TEST_USER_ID,
      domainId,
      domainData,
      null,
      false
    );
    expect(action.type).toEqual(firestoreTypes.SET_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.data).toEqual(domainData);
  });

  it('should create updateDomain action', () => {
    const domainData = {
      name: 'Domain name updated',
      description: 'Domain description updated',
      dateModified: ''
    };
    const action = actions.updateDomain(
      TEST_USER_ID,
      domainId,
      domainData,
      null,
      false
    );
    expect(action.type).toEqual(firestoreTypes.UPDATE_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.id).toEqual(domainId);
    expect(action.payload.data).toEqual(domainData);
  });

  it('should create deleteDomain action', () => {
    const action = actions.deleteDomain(TEST_USER_ID, domainData);
    expect(action.type).toEqual(firestoreTypes.REMOVE_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.id).toEqual(domainId);
    expect(action.payload.data).toEqual(domainData);
  });

  it('should create listenToAllDomains action', () => {
    const action = actions.listenToAllDomains(TEST_USER_ID);
    expect(action.type).toEqual(firestoreTypes.ADD_LISTENER_REQUEST);
    expect(action.meta).toEqual(metaType);
  });

  it('should create removeDomainsListener action', () => {
    const action = actions.removeDomainsListener();
    expect(action.type).toEqual(firestoreTypes.REMOVE_LISTENER_REQUEST);
    expect(action.meta).toEqual(metaType);
  });
});
