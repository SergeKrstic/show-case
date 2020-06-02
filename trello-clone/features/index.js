// Top level
import HomeView from './home-view/home-view.container';
import AllBoardsMenu from './menus/all-boards-menu/all-boards-menu.container';
import Notification from './notification/notification.component';
import PopOver from './pop-over/pop-over.container';

// DomainList
import DomainList from './domain-list/domain-list.container';
import Domain from './domain-list/domain/domain.component';
import DomainHeader from './domain-list/domain-header/domain-header.component';
import BoardItem from './domain-list/board-item/board-item.component';

// BoardView
import BoardView from './board-view/board-view.container';
import Toolbar from './board-view/toolbar/toolbar.container';
import BoardHeader from './board-view/board-header/board-header.container';
import Board from './board-view/board/board.container';
import List from './board-view/list/list.container';
import CardList from './board-view/card-list/card-list.component';
import Card from './board-view/card/card.draggable';

// CardView
import CardView from './card-view/card-view.container';

// import {
//   CreateDomain,
//   CreateBoard,
//   UpdateBoardName,
//   CreateList,
//   CreateCard,
//   UpdateListName,
//   SearchCards
// } from './forms/index';

export {
  // top
  HomeView,
  AllBoardsMenu,
  Notification,
  PopOver,
  // domain view
  DomainList,
  Domain,
  DomainHeader,
  BoardItem,
  // board view
  BoardView,
  Toolbar,
  BoardHeader,
  Board,
  List,
  CardList,
  Card,
  // card view
  CardView
  // forms
  // CreateDomain,
  // CreateBoard,
  // UpdateBoardName,
  // CreateList,
  // UpdateListName,
  // CreateCard,
  // SearchCards
};
