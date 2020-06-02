import { createSelector } from 'reselect';

export const selectDomainsMap = state => {
  return state.entities.domains.items;
};

export const selectDomains = createSelector(
  // inputs
  selectDomainsMap,
  // result
  domains => Object.keys(domains).map(id => domains[id])
);

export const selectDomain = (state, id) => {
  let domains = selectDomainsMap(state);
  return domains[id];
};
