import React from 'react';
import ReactMde from 'react-mde';
import Showdown from 'showdown';

import 'react-mde/lib/styles/css/react-mde-all.css';

require('showdown-icon');
require('showdown-youtube');
// var showdownKatex = require('showdown-katex');
// var xssFilter = require('showdown-xss-filter');

const converter = new Showdown.Converter({
  tables: true,
  simplifiedAutoLink: true,
  strikethrough: true,
  tasklists: true,
  emoji: true,
  parseImgDimensions: true,
  openLinksInNewWindow: true,
  excludeTrailingPunctuationFromURLs: true,
  disableForced4SpacesIndentedSublists: true,
  requireSpaceBeforeHeadingText: true,
  simpleLineBreaks: true,
  extensions: [
    // 'icon'
    'youtube'
    // 'showdown-katex'
    // showdownKatex({
    //   displayMode: true,
    //   throwOnError: false,
    //   errorColor: '#ff0000',
    //   delimiters: [
    //     { left: '$', right: '$', display: false },
    //     { left: '~', right: '~', display: false, asciimath: true }
    //   ]
    // })
    // xssFilter
  ]
});

function MarkDownEditor({ text, onChange, selectedTab, onTabChange }) {
  return (
    <div className="container">
      <ReactMde
        value={text}
        onChange={onChange}
        selectedTab={selectedTab}
        onTabChange={onTabChange}
        minEditorHeight={600}
        // textAreaProps={{ style: { backgroundColor: 'red' } }}
        // textAreaProps={{ className: 'temp' }}
        generateMarkdownPreview={markdown =>
          Promise.resolve(converter.makeHtml(markdown))
        }
      />
    </div>
  );
}

export default MarkDownEditor;

/*
Showdown.getDefaultOptions:
{
  "omitExtraWLInCodeBlocks": false,
  "noHeaderId": false,
  "prefixHeaderId": false,
  "rawPrefixHeaderId": false,
  "ghCompatibleHeaderId": false,
  "rawHeaderId": false,
  "headerLevelStart": false,
  "parseImgDimensions": false,
  "simplifiedAutoLink": false,
  "excludeTrailingPunctuationFromURLs": false,
  "literalMidWordUnderscores": false,
  "literalMidWordAsterisks": false,
  "strikethrough": false,
  "tables": false,
  "tablesHeaderId": false,
  "ghCodeBlocks": true,
  "tasklists": false,
  "smoothLivePreview": false,
  "smartIndentationFix": false,
  "disableForced4SpacesIndentedSublists": false,
  "simpleLineBreaks": false,
  "requireSpaceBeforeHeadingText": false,
  "ghMentions": false,
  "ghMentionsLink": "https://github.com/{u}",
  "encodeEmails": true,
  "openLinksInNewWindow": false,
  "backslashEscapesHTMLTags": false,
  "emoji": false,
  "underline": false,
  "completeHTMLDocument": false,
  "metadata": false,
  "splitAdjacentBlockquotes": false
}
*/
