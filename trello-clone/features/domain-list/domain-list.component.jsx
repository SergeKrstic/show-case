import React from 'react';
import PropTypes from 'prop-types';

import Domain from './domain/domain.container';
import { buildDomainListData } from './domain-list.utils';

import useDomainListStyles from './domain-list.styles';

const DomainList = ({
  mode,
  domains,
  boards,
  boardFilterText,
  modelsActions
}) => {
  const classes = useDomainListStyles();
  const domainList = buildDomainListData(domains, boards, boardFilterText);

  const renderCreateDomain = () => {
    if (mode === 'list') return null;
    return (
      <div className={classes.domainButton} onClick={handleCreateDomain}>
        Create new domain
      </div>
    );
  };

  const handleCreateDomain = () => {
    const domainName = prompt('Add a new domain:');
    if (domainName) modelsActions.addDomain({ name: domainName.trim() });
  };

  return (
    <div>
      {domainList.map((item, index) => (
        <Domain key={index} mode={mode} {...item} />
      ))}
      {renderCreateDomain()}
    </div>
  );
};

DomainList.propTypes = {
  mode: PropTypes.oneOf(['grid', 'list']),
  domains: PropTypes.array.isRequired,
  boards: PropTypes.array.isRequired,
  boardFilterText: PropTypes.string
};

export default DomainList;
