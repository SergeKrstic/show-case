/*
 * Keyboard shortcuts
 *
 * Avoid:
 *   - Must avoid: native browser and operation system shortcuts that affect the browser behaviour
 *      (not the contents of the web page), like Ctrl+N, Ctrl+O, Ctrl+S, Ctrl+P, Ctrl+W, etc.
 *   - Should avoid: native browser shortcuts for the page content, like Ctrl+C, Ctrl+Z, Ctrl+F, spacebar etc.
 *
 * Use:
 *  - Letters only shortcuts
 *    - one letter shortcuts for most common actions
 *    - two letter shortcuts for less common actions
 *    - avoid multiple modifiers Ctrl+Alt+p (or was it Alt+Shift+p?)
 *    - don't use both one and two letter shortcuts if they start with the same letter
 *
 * Common shortcuts
 *  - Ctrl+C/V/X/D - copy/paste/cut/duplicate
 *  - Ctrl+Z - undo
 *  - Ctrl+A - select all
 *  - Ctrl+B/I/U, etc for text formatting
 *  - ? - keyboard cheat sheet
 *  - / - set focus to the search field
 *  - up/down arrow keys (also j/k) - next/previous item
 *  - left/right arrow keys - collapse/expand tree nodes
 *  - Tab/Shift tab - indent/unindent for hierarchy (also focus in the form elements)
 *  - ESC - close any pop-up/dialog window
 *  - Ctrl+Enter - submit form
 *
 * Discoverability:
 *  - divide the keyboard cheat sheet window into sections (by context, action type, etc.)
 *      and show each section on a tab
 *  - Mention shortcuts in the menus
 *  - In tooltips on links and buttons
 *  - Hints in the dialog windows
 *  - Context-aware hints in the bottom bar
 *
 * Summary
 *  - Don’t override native browser (or OS) shortcuts.
 *  - Support standard shortcuts that don’t contradict the previous rule, and use one or two letter shortcuts for other actions.
 *  - Always have a consistent system.
 *  - Pay maximum attention to discoverability.
 *
 * source: https://medium.com/@sashika/j-k-or-how-to-choose-keyboard-shortcuts-for-web-applications-a7c3b7b408ee
 *
 * SUPPORTED KEYS:
 *  - For modifier keys you can use 'shift', 'ctrl', 'alt', or 'meta'.
 *  - You can substitute 'option' for 'alt' and 'command' for 'meta'.
 *  - Any other key you should be able to reference by name like 'a', '/', '$', '*', or '='.
 *  - Combination of keys: 'command+t'
 *  - Sequence of keys: 'g o command+enter'
 *  - Other special keys are:
 *    - backspace
 *    - tab
 *    - enter
 *    - return
 *    - capslock
 *    - esc
 *    - escape
 *    - space
 *    - pageup
 *    - pagedown
 *    - end
 *    - home
 *    - left
 *    - up
 *    - right
 *    - down
 *    - ins
 *    - del
 *    - plus
 *  - Full list: https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values
 *
 * source: https://craig.is/killing/mice
 *
 * CSS :focus Selector works on the following:
 *  - HTMLInputElement: <input>
 *  - HTMLSelectElement: <select>
 *  - HTMLTextAreaElement: <area>
 *  - HTMLAnchorElement: <a>
 *  - HTMLButtonElement: <button>
 *  - HTMLAreaElement: <textarea>
 *  - HTMLObjectElement: <object>
 *  - Other:
 *      Not every html element would be focusable by default. Such as div, if one wants to
 *      make that div focusable, one has to add tabindex= attribute
 */

export const keyMap = {
  //  SNAP_LEFT: 'command+left',
  //  DELETE_NODE: ['del', 'backspace'],
  OPEN_HEADER_BOARDS_MENU: {
    name: 'Open Header Boards Menu',
    description:
      'Pressing “b” opens the boards menu in the header. You can search for boards and navigate boards with the up and down arrows. Pressing enter with a board selected will open it.',
    action: 'keydown',
    sequence: 'b'
  },
  TOGGLE_LABEL_COLOR: {
    name: 'Toggle Label Color',
    description:
      'Pressing one of the following number keys, will apply or remove that label.',
    sequences: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
  }
};

export const useHandlers = actions => ({
  OPEN_HEADER_BOARDS_MENU: event => {
    actions.boardsMenuActions.openBoardsMenu();
  },
  TOGGLE_LABEL_COLOR: event => {
    const labelColorMap = {
      '1': 'green',
      '2': 'yellow',
      '3': 'orange',
      '4': 'red',
      '5': 'purple',
      '6': 'blue',
      '7': 'sky',
      '8': 'lime',
      '9': 'pink',
      '0': 'black'
    };
    actions.modelsActions.toggleCardLabel({
      labelColor: labelColorMap[event.key]
    });
  }
});

/*
{
  ACTION_NAME: {
    // Optional attributes - only present if you defined them
    name: 'name',
    group: 'group',
    description: 'description',

    // Attributes always present
    sequences: [
      {
        action: 'keydown',
        sequence: 'alt+s'
      },
      // ...
    ]
  },
  // ...
}

Keyboard Shortcuts:

Navigate Cards [← ↓/J ↑/K →]
Pressing the arrow keys will select adjacent cards on a board. Pressing “j” will select the card below the current card. Pressing “k” will select the card above the current card.

// Open Header Boards Menu [B]
// Pressing “b” opens the boards menu in the header. You can search for boards and navigate boards with the up and down arrows. Pressing enter with a board selected will open it.

Focus Search Box [/]
Pressing “/” puts the cursor in the search box in the header.

Archive Card [C]
Pressing “c” will archive a card.

Due Date [D]
Pressing “d” will open the due date picker for a card.

Add Checklist [-]
Pressing “-” will add a checklist to a card.

Quick Edit Mode [E]
If hovering over a card, pressing “e” will open quick edit mode, which lets you quickly edit the title and other card attributes.

Close Menu / Cancel Editing [Esc]
Pressing “esc” will close an open dialog window or pop-over or cancel edits and comments you are composing.

Save Text [Command/Control Enter]
Pressing Control + Enter (Windows) or Command + Enter (Mac) will save any text you are writing. This works when writing or editing comments, editing the card title, list title, description, and other things.

Open Card [Enter]
Pressing “enter” will open the currently selected card. Pressing “shift + enter” while submitting a card will open it immediately after creating it.

Open Card Filter Menu [F]
Use “f” to open the card filter menu. The search by title input is automatically focused.

Label [L]
Pressing “l” opens a pop-over of the available labels. Clicking a label will add or remove it from the card.

// Pressing one of the following number keys, will apply or remove that label.

// Key	Label Color
// [1]	Green
// [2]	Yellow
// [3]	Orange
// [4]	Red
// [5]	Purple
// [6]	Blue
// [7]	Sky
// [8]	Lime
// [9]	Pink
// [0]	Black

Toggle Label Names [;]
Pressing the semicolon key “;” shows or hides the names of labels on a board. You can also click any label on a board to toggle this.

// Add / Remove Members [M]
// Pressing “m” opens the add / remove members menu. Clicking a member’s avatar will assign or unassign that person.

Insert New Card [N]
Pressing “n” opens a pop-over that allows you to add a card after the currently selected card, or in an empty list.

Move Card to Adjacent List [, . < >]
Pressing “,” or “.” will move a card to the bottom of the adjacent left or right list. Pressing the left or right angle brackets (< and >) will move a card to the top of the adjacent left or right list.

My Cards Filter [Q]
Pressing the “q” key toggles the “cards assigned to me” filter.

// Watch [S]
// Pressing “s” will allow you to watch or unwatch a card. Watching a card will notify you of actions related to the card.

// Assign Self [Space]
// Pressing “space” will assign (or unassign) yourself to a card.

Edit Title [T]
If viewing a card, pressing “t” will edit the title. If hovering over a card, pressing “t” will open the card and edit the title.

// Vote [V]
// Pressing “v” will add (or remove) your vote on a card if the Voting Power-Up is enabled.

Toggle Board Menu [W]
Pressing “w” will collapse or expand the board menu, the sidebar on the right.

Clear All Filters [X]
Use “x” to clear all active card filters.

Open Shortcuts Page [?]
Pressing “?” will open the shortcuts page.

// Autocomplete Members [@]
// When writing a comment, you can type “@” plus a member’s name, username, or initials and get a list of matching members. You can navigate that list with the up and down arrows. Pressing enter or tab with a member selected will mention that user in the comment. The mentioned user will get a notification once submitted.

// When adding a new card, you can use the same method to assign members to cards before submitting them.

Autocomplete Labels [#]
When adding a new card, you can type “#” plus the label’s color or title and get a list of matching labels. You can use the up and down arrows to navigate the resulting list. Pressing enter or tab will add the label to the composed card. The labels will be added to the card when you submit.

Autocomplete Position [^]
When adding a new card, you can type “^” plus a list name or position in a list. You can also type “top” or “bottom” to add to the top or bottom of the current list. You can use the up and down arrows to navigate the resulting list. Pressing enter or tab will automatically change the position of the composed card.

Copy Card [Command/Control C/V]
When hovering over a card, pressing Control + C (Windows) or Command + C (Mac) will copy the card to your clipboard. Pasting by pressing Control + V (Windows) or Command + V (Mac) while hovering over a list will copy the card to the list. This will work between different boards.

Move Card [Command/Control X/V]
When hovering over a card, pressing Control + X (Windows) or Command + X (Mac) will copy card to your clipboard. Pasting by pressing Control + V (Windows) or Command + V (Mac) while hovering over a list will move the card to the list. This will work between different boards.
*/
