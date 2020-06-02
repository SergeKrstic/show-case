import React from 'react';

import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import { ToolbarButtonWrapper as ToolbarButton } from './toolbar-button.component';

import { faAmbulance } from './faAmbulance';
import { faChartNetwork } from './faChartNetwork';
import InsertChart from '@material-ui/icons/InsertChart';

const props = {
  text: 'Today',
  onClick: action('onClick')
};

storiesOf('Services|TrelloClone/components/board-view/toolbar', module)
  .addDecorator(withMockStoreProvider)
  .add('button: default', () => <ToolbarButton {...props} />)
  .add('button: bold', () => <ToolbarButton {...props} isBold />)
  .add('button: selected', () => <ToolbarButton {...props} isSelected />)
  .add('button: dark', () => <ToolbarButton {...props} isDark />)
  .add('button: dark and selected', () => (
    <ToolbarButton {...props} isDark isSelected />
  ))
  .add('button: with fa icon', () => (
    <ToolbarButton {...props} text="" icon={faAmbulance} />
  ))
  .add('button: with fa icon and text', () => (
    <ToolbarButton {...props} text="Graph" icon={faChartNetwork} />
  ))
  .add('button: with mui icon and text', () => (
    <ToolbarButton
      {...props}
      text="Board"
      icon={InsertChart}
      iconType="mui"
      isFlippedY
    />
  ));
