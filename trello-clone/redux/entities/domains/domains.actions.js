import { api } from '../../../api';

import * as actions from 'firebase/redux/firestore.actions';
import { Timestamp } from 'firebase/utils/firebase.utils';
import { metaTypes } from '../models.types';

export function addDomain(
  userId,
  domainId,
  { id, name, description, boardIds } = {},
  batch = null,
  hasTimestamp = true
) {
  let setFunc = api(userId).domains.set;
  let data = {
    id,
    name,
    description,
    boardIds,
    dateCreated: hasTimestamp ? Timestamp.now() : '',
    dateModified: hasTimestamp ? Timestamp.now() : ''
  };
  return actions.setDocument(metaTypes.domains, setFunc, domainId, data, batch);
}

export function updateDomain(
  userId,
  domainId,
  data,
  batch = null,
  hasTimestamp = true
) {
  const updateFunc = api(userId).domains.update;
  let dataWithTimestamp = {
    ...data,
    dateModified: hasTimestamp ? Timestamp.now() : ''
  };
  return actions.updateDocument(
    metaTypes.domains,
    updateFunc,
    domainId,
    dataWithTimestamp,
    batch
  );
}

export function deleteDomain(userId, domain, batch = null) {
  const deleteFunc = api(userId).domains.delete;
  return actions.removeDocument(
    metaTypes.domains,
    deleteFunc,
    domain.id,
    domain,
    batch
  );
}

export function listenToAllDomains(userId) {
  const ref = api(userId).domainsRef;
  return actions.addListener(metaTypes.domains, ref);
}

export function removeDomainsListener() {
  return actions.removeListener(metaTypes.domains, false);
}
