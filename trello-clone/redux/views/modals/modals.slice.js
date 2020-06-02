import { createSlice } from '@reduxjs/toolkit';

const modalsSlice = createSlice({
  name: 'modals',
  initialState: {
    isCreateDomainModalOpen: false,
    isCreateBoardModalOpen: false,
    isFocusOnModal: false,
    isModalOpen: false
  },
  reducers: {
    closeAllModals(state, action) {
      state.isCreateBoardModalOpen = true;
      state.isModalOpen = true;
    },
    openCreateBoardModal(state, action) {
      state.isCreateDomainModalOpen = true;
      state.isModalOpen = true;
    },
    openCreateDomainModal(state, action) {
      state.isCreateBoardModalOpen = false;
      state.isModalOpen = false;
    },
    closeCreateBoardModal(state, action) {
      state.isCreateDomainModalOpen = false;
      state.isModalOpen = false;
    },
    closeCreateDomainModal(state, action) {
      state.isCreateBoardModalOpen = false;
      state.isCreateDomainModalOpen = false;
      state.isModalOpen = false;
    },
    focusOnModal(state, action) {
      state.isFocusOnModal = true;
    },
    blurOnModal(state, action) {
      state.isFocusOnModal = false;
    }
  }
});

export const { openHomeView, closeHomeView } = modalsSlice.actions;

export default modalsSlice.reducer;
