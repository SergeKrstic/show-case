import { createSlice } from '@reduxjs/toolkit';
import { firestoreTypes } from 'firebase/redux/firestore.types';

const boardViewSlice = createSlice({
  name: 'boardView',
  initialState: {
    boardId: '',
    activeCardId: null,

    // Potential new cards
    potentialNewCards: {
      listId: { cardName: '' }
    },

    // Create card form
    isCreateCardFormOpen: false,
    isFocusOnCreateCardForm: false,
    createCardFormIndexToOpen: 0,
    createCardFormListId: '',

    // Search cards form
    searchTerm: '',

    // Create list form
    isCreateListFormOpen: false,
    isFocusOnCreateListForm: false,

    // Update list name form
    isUpdateListNameFormOpen: false,
    isFocusOnUpdateListNameForm: false,
    updateListNameFormIndexToOpen: 0,

    // Update board name form
    isUpdateBoardNameFormOpen: false,
    isFocusOnUpdateBoardNameForm: false
  },
  reducers: {
    // CreateCardForm
    openCreateCardForm(state, action) {
      const { listIndex } = action.payload;
      state.createCardFormIndexToOpen = listIndex;
      state.isCreateCardFormOpen = true;
    },
    closeCreateCardForm(state, action) {
      state.createCardFormIndexToOpen = 0;
      state.isCreateCardFormOpen = false;
    },
    focusOnCardForm(state, action) {
      state.isFocusOnCreateCardForm = true;
    },
    blurOnCardForm(state, action) {
      state.isFocusOnCreateCardForm = false;
    },
    updateCreateCardForm(state, action) {
      const { listId, cardName } = action.payload;
      state.createCardFormListId = listId;
      state.potentialNewCards[listId] = { cardName };
    },
    // Search cards form
    updateSearchTerm(state, action) {
      const { searchTerm } = action.payload;
      state.searchTerm = searchTerm;
    },
    // CreateListForm
    openCreateListForm(state, action) {
      state.isCreateListFormOpen = true;
    },
    closeCreateListForm(state, action) {
      state.isCreateListFormOpen = false;
    },
    focusOnListForm(state, action) {
      state.isFocusOnCreateListForm = true;
    },
    blurOnListForm(state, action) {
      state.isFocusOnCreateListForm = false;
    },
    // UpdateListNameForm
    openUpdateListNameForm(state, action) {
      const { listIndex } = action.payload;
      state.updateListNameFormIndexToOpen = listIndex;
      state.isUpdateListNameFormOpen = true;
    },
    closeUpdateListNameForm(state, action) {
      state.updateListNameFormIndexToOpen = 0;
      state.isUpdateListNameFormOpen = false;
    },
    focusOnUpdateListNameForm(state, action) {
      state.isFocusOnUpdateListNameForm = true;
    },
    blurOnUpdateListNameForm(state, action) {
      state.isFocusOnUpdateListNameForm = false;
    },
    // UpdateBoardName
    openUpdateBoardNameForm(state, action) {
      state.isUpdateBoardNameOpen = true;
    },
    closeUpdateBoardNameForm(state, action) {
      state.isUpdateBoardNameOpen = false;
    },
    focusOnUpdateBoardNameForm(state, action) {
      state.isFocusOnUpdateBoardNameForm = true;
    },
    blurOnUpdateBoardNameForm(state, action) {
      state.isFocusOnUpdateBoardNameForm = false;
    },
    // Card actions
    setActiveCard(state, action) {
      const { id } = action.payload;
      state.activeCardId = id;
    },
    // board actions
    setBoardId(state, action) {
      const { id } = action.payload;
      state.boardId = id;
    },
    [firestoreTypes.ON_DOCUMENT_ADDED](state, action) {
      if ((action.meta.type = 'card')) {
      }
    }
  }
});

export const {
  // CreateCardForm
  openCreateCardForm,
  closeCreateCardForm,
  focusOnCardForm,
  blurOnCardForm,
  updateCreateCardForm,
  // Search cards form
  updateSearchTerm,
  // CreateListForm
  openCreateListForm,
  closeCreateListForm,
  focusOnListForm,
  blurOnListForm,
  // UpdateListNameForm
  openUpdateListNameForm,
  closeUpdateListNameForm,
  focusOnUpdateListNameForm,
  blurOnUpdateListNameForm,
  // UpdateBoardName
  openUpdateBoardNameForm,
  closeUpdateBoardNameForm,
  focusOnUpdateBoardNameForm,
  blurOnUpdateBoardNameForm,
  // Card actions
  setActiveCard,
  // board actions
  setBoardId
} = boardViewSlice.actions;

export default boardViewSlice.reducer;
