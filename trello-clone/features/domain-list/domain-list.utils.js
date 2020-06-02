export const buildDomainListData = (domains, boards, filterText) => {
  const domainList = [];

  if (filterText) {
    const filteredBoards = filterBoards(boards, filterText);
    domainList.push({
      domainName: '',
      iconName: 'domain',
      isStarIconVisible: false,
      isDomainNameVisible: false,
      isCreateBoardVisible: false,
      boards: sortAlphabetically(filteredBoards)
    });
    return domainList;
  }

  // 1. Build Focus boards list
  domainList.push({
    domainName: 'Focus Boards',
    iconName: 'focus',
    isStarIconVisible: false,
    isDomainNameVisible: false,
    isCreateBoardVisible: false,
    boards: [
      boards.find(board => board.name === 'Today'),
      boards.find(board => board.name === 'Next')
    ]
  });

  // 2. Build Starred boards list
  const starredBoards = boards.filter(board => board.isStarred === true);
  domainList.push({
    domainName: 'Starred Boards',
    iconName: 'star',
    isStarIconVisible: true,
    isDomainNameVisible: true,
    isCreateBoardVisible: false,
    boards: sortAlphabetically(starredBoards)
  });

  // 3. Build remain domain boards list
  const sortedDomains = sortAlphabetically(domains);
  sortedDomains.forEach(domain => {
    if (domain.name !== 'Focus') {
      const filteredBoards = boards.filter(
        board => board.domainId === domain.id
      );
      domainList.push({
        domainId: domain.id,
        domainName: domain.name,
        iconName: 'domain',
        isStarIconVisible: true,
        isDomainNameVisible: false,
        isCreateBoardVisible: true,
        boards: sortAlphabetically(filteredBoards)
      });
    }
  });

  // 4. Return the data structure
  return domainList;
};

const filterBoards = (boards, filterText) => {
  return boards.filter(board =>
    board.name.toLowerCase().includes(filterText.toLowerCase())
  );
};

const sortAlphabetically = array => {
  return array.sort((a, b) => {
    var x = a.name.toLowerCase();
    var y = b.name.toLowerCase();
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
  });
};
