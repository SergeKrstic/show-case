import { mockFirebase, mockFirestore } from './mock-firestore';
import { convertCollectionsSnapshotToMap } from 'firebase/utils/firestore.utils';

describe('mock firestore', () => {
  xit('should return users collection', () => {
    let mockFirestore = mockFirebase.getFirestore();
    console.log(mockFirebase);
    console.log('mockFirestore:', mockFirestore);
    console.log('users:', mockFirestore.collection('users').get());
  });

  xit('should return a list collection from TrelloClone', async () => {
    let pathToLists = 'users/MOCK_USER_ID/agents/GGRvO9ToyqlucCqrmXdw/lists';

    const printLists = async message => {
      let query = await mockFirebase
        .getFirestore()
        .collection(pathToLists)
        .get();
      let remoteLists = convertCollectionsSnapshotToMap(query);
      console.log(message, '=>', remoteLists);
    };

    await printLists('initial');

    await mockFirebase
      .getFirestore()
      .collection(pathToLists)
      .doc('b-project-l-backlog')
      .update({ name: 'back-log' });

    await printLists('modified');

    mockFirebase.reset();

    await printLists('reset');
  });
});
