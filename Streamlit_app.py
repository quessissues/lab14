import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Danilc apps')

st.text("Hello, this is my app.")

st.write("This is a Streamlit app used to demonstrate interactive widgets and plots!")

user_input = st.text_input("Please enter your name")

if user_input:
    st.write(f"Hello, {user_input}! Welcome to the Streamlit app.")

number = st.slider("Select a number", 0, 100, 25)
st.write(f"You selected: {number}")

data = pd.DataFrame(
    np.random.randn(50, 2), 
    columns=['A', 'B']
)

<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>lab12</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>




<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .pm { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation.Marker */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>



<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/*
 * Webkit scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-corner {
  background: var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-thumb {
  background: rgb(var(--jp-scrollbar-thumb-color));
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-right: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-bottom: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar */

[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-corner,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-corner {
  background-color: transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-thumb,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid transparent;
  border-right: var(--jp-scrollbar-endpad) solid transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid transparent;
  border-bottom: var(--jp-scrollbar-endpad) solid transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0px solid transparent;
  border-right: 0px solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0px solid transparent;
  border-bottom: 0px solid transparent;
}

/*
 * Phosphor
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Widget, /* </DEPRECATED> */
.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}


/* <DEPRECATED> */ .p-Widget.p-mod-hidden, /* </DEPRECATED> */
.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-CommandPalette, /* </DEPRECATED> */
.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-CommandPalette-search, /* </DEPRECATED> */
.lm-CommandPalette-search {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-content, /* </DEPRECATED> */
.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-CommandPalette-header, /* </DEPRECATED> */
.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}


/* <DEPRECATED> */ .p-CommandPalette-item, /* </DEPRECATED> */
.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}


/* <DEPRECATED> */ .p-CommandPalette-itemIcon, /* </DEPRECATED> */
.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemContent, /* </DEPRECATED> */
.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}


/* <DEPRECATED> */ .p-CommandPalette-itemShortcut, /* </DEPRECATED> */
.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemLabel, /* </DEPRECATED> */
.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
	border:1px solid transparent;
  background-color: transparent;
  position: absolute;
	z-index:1;
	right:3%;
	top: 0;
	bottom: 0;
	margin: auto;
	padding: 7px 0;
	display: none;
	vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
	content: "X";
	display: block;
	width: 15px;
	height: 15px;
	text-align: center;
	color:#000;
	font-weight: normal;
	font-size: 12px;
	cursor: pointer;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-DockPanel, /* </DEPRECATED> */
.lm-DockPanel {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-widget, /* </DEPRECATED> */
.lm-DockPanel-widget {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-tabBar, /* </DEPRECATED> */
.lm-DockPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-DockPanel-handle, /* </DEPRECATED> */
.lm-DockPanel-handle {
  z-index: 2;
}


/* <DEPRECATED> */ .p-DockPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-DockPanel-handle:after, /* </DEPRECATED> */
.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}


/* <DEPRECATED> */ .p-DockPanel-overlay, /* </DEPRECATED> */
.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}


/* <DEPRECATED> */ .p-DockPanel-overlay.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Menu, /* </DEPRECATED> */
.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-Menu-content, /* </DEPRECATED> */
.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-Menu-item, /* </DEPRECATED> */
.lm-Menu-item {
  display: table-row;
}


/* <DEPRECATED> */
.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed,
/* </DEPRECATED> */
.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}


/* <DEPRECATED> */
.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon,
/* </DEPRECATED> */
.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}


/* <DEPRECATED> */ .p-Menu-itemLabel, /* </DEPRECATED> */
.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}


/* <DEPRECATED> */ .p-Menu-itemShortcut, /* </DEPRECATED> */
.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-MenuBar, /* </DEPRECATED> */
.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-MenuBar-content, /* </DEPRECATED> */
.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}


/* <DEPRECATED> */ .p--MenuBar-item, /* </DEPRECATED> */
.lm-MenuBar-item {
  box-sizing: border-box;
}


/* <DEPRECATED> */
.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel,
/* </DEPRECATED> */
.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-ScrollBar, /* </DEPRECATED> */
.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-ScrollBar-button, /* </DEPRECATED> */
.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-track, /* </DEPRECATED> */
.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-thumb, /* </DEPRECATED> */
.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-SplitPanel-child, /* </DEPRECATED> */
.lm-SplitPanel-child {
  z-index: 0;
}


/* <DEPRECATED> */ .p-SplitPanel-handle, /* </DEPRECATED> */
.lm-SplitPanel-handle {
  z-index: 1;
}


/* <DEPRECATED> */ .p-SplitPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-SplitPanel-handle:after, /* </DEPRECATED> */
.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabBar, /* </DEPRECATED> */
.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='horizontal'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='vertical'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}


/* <DEPRECATED> */ .p-TabBar-content, /* </DEPRECATED> */
.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='vertical'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


/* <DEPRECATED> */
.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon,
/* </DEPRECATED> */
.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-TabBar-tabLabel, /* </DEPRECATED> */
.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing : border-box;
}


/* <DEPRECATED> */ .p-TabBar-tab.p-mod-hidden, /* </DEPRECATED> */
.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}


.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-TabBar.p-mod-dragging .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing : border-box;
  background: inherit;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabPanel-tabBar, /* </DEPRECATED> */
.lm-TabPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-TabPanel-stackedPanel, /* </DEPRECATED> */
.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

@charset "UTF-8";
html{
  -webkit-box-sizing:border-box;
          box-sizing:border-box; }

*,
*::before,
*::after{
  -webkit-box-sizing:inherit;
          box-sizing:inherit; }

body{
  font-size:14px;
  font-weight:400;
  letter-spacing:0;
  line-height:1.28581;
  text-transform:none;
  color:#182026;
  font-family:-apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", "Icons16", sans-serif; }

p{
  margin-bottom:10px;
  margin-top:0; }

small{
  font-size:12px; }

strong{
  font-weight:600; }

::-moz-selection{
  background:rgba(125, 188, 255, 0.6); }

::selection{
  background:rgba(125, 188, 255, 0.6); }
.bp3-heading{
  color:#182026;
  font-weight:600;
  margin:0 0 10px;
  padding:0; }
  .bp3-dark .bp3-heading{
    color:#f5f8fa; }

h1.bp3-heading, .bp3-running-text h1{
  font-size:36px;
  line-height:40px; }

h2.bp3-heading, .bp3-running-text h2{
  font-size:28px;
  line-height:32px; }

h3.bp3-heading, .bp3-running-text h3{
  font-size:22px;
  line-height:25px; }

h4.bp3-heading, .bp3-running-text h4{
  font-size:18px;
  line-height:21px; }

h5.bp3-heading, .bp3-running-text h5{
  font-size:16px;
  line-height:19px; }

h6.bp3-heading, .bp3-running-text h6{
  font-size:14px;
  line-height:16px; }
.bp3-ui-text{
  font-size:14px;
  font-weight:400;
  letter-spacing:0;
  line-height:1.28581;
  text-transform:none; }

.bp3-monospace-text{
  font-family:monospace;
  text-transform:none; }

.bp3-text-muted{
  color:#5c7080; }
  .bp3-dark .bp3-text-muted{
    color:#a7b6c2; }

.bp3-text-disabled{
  color:rgba(92, 112, 128, 0.6); }
  .bp3-dark .bp3-text-disabled{
    color:rgba(167, 182, 194, 0.6); }

.bp3-text-overflow-ellipsis{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal; }
.bp3-running-text{
  font-size:14px;
  line-height:1.5; }
  .bp3-running-text h1{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h1{
      color:#f5f8fa; }
  .bp3-running-text h2{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h2{
      color:#f5f8fa; }
  .bp3-running-text h3{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h3{
      color:#f5f8fa; }
  .bp3-running-text h4{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h4{
      color:#f5f8fa; }
  .bp3-running-text h5{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h5{
      color:#f5f8fa; }
  .bp3-running-text h6{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h6{
      color:#f5f8fa; }
  .bp3-running-text hr{
    border:none;
    border-bottom:1px solid rgba(16, 22, 26, 0.15);
    margin:20px 0; }
    .bp3-dark .bp3-running-text hr{
      border-color:rgba(255, 255, 255, 0.15); }
  .bp3-running-text p{
    margin:0 0 10px;
    padding:0; }

.bp3-text-large{
  font-size:16px; }

.bp3-text-small{
  font-size:12px; }
a{
  color:#106ba3;
  text-decoration:none; }
  a:hover{
    color:#106ba3;
    cursor:pointer;
    text-decoration:underline; }
  a .bp3-icon, a .bp3-icon-standard, a .bp3-icon-large{
    color:inherit; }
  a code,
  .bp3-dark a code{
    color:inherit; }
  .bp3-dark a,
  .bp3-dark a:hover{
    color:#48aff0; }
    .bp3-dark a .bp3-icon, .bp3-dark a .bp3-icon-standard, .bp3-dark a .bp3-icon-large,
    .bp3-dark a:hover .bp3-icon,
    .bp3-dark a:hover .bp3-icon-standard,
    .bp3-dark a:hover .bp3-icon-large{
      color:inherit; }
.bp3-running-text code, .bp3-code{
  font-family:monospace;
  text-transform:none;
  background:rgba(255, 255, 255, 0.7);
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
  color:#5c7080;
  font-size:smaller;
  padding:2px 5px; }
  .bp3-dark .bp3-running-text code, .bp3-running-text .bp3-dark code, .bp3-dark .bp3-code{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#a7b6c2; }
  .bp3-running-text a > code, a > .bp3-code{
    color:#137cbd; }
    .bp3-dark .bp3-running-text a > code, .bp3-running-text .bp3-dark a > code, .bp3-dark a > .bp3-code{
      color:inherit; }

.bp3-running-text pre, .bp3-code-block{
  font-family:monospace;
  text-transform:none;
  background:rgba(255, 255, 255, 0.7);
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
  color:#182026;
  display:block;
  font-size:13px;
  line-height:1.4;
  margin:10px 0;
  padding:13px 15px 12px;
  word-break:break-all;
  word-wrap:break-word; }
  .bp3-dark .bp3-running-text pre, .bp3-running-text .bp3-dark pre, .bp3-dark .bp3-code-block{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
  .bp3-running-text pre > code, .bp3-code-block > code{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:inherit;
    font-size:inherit;
    padding:0; }

.bp3-running-text kbd, .bp3-key{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#5c7080;
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  font-family:inherit;
  font-size:12px;
  height:24px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  line-height:24px;
  min-width:24px;
  padding:3px 6px;
  vertical-align:middle; }
  .bp3-running-text kbd .bp3-icon, .bp3-key .bp3-icon, .bp3-running-text kbd .bp3-icon-standard, .bp3-key .bp3-icon-standard, .bp3-running-text kbd .bp3-icon-large, .bp3-key .bp3-icon-large{
    margin-right:5px; }
  .bp3-dark .bp3-running-text kbd, .bp3-running-text .bp3-dark kbd, .bp3-dark .bp3-key{
    background:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#a7b6c2; }
.bp3-running-text blockquote, .bp3-blockquote{
  border-left:solid 4px rgba(167, 182, 194, 0.5);
  margin:0 0 10px;
  padding:0 20px; }
  .bp3-dark .bp3-running-text blockquote, .bp3-running-text .bp3-dark blockquote, .bp3-dark .bp3-blockquote{
    border-color:rgba(115, 134, 148, 0.5); }
.bp3-running-text ul,
.bp3-running-text ol, .bp3-list{
  margin:10px 0;
  padding-left:30px; }
  .bp3-running-text ul li:not(:last-child), .bp3-running-text ol li:not(:last-child), .bp3-list li:not(:last-child){
    margin-bottom:5px; }
  .bp3-running-text ul ol, .bp3-running-text ol ol, .bp3-list ol,
  .bp3-running-text ul ul,
  .bp3-running-text ol ul,
  .bp3-list ul{
    margin-top:5px; }

.bp3-list-unstyled{
  list-style:none;
  margin:0;
  padding:0; }
  .bp3-list-unstyled li{
    padding:0; }
.bp3-rtl{
  text-align:right; }

.bp3-dark{
  color:#f5f8fa; }

:focus{
  outline:rgba(19, 124, 189, 0.6) auto 2px;
  outline-offset:2px;
  -moz-outline-radius:6px; }

.bp3-focus-disabled :focus{
  outline:none !important; }
  .bp3-focus-disabled :focus ~ .bp3-control-indicator{
    outline:none !important; }

.bp3-alert{
  max-width:400px;
  padding:20px; }

.bp3-alert-body{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-alert-body .bp3-icon{
    font-size:40px;
    margin-right:20px;
    margin-top:0; }

.bp3-alert-contents{
  word-break:break-word; }

.bp3-alert-footer{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:reverse;
      -ms-flex-direction:row-reverse;
          flex-direction:row-reverse;
  margin-top:10px; }
  .bp3-alert-footer .bp3-button{
    margin-left:10px; }
.bp3-breadcrumbs{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  cursor:default;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:wrap;
      flex-wrap:wrap;
  height:30px;
  list-style:none;
  margin:0;
  padding:0; }
  .bp3-breadcrumbs > li{
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex; }
    .bp3-breadcrumbs > li::after{
      background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M10.71 7.29l-4-4a1.003 1.003 0 00-1.42 1.42L8.59 8 5.3 11.29c-.19.18-.3.43-.3.71a1.003 1.003 0 001.71.71l4-4c.18-.18.29-.43.29-.71 0-.28-.11-.53-.29-.71z' fill='%235C7080'/%3e%3c/svg%3e");
      content:"";
      display:block;
      height:16px;
      margin:0 5px;
      width:16px; }
    .bp3-breadcrumbs > li:last-of-type::after{
      display:none; }

.bp3-breadcrumb,
.bp3-breadcrumb-current,
.bp3-breadcrumbs-collapsed{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  font-size:16px; }

.bp3-breadcrumb,
.bp3-breadcrumbs-collapsed{
  color:#5c7080; }

.bp3-breadcrumb:hover{
  text-decoration:none; }

.bp3-breadcrumb.bp3-disabled{
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-breadcrumb .bp3-icon{
  margin-right:5px; }

.bp3-breadcrumb-current{
  color:inherit;
  font-weight:600; }
  .bp3-breadcrumb-current .bp3-input{
    font-size:inherit;
    font-weight:inherit;
    vertical-align:baseline; }

.bp3-breadcrumbs-collapsed{
  background:#ced9e0;
  border:none;
  border-radius:3px;
  cursor:pointer;
  margin-right:2px;
  padding:1px 5px;
  vertical-align:text-bottom; }
  .bp3-breadcrumbs-collapsed::before{
    background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cg fill='%235C7080'%3e%3ccircle cx='2' cy='8.03' r='2'/%3e%3ccircle cx='14' cy='8.03' r='2'/%3e%3ccircle cx='8' cy='8.03' r='2'/%3e%3c/g%3e%3c/svg%3e") center no-repeat;
    content:"";
    display:block;
    height:16px;
    width:16px; }
  .bp3-breadcrumbs-collapsed:hover{
    background:#bfccd6;
    color:#182026;
    text-decoration:none; }

.bp3-dark .bp3-breadcrumb,
.bp3-dark .bp3-breadcrumbs-collapsed{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumbs > li::after{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumb.bp3-disabled{
  color:rgba(167, 182, 194, 0.6); }

.bp3-dark .bp3-breadcrumb-current{
  color:#f5f8fa; }

.bp3-dark .bp3-breadcrumbs-collapsed{
  background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-breadcrumbs-collapsed:hover{
    background:rgba(16, 22, 26, 0.6);
    color:#f5f8fa; }
.bp3-button{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  font-size:14px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  padding:5px 10px;
  text-align:left;
  vertical-align:middle;
  min-height:30px;
  min-width:30px; }
  .bp3-button > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-button > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-button::before,
  .bp3-button > *{
    margin-right:7px; }
  .bp3-button:empty::before,
  .bp3-button > :last-child{
    margin-right:0; }
  .bp3-button:empty{
    padding:0 !important; }
  .bp3-button:disabled, .bp3-button.bp3-disabled{
    cursor:not-allowed; }
  .bp3-button.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button.bp3-align-right,
  .bp3-align-right .bp3-button{
    text-align:right; }
  .bp3-button.bp3-align-left,
  .bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-button:not([class*="bp3-intent-"]){
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    color:#182026; }
    .bp3-button:not([class*="bp3-intent-"]):hover{
      background-clip:padding-box;
      background-color:#ebf1f5;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
    .bp3-button:not([class*="bp3-intent-"]):active, .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      background-color:#d8e1e8;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      outline:none; }
      .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active:hover, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-button.bp3-intent-primary{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover, .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover{
      background-color:#106ba3;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      background-color:#0e5a8a;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-primary:disabled, .bp3-button.bp3-intent-primary.bp3-disabled{
      background-color:rgba(19, 124, 189, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-success{
    background-color:#0f9960;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-success:hover, .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-success:hover{
      background-color:#0d8050;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      background-color:#0a6640;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-success:disabled, .bp3-button.bp3-intent-success.bp3-disabled{
      background-color:rgba(15, 153, 96, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-warning{
    background-color:#d9822b;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover, .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover{
      background-color:#bf7326;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      background-color:#a66321;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-warning:disabled, .bp3-button.bp3-intent-warning.bp3-disabled{
      background-color:rgba(217, 130, 43, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-danger{
    background-color:#db3737;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover, .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover{
      background-color:#c23030;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      background-color:#a82a2a;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-danger:disabled, .bp3-button.bp3-intent-danger.bp3-disabled{
      background-color:rgba(219, 55, 55, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
    stroke:#ffffff; }
  .bp3-button.bp3-large,
  .bp3-large .bp3-button{
    min-height:40px;
    min-width:40px;
    font-size:16px;
    padding:5px 15px; }
    .bp3-button.bp3-large::before,
    .bp3-button.bp3-large > *,
    .bp3-large .bp3-button::before,
    .bp3-large .bp3-button > *{
      margin-right:10px; }
    .bp3-button.bp3-large:empty::before,
    .bp3-button.bp3-large > :last-child,
    .bp3-large .bp3-button:empty::before,
    .bp3-large .bp3-button > :last-child{
      margin-right:0; }
  .bp3-button.bp3-small,
  .bp3-small .bp3-button{
    min-height:24px;
    min-width:24px;
    padding:0 7px; }
  .bp3-button.bp3-loading{
    position:relative; }
    .bp3-button.bp3-loading[class*="bp3-icon-"]::before{
      visibility:hidden; }
    .bp3-button.bp3-loading .bp3-button-spinner{
      margin:0;
      position:absolute; }
    .bp3-button.bp3-loading > :not(.bp3-button-spinner){
      visibility:hidden; }
  .bp3-button[class*="bp3-icon-"]::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    color:#5c7080; }
  .bp3-button .bp3-icon, .bp3-button .bp3-icon-standard, .bp3-button .bp3-icon-large{
    color:#5c7080; }
    .bp3-button .bp3-icon.bp3-align-right, .bp3-button .bp3-icon-standard.bp3-align-right, .bp3-button .bp3-icon-large.bp3-align-right{
      margin-left:7px; }
  .bp3-button .bp3-icon:first-child:last-child,
  .bp3-button .bp3-spinner + .bp3-icon:last-child{
    margin:0 -7px; }
  .bp3-dark .bp3-button:not([class*="bp3-intent-"]){
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover, .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"])[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-large{
      color:#a7b6c2; }
  .bp3-dark .bp3-button[class*="bp3-intent-"]{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:hover{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:active, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-active{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:disabled, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-disabled{
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.3); }
    .bp3-dark .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
      stroke:#8a9ba8; }
  .bp3-button:disabled::before,
  .bp3-button:disabled .bp3-icon, .bp3-button:disabled .bp3-icon-standard, .bp3-button:disabled .bp3-icon-large, .bp3-button.bp3-disabled::before,
  .bp3-button.bp3-disabled .bp3-icon, .bp3-button.bp3-disabled .bp3-icon-standard, .bp3-button.bp3-disabled .bp3-icon-large, .bp3-button[class*="bp3-intent-"]::before,
  .bp3-button[class*="bp3-intent-"] .bp3-icon, .bp3-button[class*="bp3-intent-"] .bp3-icon-standard, .bp3-button[class*="bp3-intent-"] .bp3-icon-large{
    color:inherit !important; }
  .bp3-button.bp3-minimal{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-button.bp3-minimal:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button.bp3-minimal:active, .bp3-button.bp3-minimal.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button.bp3-minimal:disabled, .bp3-button.bp3-minimal:disabled:hover, .bp3-button.bp3-minimal.bp3-disabled, .bp3-button.bp3-minimal.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-minimal{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-minimal:hover, .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button.bp3-minimal:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-minimal:disabled, .bp3-dark .bp3-button.bp3-minimal:disabled:hover, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover, .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover, .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover, .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover, .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button.bp3-outlined{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    border:1px solid rgba(24, 32, 38, 0.2);
    -webkit-box-sizing:border-box;
            box-sizing:border-box; }
    .bp3-button.bp3-outlined:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button.bp3-outlined:active, .bp3-button.bp3-outlined.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button.bp3-outlined:disabled, .bp3-button.bp3-outlined:disabled:hover, .bp3-button.bp3-outlined.bp3-disabled, .bp3-button.bp3-outlined.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button.bp3-outlined:disabled.bp3-active, .bp3-button.bp3-outlined:disabled:hover.bp3-active, .bp3-button.bp3-outlined.bp3-disabled.bp3-active, .bp3-button.bp3-outlined.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-outlined{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-outlined:hover, .bp3-dark .bp3-button.bp3-outlined:active, .bp3-dark .bp3-button.bp3-outlined.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button.bp3-outlined:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-outlined:active, .bp3-dark .bp3-button.bp3-outlined.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-outlined:disabled, .bp3-dark .bp3-button.bp3-outlined:disabled:hover, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button.bp3-outlined:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:hover, .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:hover, .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:hover, .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:hover, .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
    .bp3-button.bp3-outlined:disabled, .bp3-button.bp3-outlined.bp3-disabled, .bp3-button.bp3-outlined:disabled:hover, .bp3-button.bp3-outlined.bp3-disabled:hover{
      border-color:rgba(92, 112, 128, 0.1); }
    .bp3-dark .bp3-button.bp3-outlined{
      border-color:rgba(255, 255, 255, 0.4); }
      .bp3-dark .bp3-button.bp3-outlined:disabled, .bp3-dark .bp3-button.bp3-outlined:disabled:hover, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover{
        border-color:rgba(255, 255, 255, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-primary{
      border-color:rgba(16, 107, 163, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
        border-color:rgba(16, 107, 163, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary{
        border-color:rgba(72, 175, 240, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
          border-color:rgba(72, 175, 240, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-success{
      border-color:rgba(13, 128, 80, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
        border-color:rgba(13, 128, 80, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success{
        border-color:rgba(61, 204, 145, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
          border-color:rgba(61, 204, 145, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-warning{
      border-color:rgba(191, 115, 38, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
        border-color:rgba(191, 115, 38, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning{
        border-color:rgba(255, 179, 102, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
          border-color:rgba(255, 179, 102, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-danger{
      border-color:rgba(194, 48, 48, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
        border-color:rgba(194, 48, 48, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger{
        border-color:rgba(255, 115, 115, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
          border-color:rgba(255, 115, 115, 0.2); }

a.bp3-button{
  text-align:center;
  text-decoration:none;
  -webkit-transition:none;
  transition:none; }
  a.bp3-button, a.bp3-button:hover, a.bp3-button:active{
    color:#182026; }
  a.bp3-button.bp3-disabled{
    color:rgba(92, 112, 128, 0.6); }

.bp3-button-text{
  -webkit-box-flex:0;
      -ms-flex:0 1 auto;
          flex:0 1 auto; }

.bp3-button.bp3-align-left .bp3-button-text, .bp3-button.bp3-align-right .bp3-button-text,
.bp3-button-group.bp3-align-left .bp3-button-text,
.bp3-button-group.bp3-align-right .bp3-button-text{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto; }
.bp3-button-group{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex; }
  .bp3-button-group .bp3-button{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    position:relative;
    z-index:4; }
    .bp3-button-group .bp3-button:focus{
      z-index:5; }
    .bp3-button-group .bp3-button:hover{
      z-index:6; }
    .bp3-button-group .bp3-button:active, .bp3-button-group .bp3-button.bp3-active{
      z-index:7; }
    .bp3-button-group .bp3-button:disabled, .bp3-button-group .bp3-button.bp3-disabled{
      z-index:3; }
    .bp3-button-group .bp3-button[class*="bp3-intent-"]{
      z-index:9; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:focus{
        z-index:10; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:hover{
        z-index:11; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:active, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-active{
        z-index:12; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:disabled, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-disabled{
        z-index:8; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:first-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:first-child){
    border-bottom-left-radius:0;
    border-top-left-radius:0; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    border-bottom-right-radius:0;
    border-top-right-radius:0;
    margin-right:-1px; }
  .bp3-button-group.bp3-minimal .bp3-button{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-button-group.bp3-minimal .bp3-button:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button-group.bp3-minimal .bp3-button{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
      color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
      color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button-group .bp3-popover-wrapper,
  .bp3-button-group .bp3-popover-target{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button-group .bp3-button.bp3-fill,
  .bp3-button-group.bp3-fill .bp3-button:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-vertical{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column;
    vertical-align:top; }
    .bp3-button-group.bp3-vertical.bp3-fill{
      height:100%;
      width:unset; }
    .bp3-button-group.bp3-vertical .bp3-button{
      margin-right:0 !important;
      width:100%; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:first-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:first-child{
      border-radius:3px 3px 0 0; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:last-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:last-child{
      border-radius:0 0 3px 3px; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:not(:last-child){
      margin-bottom:-1px; }
  .bp3-button-group.bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    margin-right:1px; }
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-button:not(:last-child){
    margin-bottom:1px; }
.bp3-callout{
  font-size:14px;
  line-height:1.5;
  background-color:rgba(138, 155, 168, 0.15);
  border-radius:3px;
  padding:10px 12px 9px;
  position:relative;
  width:100%; }
  .bp3-callout[class*="bp3-icon-"]{
    padding-left:40px; }
    .bp3-callout[class*="bp3-icon-"]::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      color:#5c7080;
      left:10px;
      position:absolute;
      top:10px; }
  .bp3-callout.bp3-callout-icon{
    padding-left:40px; }
    .bp3-callout.bp3-callout-icon > .bp3-icon:first-child{
      color:#5c7080;
      left:10px;
      position:absolute;
      top:10px; }
  .bp3-callout .bp3-heading{
    line-height:20px;
    margin-bottom:5px;
    margin-top:0; }
    .bp3-callout .bp3-heading:last-child{
      margin-bottom:0; }
  .bp3-dark .bp3-callout{
    background-color:rgba(138, 155, 168, 0.2); }
    .bp3-dark .bp3-callout[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
  .bp3-callout.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15); }
    .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-primary .bp3-heading{
      color:#106ba3; }
    .bp3-dark .bp3-callout.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-primary .bp3-heading{
        color:#48aff0; }
  .bp3-callout.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15); }
    .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-success .bp3-heading{
      color:#0d8050; }
    .bp3-dark .bp3-callout.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-success .bp3-heading{
        color:#3dcc91; }
  .bp3-callout.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15); }
    .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-warning .bp3-heading{
      color:#bf7326; }
    .bp3-dark .bp3-callout.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-warning .bp3-heading{
        color:#ffb366; }
  .bp3-callout.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15); }
    .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-danger .bp3-heading{
      color:#c23030; }
    .bp3-dark .bp3-callout.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-danger .bp3-heading{
        color:#ff7373; }
  .bp3-running-text .bp3-callout{
    margin:20px 0; }
.bp3-card{
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
  padding:20px;
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-card.bp3-dark,
  .bp3-dark .bp3-card{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-0{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }
  .bp3-elevation-0.bp3-dark,
  .bp3-dark .bp3-elevation-0{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-1{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-1.bp3-dark,
  .bp3-dark .bp3-elevation-1{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-elevation-2{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-2.bp3-dark,
  .bp3-dark .bp3-elevation-2{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4); }

.bp3-elevation-3{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-3.bp3-dark,
  .bp3-dark .bp3-elevation-3{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-elevation-4{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-4.bp3-dark,
  .bp3-dark .bp3-elevation-4{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:hover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  cursor:pointer; }
  .bp3-card.bp3-interactive:hover.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:hover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:active{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  opacity:0.9;
  -webkit-transition-duration:0;
          transition-duration:0; }
  .bp3-card.bp3-interactive:active.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:active{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-collapse{
  height:0;
  overflow-y:hidden;
  -webkit-transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-collapse .bp3-collapse-body{
    -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-collapse .bp3-collapse-body[aria-hidden="true"]{
      display:none; }

.bp3-context-menu .bp3-popover-target{
  display:block; }

.bp3-context-menu-popover-target{
  position:fixed; }

.bp3-divider{
  border-bottom:1px solid rgba(16, 22, 26, 0.15);
  border-right:1px solid rgba(16, 22, 26, 0.15);
  margin:5px; }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-dialog-container{
  opacity:1;
  -webkit-transform:scale(1);
          transform:scale(1);
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  min-height:100%;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none;
  width:100%; }
  .bp3-dialog-container.bp3-overlay-enter > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5); }
  .bp3-dialog-container.bp3-overlay-enter-active > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear-active > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-dialog-container.bp3-overlay-exit > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-dialog-container.bp3-overlay-exit-active > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }

.bp3-dialog{
  background:#ebf1f5;
  border-radius:6px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:30px 0;
  padding-bottom:20px;
  pointer-events:all;
  -webkit-user-select:text;
     -moz-user-select:text;
      -ms-user-select:text;
          user-select:text;
  width:500px; }
  .bp3-dialog:focus{
    outline:0; }
  .bp3-dialog.bp3-dark,
  .bp3-dark .bp3-dialog{
    background:#293742;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }

.bp3-dialog-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background:#ffffff;
  border-radius:6px 6px 0 0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  min-height:40px;
  padding-left:20px;
  padding-right:5px;
  z-index:30; }
  .bp3-dialog-header .bp3-icon-large,
  .bp3-dialog-header .bp3-icon{
    color:#5c7080;
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px; }
  .bp3-dialog-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:inherit;
    margin:0; }
    .bp3-dialog-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-dialog-header{
    background:#30404d;
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-dialog-header .bp3-icon-large,
    .bp3-dark .bp3-dialog-header .bp3-icon{
      color:#a7b6c2; }

.bp3-dialog-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  line-height:18px;
  margin:20px; }

.bp3-dialog-footer{
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  margin:0 20px; }

.bp3-dialog-footer-actions{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:end;
      -ms-flex-pack:end;
          justify-content:flex-end; }
  .bp3-dialog-footer-actions .bp3-button{
    margin-left:10px; }
.bp3-multistep-dialog-panels{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }

.bp3-multistep-dialog-left-panel{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:1;
      -ms-flex:1;
          flex:1;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column; }
  .bp3-dark .bp3-multistep-dialog-left-panel{
    background:#202b33; }

.bp3-multistep-dialog-right-panel{
  background-color:#f5f8fa;
  border-left:1px solid rgba(16, 22, 26, 0.15);
  border-radius:0 0 6px 0;
  -webkit-box-flex:3;
      -ms-flex:3;
          flex:3;
  min-width:0; }
  .bp3-dark .bp3-multistep-dialog-right-panel{
    background-color:#293742;
    border-left:1px solid rgba(16, 22, 26, 0.4); }

.bp3-multistep-dialog-footer{
  background-color:#ffffff;
  border-radius:0 0 6px 0;
  border-top:1px solid rgba(16, 22, 26, 0.15);
  padding:10px; }
  .bp3-dark .bp3-multistep-dialog-footer{
    background:#30404d;
    border-top:1px solid rgba(16, 22, 26, 0.4); }

.bp3-dialog-step-container{
  background-color:#f5f8fa;
  border-bottom:1px solid rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-dialog-step-container{
    background:#293742;
    border-bottom:1px solid rgba(16, 22, 26, 0.4); }
  .bp3-dialog-step-container.bp3-dialog-step-viewed{
    background-color:#ffffff; }
    .bp3-dark .bp3-dialog-step-container.bp3-dialog-step-viewed{
      background:#30404d; }

.bp3-dialog-step{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:#f5f8fa;
  border-radius:6px;
  cursor:not-allowed;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin:4px;
  padding:6px 14px; }
  .bp3-dark .bp3-dialog-step{
    background:#293742; }
  .bp3-dialog-step-viewed .bp3-dialog-step{
    background-color:#ffffff;
    cursor:pointer; }
    .bp3-dark .bp3-dialog-step-viewed .bp3-dialog-step{
      background:#30404d; }
  .bp3-dialog-step:hover{
    background-color:#f5f8fa; }
    .bp3-dark .bp3-dialog-step:hover{
      background:#293742; }

.bp3-dialog-step-icon{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:rgba(92, 112, 128, 0.6);
  border-radius:50%;
  color:#ffffff;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:25px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  width:25px; }
  .bp3-dark .bp3-dialog-step-icon{
    background-color:rgba(167, 182, 194, 0.6); }
  .bp3-active.bp3-dialog-step-viewed .bp3-dialog-step-icon{
    background-color:#2b95d6; }
  .bp3-dialog-step-viewed .bp3-dialog-step-icon{
    background-color:#8a9ba8; }

.bp3-dialog-step-title{
  color:rgba(92, 112, 128, 0.6);
  -webkit-box-flex:1;
      -ms-flex:1;
          flex:1;
  padding-left:10px; }
  .bp3-dark .bp3-dialog-step-title{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-active.bp3-dialog-step-viewed .bp3-dialog-step-title{
    color:#2b95d6; }
  .bp3-dialog-step-viewed:not(.bp3-active) .bp3-dialog-step-title{
    color:#182026; }
    .bp3-dark .bp3-dialog-step-viewed:not(.bp3-active) .bp3-dialog-step-title{
      color:#f5f8fa; }
.bp3-drawer{
  background:#ffffff;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0;
  padding:0; }
  .bp3-drawer:focus{
    outline:0; }
  .bp3-drawer.bp3-position-top{
    height:50%;
    left:0;
    right:0;
    top:0; }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter, .bp3-drawer.bp3-position-top.bp3-overlay-appear{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%); }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter-active, .bp3-drawer.bp3-position-top.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit-active{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-bottom{
    bottom:0;
    height:50%;
    left:0;
    right:0; }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter-active, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-left{
    bottom:0;
    left:0;
    top:0;
    width:50%; }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter, .bp3-drawer.bp3-position-left.bp3-overlay-appear{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%); }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter-active, .bp3-drawer.bp3-position-left.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit-active{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-right{
    bottom:0;
    right:0;
    top:0;
    width:50%; }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter, .bp3-drawer.bp3-position-right.bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter-active, .bp3-drawer.bp3-position-right.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right):not(.bp3-vertical){
    bottom:0;
    right:0;
    top:0;
    width:50%; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right).bp3-vertical{
    bottom:0;
    height:50%;
    left:0;
    right:0; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-dark,
  .bp3-dark .bp3-drawer{
    background:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }

.bp3-drawer-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border-radius:0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  min-height:40px;
  padding:5px;
  padding-left:20px;
  position:relative; }
  .bp3-drawer-header .bp3-icon-large,
  .bp3-drawer-header .bp3-icon{
    color:#5c7080;
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px; }
  .bp3-drawer-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:inherit;
    margin:0; }
    .bp3-drawer-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-drawer-header{
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-drawer-header .bp3-icon-large,
    .bp3-dark .bp3-drawer-header .bp3-icon{
      color:#a7b6c2; }

.bp3-drawer-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  line-height:18px;
  overflow:auto; }

.bp3-drawer-footer{
  -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  padding:10px 20px;
  position:relative; }
  .bp3-dark .bp3-drawer-footer{
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4); }
.bp3-editable-text{
  cursor:text;
  display:inline-block;
  max-width:100%;
  position:relative;
  vertical-align:top;
  white-space:nowrap; }
  .bp3-editable-text::before{
    bottom:-3px;
    left:-3px;
    position:absolute;
    right:-3px;
    top:-3px;
    border-radius:3px;
    content:"";
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-editable-text.bp3-editable-text-editing::before{
    background-color:#ffffff;
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#137cbd; }
  .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4); }
  .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#0f9960; }
  .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4); }
  .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#d9822b; }
  .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4); }
  .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#db3737; }
  .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4); }
  .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15); }
  .bp3-dark .bp3-editable-text.bp3-editable-text-editing::before{
    background-color:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#48aff0; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4);
            box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#3dcc91; }
  .bp3-dark .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4);
            box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#ffb366; }
  .bp3-dark .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4);
            box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#ff7373; }
  .bp3-dark .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4);
            box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-editable-text-input,
.bp3-editable-text-content{
  color:inherit;
  display:inherit;
  font:inherit;
  letter-spacing:inherit;
  max-width:inherit;
  min-width:inherit;
  position:relative;
  resize:none;
  text-transform:inherit;
  vertical-align:top; }

.bp3-editable-text-input{
  background:none;
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0;
  white-space:pre-wrap;
  width:100%; }
  .bp3-editable-text-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input:focus{
    outline:none; }
  .bp3-editable-text-input::-ms-clear{
    display:none; }

.bp3-editable-text-content{
  overflow:hidden;
  padding-right:2px;
  text-overflow:ellipsis;
  white-space:pre; }
  .bp3-editable-text-editing > .bp3-editable-text-content{
    left:0;
    position:absolute;
    visibility:hidden; }
  .bp3-editable-text-placeholder > .bp3-editable-text-content{
    color:rgba(92, 112, 128, 0.6); }
    .bp3-dark .bp3-editable-text-placeholder > .bp3-editable-text-content{
      color:rgba(167, 182, 194, 0.6); }

.bp3-editable-text.bp3-multiline{
  display:block; }
  .bp3-editable-text.bp3-multiline .bp3-editable-text-content{
    overflow:auto;
    white-space:pre-wrap;
    word-wrap:break-word; }
.bp3-divider{
  border-bottom:1px solid rgba(16, 22, 26, 0.15);
  border-right:1px solid rgba(16, 22, 26, 0.15);
  margin:5px; }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-control-group{
  -webkit-transform:translateZ(0);
          transform:translateZ(0);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:stretch;
      -ms-flex-align:stretch;
          align-items:stretch; }
  .bp3-control-group > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select,
  .bp3-control-group .bp3-input,
  .bp3-control-group .bp3-select{
    position:relative; }
  .bp3-control-group .bp3-input{
    border-radius:inherit;
    z-index:2; }
    .bp3-control-group .bp3-input:focus{
      border-radius:3px;
      z-index:14; }
    .bp3-control-group .bp3-input[class*="bp3-intent"]{
      z-index:13; }
      .bp3-control-group .bp3-input[class*="bp3-intent"]:focus{
        z-index:15; }
    .bp3-control-group .bp3-input[readonly], .bp3-control-group .bp3-input:disabled, .bp3-control-group .bp3-input.bp3-disabled{
      z-index:1; }
  .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input{
    z-index:13; }
    .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input:focus{
      z-index:15; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select select,
  .bp3-control-group .bp3-select select{
    -webkit-transform:translateZ(0);
            transform:translateZ(0);
    border-radius:inherit;
    z-index:4; }
    .bp3-control-group .bp3-button:focus,
    .bp3-control-group .bp3-html-select select:focus,
    .bp3-control-group .bp3-select select:focus{
      z-index:5; }
    .bp3-control-group .bp3-button:hover,
    .bp3-control-group .bp3-html-select select:hover,
    .bp3-control-group .bp3-select select:hover{
      z-index:6; }
    .bp3-control-group .bp3-button:active,
    .bp3-control-group .bp3-html-select select:active,
    .bp3-control-group .bp3-select select:active{
      z-index:7; }
    .bp3-control-group .bp3-button[readonly], .bp3-control-group .bp3-button:disabled, .bp3-control-group .bp3-button.bp3-disabled,
    .bp3-control-group .bp3-html-select select[readonly],
    .bp3-control-group .bp3-html-select select:disabled,
    .bp3-control-group .bp3-html-select select.bp3-disabled,
    .bp3-control-group .bp3-select select[readonly],
    .bp3-control-group .bp3-select select:disabled,
    .bp3-control-group .bp3-select select.bp3-disabled{
      z-index:3; }
    .bp3-control-group .bp3-button[class*="bp3-intent"],
    .bp3-control-group .bp3-html-select select[class*="bp3-intent"],
    .bp3-control-group .bp3-select select[class*="bp3-intent"]{
      z-index:9; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:focus{
        z-index:10; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:hover{
        z-index:11; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:active{
        z-index:12; }
      .bp3-control-group .bp3-button[class*="bp3-intent"][readonly], .bp3-control-group .bp3-button[class*="bp3-intent"]:disabled, .bp3-control-group .bp3-button[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"].bp3-disabled{
        z-index:8; }
  .bp3-control-group .bp3-input-group > .bp3-icon,
  .bp3-control-group .bp3-input-group > .bp3-button,
  .bp3-control-group .bp3-input-group > .bp3-input-left-container,
  .bp3-control-group .bp3-input-group > .bp3-input-action{
    z-index:16; }
  .bp3-control-group .bp3-select::after,
  .bp3-control-group .bp3-html-select::after,
  .bp3-control-group .bp3-select > .bp3-icon,
  .bp3-control-group .bp3-html-select > .bp3-icon{
    z-index:17; }
  .bp3-control-group .bp3-select:focus-within{
    z-index:5; }
  .bp3-control-group:not(.bp3-vertical) > *:not(.bp3-divider){
    margin-right:-1px; }
  .bp3-control-group:not(.bp3-vertical) > .bp3-divider:not(:first-child){
    margin-left:6px; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > *:not(.bp3-divider){
    margin-right:0; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > .bp3-button + .bp3-button{
    margin-left:1px; }
  .bp3-control-group .bp3-popover-wrapper,
  .bp3-control-group .bp3-popover-target{
    border-radius:inherit; }
  .bp3-control-group > :first-child{
    border-radius:3px 0 0 3px; }
  .bp3-control-group > :last-child{
    border-radius:0 3px 3px 0;
    margin-right:0; }
  .bp3-control-group > :only-child{
    border-radius:3px;
    margin-right:0; }
  .bp3-control-group .bp3-input-group .bp3-button{
    border-radius:3px; }
  .bp3-control-group .bp3-numeric-input:not(:first-child) .bp3-input-group{
    border-bottom-left-radius:0;
    border-top-left-radius:0; }
  .bp3-control-group.bp3-fill{
    width:100%; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-fill > *:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-vertical{
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-control-group.bp3-vertical > *{
      margin-top:-1px; }
    .bp3-control-group.bp3-vertical > :first-child{
      border-radius:3px 3px 0 0;
      margin-top:0; }
    .bp3-control-group.bp3-vertical > :last-child{
      border-radius:0 0 3px 3px; }
.bp3-control{
  cursor:pointer;
  display:block;
  margin-bottom:10px;
  position:relative;
  text-transform:none; }
  .bp3-control input:checked ~ .bp3-control-indicator{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
  .bp3-control:hover input:checked ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
  .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    background:#0e5a8a;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-control input:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control:hover input:checked ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    background-color:#0e5a8a;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-control:not(.bp3-align-right){
    padding-left:26px; }
    .bp3-control:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-26px; }
  .bp3-control.bp3-align-right{
    padding-right:26px; }
    .bp3-control.bp3-align-right .bp3-control-indicator{
      margin-right:-26px; }
  .bp3-control.bp3-disabled{
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-control.bp3-inline{
    display:inline-block;
    margin-right:20px; }
  .bp3-control input{
    left:0;
    opacity:0;
    position:absolute;
    top:0;
    z-index:-1; }
  .bp3-control .bp3-control-indicator{
    background-clip:padding-box;
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    border:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    cursor:pointer;
    display:inline-block;
    font-size:16px;
    height:1em;
    margin-right:10px;
    margin-top:-3px;
    position:relative;
    -webkit-user-select:none;
       -moz-user-select:none;
        -ms-user-select:none;
            user-select:none;
    vertical-align:middle;
    width:1em; }
    .bp3-control .bp3-control-indicator::before{
      content:"";
      display:block;
      height:1em;
      width:1em; }
  .bp3-control:hover .bp3-control-indicator{
    background-color:#ebf1f5; }
  .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
    background:#d8e1e8;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    cursor:not-allowed; }
  .bp3-control input:focus ~ .bp3-control-indicator{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:2px;
    -moz-outline-radius:6px; }
  .bp3-control.bp3-align-right .bp3-control-indicator{
    float:right;
    margin-left:10px;
    margin-top:1px; }
  .bp3-control.bp3-large{
    font-size:16px; }
    .bp3-control.bp3-large:not(.bp3-align-right){
      padding-left:30px; }
      .bp3-control.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
        margin-left:-30px; }
    .bp3-control.bp3-large.bp3-align-right{
      padding-right:30px; }
      .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
        margin-right:-30px; }
    .bp3-control.bp3-large .bp3-control-indicator{
      font-size:20px; }
    .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-top:0; }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
  .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
  .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    background:#0e5a8a;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    background-color:#0e5a8a;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-control.bp3-checkbox .bp3-control-indicator{
    border-radius:3px; }
  .bp3-control.bp3-checkbox input:checked ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M12 5c-.28 0-.53.11-.71.29L7 9.59l-2.29-2.3a1.003 1.003 0 00-1.42 1.42l3 3c.18.18.43.29.71.29s.53-.11.71-.29l5-5A1.003 1.003 0 0012 5z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M11 7H5c-.55 0-1 .45-1 1s.45 1 1 1h6c.55 0 1-.45 1-1s-.45-1-1-1z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-radio .bp3-control-indicator{
    border-radius:50%; }
  .bp3-control.bp3-radio input:checked ~ .bp3-control-indicator::before{
    background-image:radial-gradient(#ffffff, #ffffff 28%, transparent 32%); }
  .bp3-control.bp3-radio input:checked:disabled ~ .bp3-control-indicator::before{
    opacity:0.5; }
  .bp3-control.bp3-radio input:focus ~ .bp3-control-indicator{
    -moz-outline-radius:16px; }
  .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(167, 182, 194, 0.5); }
  .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(115, 134, 148, 0.5); }
  .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(92, 112, 128, 0.5); }
  .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5); }
    .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5); }
    .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch:not(.bp3-align-right){
    padding-left:38px; }
    .bp3-control.bp3-switch:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-38px; }
  .bp3-control.bp3-switch.bp3-align-right{
    padding-right:38px; }
    .bp3-control.bp3-switch.bp3-align-right .bp3-control-indicator{
      margin-right:-38px; }
  .bp3-control.bp3-switch .bp3-control-indicator{
    border:none;
    border-radius:1.75em;
    -webkit-box-shadow:none !important;
            box-shadow:none !important;
    min-width:1.75em;
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    width:auto; }
    .bp3-control.bp3-switch .bp3-control-indicator::before{
      background:#ffffff;
      border-radius:50%;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
      height:calc(1em - 4px);
      left:0;
      margin:2px;
      position:absolute;
      -webkit-transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      width:calc(1em - 4px); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    left:calc(100% - 1em); }
  .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right){
    padding-left:45px; }
    .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-45px; }
  .bp3-control.bp3-switch.bp3-large.bp3-align-right{
    padding-right:45px; }
    .bp3-control.bp3-switch.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-right:-45px; }
  .bp3-dark .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.7); }
  .bp3-dark .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.9); }
  .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(57, 75, 89, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-dark .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-dark .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch .bp3-control-indicator::before{
    background:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-control.bp3-switch .bp3-switch-inner-text{
    font-size:0.7em;
    text-align:center; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:first-child{
    line-height:0;
    margin-left:0.5em;
    margin-right:1.2em;
    visibility:hidden; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:last-child{
    line-height:1em;
    margin-left:1.2em;
    margin-right:0.5em;
    visibility:visible; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:first-child{
    line-height:1em;
    visibility:visible; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:last-child{
    line-height:0;
    visibility:hidden; }
  .bp3-dark .bp3-control{
    color:#f5f8fa; }
    .bp3-dark .bp3-control.bp3-disabled{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-control .bp3-control-indicator{
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-control:hover .bp3-control-indicator{
      background-color:#30404d; }
    .bp3-dark .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
      background:#202b33;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-control input:disabled ~ .bp3-control-indicator{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      cursor:not-allowed; }
    .bp3-dark .bp3-control.bp3-checkbox input:disabled:checked ~ .bp3-control-indicator, .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
      color:rgba(167, 182, 194, 0.6); }
.bp3-file-input{
  cursor:pointer;
  display:inline-block;
  height:30px;
  position:relative; }
  .bp3-file-input input{
    margin:0;
    min-width:200px;
    opacity:0; }
    .bp3-file-input input:disabled + .bp3-file-upload-input,
    .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
      background:rgba(206, 217, 224, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      resize:none; }
      .bp3-file-input input:disabled + .bp3-file-upload-input::after,
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
        background-color:rgba(206, 217, 224, 0.5);
        background-image:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(92, 112, 128, 0.6);
        cursor:not-allowed;
        outline:none; }
        .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active:hover,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active:hover{
          background:rgba(206, 217, 224, 0.7); }
      .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input, .bp3-dark
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
        background:rgba(57, 75, 89, 0.5);
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after, .bp3-dark
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
          background-color:rgba(57, 75, 89, 0.5);
          background-image:none;
          -webkit-box-shadow:none;
                  box-shadow:none;
          color:rgba(167, 182, 194, 0.6); }
          .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-dark
          .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active{
            background:rgba(57, 75, 89, 0.7); }
  .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#182026; }
  .bp3-dark .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#f5f8fa; }
  .bp3-file-input.bp3-fill{
    width:100%; }
  .bp3-file-input.bp3-large,
  .bp3-large .bp3-file-input{
    height:40px; }
  .bp3-file-input .bp3-file-upload-input-custom-text::after{
    content:attr(bp3-button-text); }

.bp3-file-upload-input{
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  background:#ffffff;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#182026;
  font-size:14px;
  font-weight:400;
  height:30px;
  line-height:30px;
  outline:none;
  padding:0 10px;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  vertical-align:middle;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  color:rgba(92, 112, 128, 0.6);
  left:0;
  padding-right:80px;
  position:absolute;
  right:0;
  top:0;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-file-upload-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input:focus, .bp3-file-upload-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-file-upload-input[type="search"], .bp3-file-upload-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-file-upload-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-file-upload-input:disabled, .bp3-file-upload-input.bp3-disabled{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    resize:none; }
  .bp3-file-upload-input::after{
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    color:#182026;
    min-height:24px;
    min-width:24px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    border-radius:3px;
    content:"Browse";
    line-height:24px;
    margin:3px;
    position:absolute;
    right:0;
    text-align:center;
    top:0;
    width:70px; }
    .bp3-file-upload-input::after:hover{
      background-clip:padding-box;
      background-color:#ebf1f5;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
    .bp3-file-upload-input::after:active, .bp3-file-upload-input::after.bp3-active{
      background-color:#d8e1e8;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-file-upload-input::after:disabled, .bp3-file-upload-input::after.bp3-disabled{
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      outline:none; }
      .bp3-file-upload-input::after:disabled.bp3-active, .bp3-file-upload-input::after:disabled.bp3-active:hover, .bp3-file-upload-input::after.bp3-disabled.bp3-active, .bp3-file-upload-input::after.bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-file-upload-input:hover::after{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-file-upload-input:active::after{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-large .bp3-file-upload-input{
    font-size:16px;
    height:40px;
    line-height:40px;
    padding-right:95px; }
    .bp3-large .bp3-file-upload-input[type="search"], .bp3-large .bp3-file-upload-input.bp3-round{
      padding:0 15px; }
    .bp3-large .bp3-file-upload-input::after{
      min-height:30px;
      min-width:30px;
      line-height:30px;
      margin:5px;
      width:85px; }
  .bp3-dark .bp3-file-upload-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:disabled, .bp3-dark .bp3-file-upload-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::after{
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
      color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover, .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover{
        background-color:#30404d;
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        background-color:#202b33;
        background-image:none;
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
      .bp3-dark .bp3-file-upload-input::after:disabled, .bp3-dark .bp3-file-upload-input::after.bp3-disabled{
        background-color:rgba(57, 75, 89, 0.5);
        background-image:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-upload-input::after:disabled.bp3-active, .bp3-dark .bp3-file-upload-input::after.bp3-disabled.bp3-active{
          background:rgba(57, 75, 89, 0.7); }
      .bp3-dark .bp3-file-upload-input::after .bp3-button-spinner .bp3-spinner-head{
        background:rgba(16, 22, 26, 0.5);
        stroke:#8a9ba8; }
    .bp3-dark .bp3-file-upload-input:hover::after{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:active::after{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
.bp3-file-upload-input::after{
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
.bp3-form-group{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0 0 15px; }
  .bp3-form-group label.bp3-label{
    margin-bottom:5px; }
  .bp3-form-group .bp3-control{
    margin-top:7px; }
  .bp3-form-group .bp3-form-helper-text{
    color:#5c7080;
    font-size:12px;
    margin-top:5px; }
  .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#106ba3; }
  .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#0d8050; }
  .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#bf7326; }
  .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#c23030; }
  .bp3-form-group.bp3-inline{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row; }
    .bp3-form-group.bp3-inline.bp3-large label.bp3-label{
      line-height:40px;
      margin:0 10px 0 0; }
    .bp3-form-group.bp3-inline label.bp3-label{
      line-height:30px;
      margin:0 10px 0 0; }
  .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-dark .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#48aff0; }
  .bp3-dark .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#3dcc91; }
  .bp3-dark .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#ffb366; }
  .bp3-dark .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#ff7373; }
  .bp3-dark .bp3-form-group .bp3-form-helper-text{
    color:#a7b6c2; }
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(167, 182, 194, 0.6) !important; }
.bp3-input-group{
  display:block;
  position:relative; }
  .bp3-input-group .bp3-input{
    position:relative;
    width:100%; }
    .bp3-input-group .bp3-input:not(:first-child){
      padding-left:30px; }
    .bp3-input-group .bp3-input:not(:last-child){
      padding-right:30px; }
  .bp3-input-group .bp3-input-action,
  .bp3-input-group > .bp3-input-left-container,
  .bp3-input-group > .bp3-button,
  .bp3-input-group > .bp3-icon{
    position:absolute;
    top:0; }
    .bp3-input-group .bp3-input-action:first-child,
    .bp3-input-group > .bp3-input-left-container:first-child,
    .bp3-input-group > .bp3-button:first-child,
    .bp3-input-group > .bp3-icon:first-child{
      left:0; }
    .bp3-input-group .bp3-input-action:last-child,
    .bp3-input-group > .bp3-input-left-container:last-child,
    .bp3-input-group > .bp3-button:last-child,
    .bp3-input-group > .bp3-icon:last-child{
      right:0; }
  .bp3-input-group .bp3-button{
    min-height:24px;
    min-width:24px;
    margin:3px;
    padding:0 7px; }
    .bp3-input-group .bp3-button:empty{
      padding:0; }
  .bp3-input-group > .bp3-input-left-container,
  .bp3-input-group > .bp3-icon{
    z-index:1; }
  .bp3-input-group > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group > .bp3-icon{
    color:#5c7080; }
    .bp3-input-group > .bp3-input-left-container > .bp3-icon:empty,
    .bp3-input-group > .bp3-icon:empty{
      font-family:"Icons16", sans-serif;
      font-size:16px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased; }
  .bp3-input-group > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group > .bp3-icon,
  .bp3-input-group .bp3-input-action > .bp3-spinner{
    margin:7px; }
  .bp3-input-group .bp3-tag{
    margin:5px; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus),
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
    color:#5c7080; }
    .bp3-dark .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus), .bp3-dark
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
      color:#a7b6c2; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large{
      color:#5c7080; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled,
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled{
    color:rgba(92, 112, 128, 0.6) !important; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-large{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-input-group.bp3-disabled{
    cursor:not-allowed; }
    .bp3-input-group.bp3-disabled .bp3-icon{
      color:rgba(92, 112, 128, 0.6); }
  .bp3-input-group.bp3-large .bp3-button{
    min-height:30px;
    min-width:30px;
    margin:5px; }
  .bp3-input-group.bp3-large > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group.bp3-large > .bp3-icon,
  .bp3-input-group.bp3-large .bp3-input-action > .bp3-spinner{
    margin:12px; }
  .bp3-input-group.bp3-large .bp3-input{
    font-size:16px;
    height:40px;
    line-height:40px; }
    .bp3-input-group.bp3-large .bp3-input[type="search"], .bp3-input-group.bp3-large .bp3-input.bp3-round{
      padding:0 15px; }
    .bp3-input-group.bp3-large .bp3-input:not(:first-child){
      padding-left:40px; }
    .bp3-input-group.bp3-large .bp3-input:not(:last-child){
      padding-right:40px; }
  .bp3-input-group.bp3-small .bp3-button{
    min-height:20px;
    min-width:20px;
    margin:2px; }
  .bp3-input-group.bp3-small .bp3-tag{
    min-height:20px;
    min-width:20px;
    margin:2px; }
  .bp3-input-group.bp3-small > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group.bp3-small > .bp3-icon,
  .bp3-input-group.bp3-small .bp3-input-action > .bp3-spinner{
    margin:4px; }
  .bp3-input-group.bp3-small .bp3-input{
    font-size:12px;
    height:24px;
    line-height:24px;
    padding-left:8px;
    padding-right:8px; }
    .bp3-input-group.bp3-small .bp3-input[type="search"], .bp3-input-group.bp3-small .bp3-input.bp3-round{
      padding:0 12px; }
    .bp3-input-group.bp3-small .bp3-input:not(:first-child){
      padding-left:24px; }
    .bp3-input-group.bp3-small .bp3-input:not(:last-child){
      padding-right:24px; }
  .bp3-input-group.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-input-group.bp3-round .bp3-button,
  .bp3-input-group.bp3-round .bp3-input,
  .bp3-input-group.bp3-round .bp3-tag{
    border-radius:30px; }
  .bp3-dark .bp3-input-group .bp3-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-input-group.bp3-disabled .bp3-icon{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-input-group.bp3-intent-primary .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input-group.bp3-intent-primary .bp3-input:disabled, .bp3-input-group.bp3-intent-primary .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-primary > .bp3-icon{
    color:#106ba3; }
    .bp3-dark .bp3-input-group.bp3-intent-primary > .bp3-icon{
      color:#48aff0; }
  .bp3-input-group.bp3-intent-success .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input-group.bp3-intent-success .bp3-input:disabled, .bp3-input-group.bp3-intent-success .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-success > .bp3-icon{
    color:#0d8050; }
    .bp3-dark .bp3-input-group.bp3-intent-success > .bp3-icon{
      color:#3dcc91; }
  .bp3-input-group.bp3-intent-warning .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input-group.bp3-intent-warning .bp3-input:disabled, .bp3-input-group.bp3-intent-warning .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-warning > .bp3-icon{
    color:#bf7326; }
    .bp3-dark .bp3-input-group.bp3-intent-warning > .bp3-icon{
      color:#ffb366; }
  .bp3-input-group.bp3-intent-danger .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input-group.bp3-intent-danger .bp3-input:disabled, .bp3-input-group.bp3-intent-danger .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-danger > .bp3-icon{
    color:#c23030; }
    .bp3-dark .bp3-input-group.bp3-intent-danger > .bp3-icon{
      color:#ff7373; }
.bp3-input{
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  background:#ffffff;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#182026;
  font-size:14px;
  font-weight:400;
  height:30px;
  line-height:30px;
  outline:none;
  padding:0 10px;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  vertical-align:middle; }
  .bp3-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input:focus, .bp3-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-input[type="search"], .bp3-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-input:disabled, .bp3-input.bp3-disabled{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    resize:none; }
  .bp3-input.bp3-large{
    font-size:16px;
    height:40px;
    line-height:40px; }
    .bp3-input.bp3-large[type="search"], .bp3-input.bp3-large.bp3-round{
      padding:0 15px; }
  .bp3-input.bp3-small{
    font-size:12px;
    height:24px;
    line-height:24px;
    padding-left:8px;
    padding-right:8px; }
    .bp3-input.bp3-small[type="search"], .bp3-input.bp3-small.bp3-round{
      padding:0 12px; }
  .bp3-input.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-dark .bp3-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input:disabled, .bp3-dark .bp3-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-input.bp3-intent-primary{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input.bp3-intent-primary:disabled, .bp3-input.bp3-intent-primary.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary:focus{
        -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #137cbd;
                box-shadow:inset 0 0 0 1px #137cbd; }
      .bp3-dark .bp3-input.bp3-intent-primary:disabled, .bp3-dark .bp3-input.bp3-intent-primary.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-success{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input.bp3-intent-success:disabled, .bp3-input.bp3-intent-success.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-success{
      -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success:focus{
        -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #0f9960;
                box-shadow:inset 0 0 0 1px #0f9960; }
      .bp3-dark .bp3-input.bp3-intent-success:disabled, .bp3-dark .bp3-input.bp3-intent-success.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-warning{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input.bp3-intent-warning:disabled, .bp3-input.bp3-intent-warning.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning:focus{
        -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #d9822b;
                box-shadow:inset 0 0 0 1px #d9822b; }
      .bp3-dark .bp3-input.bp3-intent-warning:disabled, .bp3-dark .bp3-input.bp3-intent-warning.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-danger{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input.bp3-intent-danger:disabled, .bp3-input.bp3-intent-danger.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger:focus{
        -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #db3737;
                box-shadow:inset 0 0 0 1px #db3737; }
      .bp3-dark .bp3-input.bp3-intent-danger:disabled, .bp3-dark .bp3-input.bp3-intent-danger.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input::-ms-clear{
    display:none; }
textarea.bp3-input{
  max-width:100%;
  padding:10px; }
  textarea.bp3-input, textarea.bp3-input.bp3-large, textarea.bp3-input.bp3-small{
    height:auto;
    line-height:inherit; }
  textarea.bp3-input.bp3-small{
    padding:8px; }
  .bp3-dark textarea.bp3-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark textarea.bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input:disabled, .bp3-dark textarea.bp3-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
label.bp3-label{
  display:block;
  margin-bottom:15px;
  margin-top:0; }
  label.bp3-label .bp3-html-select,
  label.bp3-label .bp3-input,
  label.bp3-label .bp3-select,
  label.bp3-label .bp3-slider,
  label.bp3-label .bp3-popover-wrapper{
    display:block;
    margin-top:5px;
    text-transform:none; }
  label.bp3-label .bp3-button-group{
    margin-top:5px; }
  label.bp3-label .bp3-select select,
  label.bp3-label .bp3-html-select select{
    font-weight:400;
    vertical-align:top;
    width:100%; }
  label.bp3-label.bp3-disabled,
  label.bp3-label.bp3-disabled .bp3-text-muted{
    color:rgba(92, 112, 128, 0.6); }
  label.bp3-label.bp3-inline{
    line-height:30px; }
    label.bp3-label.bp3-inline .bp3-html-select,
    label.bp3-label.bp3-inline .bp3-input,
    label.bp3-label.bp3-inline .bp3-input-group,
    label.bp3-label.bp3-inline .bp3-select,
    label.bp3-label.bp3-inline .bp3-popover-wrapper{
      display:inline-block;
      margin:0 0 0 5px;
      vertical-align:top; }
    label.bp3-label.bp3-inline .bp3-button-group{
      margin:0 0 0 5px; }
    label.bp3-label.bp3-inline .bp3-input-group .bp3-input{
      margin-left:0; }
    label.bp3-label.bp3-inline.bp3-large{
      line-height:40px; }
  label.bp3-label:not(.bp3-inline) .bp3-popover-target{
    display:block; }
  .bp3-dark label.bp3-label{
    color:#f5f8fa; }
    .bp3-dark label.bp3-label.bp3-disabled,
    .bp3-dark label.bp3-label.bp3-disabled .bp3-text-muted{
      color:rgba(167, 182, 194, 0.6); }
.bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button{
  -webkit-box-flex:1;
      -ms-flex:1 1 14px;
          flex:1 1 14px;
  min-height:0;
  padding:0;
  width:30px; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:first-child{
    border-radius:0 3px 0 0; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:last-child{
    border-radius:0 0 3px 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:first-child{
  border-radius:3px 0 0 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:last-child{
  border-radius:0 0 0 3px; }

.bp3-numeric-input.bp3-large .bp3-button-group.bp3-vertical > .bp3-button{
  width:40px; }

form{
  display:block; }
.bp3-html-select select,
.bp3-select select{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  font-size:14px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  padding:5px 10px;
  text-align:left;
  vertical-align:middle;
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  color:#182026;
  -moz-appearance:none;
  -webkit-appearance:none;
  border-radius:3px;
  height:30px;
  padding:0 25px 0 10px;
  width:100%; }
  .bp3-html-select select > *, .bp3-select select > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-html-select select > .bp3-fill, .bp3-select select > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-html-select select::before,
  .bp3-select select::before, .bp3-html-select select > *, .bp3-select select > *{
    margin-right:7px; }
  .bp3-html-select select:empty::before,
  .bp3-select select:empty::before,
  .bp3-html-select select > :last-child,
  .bp3-select select > :last-child{
    margin-right:0; }
  .bp3-html-select select:hover,
  .bp3-select select:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-html-select select:active,
  .bp3-select select:active, .bp3-html-select select.bp3-active,
  .bp3-select select.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-html-select select:disabled,
  .bp3-select select:disabled, .bp3-html-select select.bp3-disabled,
  .bp3-select select.bp3-disabled{
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    outline:none; }
    .bp3-html-select select:disabled.bp3-active,
    .bp3-select select:disabled.bp3-active, .bp3-html-select select:disabled.bp3-active:hover,
    .bp3-select select:disabled.bp3-active:hover, .bp3-html-select select.bp3-disabled.bp3-active,
    .bp3-select select.bp3-disabled.bp3-active, .bp3-html-select select.bp3-disabled.bp3-active:hover,
    .bp3-select select.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }

.bp3-html-select.bp3-minimal select,
.bp3-select.bp3-minimal select{
  background:none;
  -webkit-box-shadow:none;
          box-shadow:none; }
  .bp3-html-select.bp3-minimal select:hover,
  .bp3-select.bp3-minimal select:hover{
    background:rgba(167, 182, 194, 0.3);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:#182026;
    text-decoration:none; }
  .bp3-html-select.bp3-minimal select:active,
  .bp3-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal select.bp3-active,
  .bp3-select.bp3-minimal select.bp3-active{
    background:rgba(115, 134, 148, 0.3);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:#182026; }
  .bp3-html-select.bp3-minimal select:disabled,
  .bp3-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal select:disabled:hover,
  .bp3-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal select.bp3-disabled,
  .bp3-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal select.bp3-disabled:hover,
  .bp3-select.bp3-minimal select.bp3-disabled:hover{
    background:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
    .bp3-html-select.bp3-minimal select:disabled.bp3-active,
    .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active{
      background:rgba(115, 134, 148, 0.3); }
  .bp3-dark .bp3-html-select.bp3-minimal select, .bp3-html-select.bp3-minimal .bp3-dark select,
  .bp3-dark .bp3-select.bp3-minimal select, .bp3-select.bp3-minimal .bp3-dark select{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:inherit; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover, .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover{
      background:rgba(138, 155, 168, 0.15); }
    .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:rgba(138, 155, 168, 0.3);
      color:#f5f8fa; }
    .bp3-dark .bp3-html-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal .bp3-dark select:disabled,
    .bp3-dark .bp3-select.bp3-minimal select:disabled, .bp3-select.bp3-minimal .bp3-dark select:disabled, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select:disabled:hover, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover{
      background:none;
      color:rgba(167, 182, 194, 0.6);
      cursor:not-allowed; }
      .bp3-dark .bp3-html-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active{
        background:rgba(138, 155, 168, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-primary,
  .bp3-select.bp3-minimal select.bp3-intent-primary{
    color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover{
      background:rgba(19, 124, 189, 0.15);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:rgba(19, 124, 189, 0.3);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled{
      background:none;
      color:rgba(16, 107, 163, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active{
        background:rgba(19, 124, 189, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
      stroke:#106ba3; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary{
      color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.2);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(72, 175, 240, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-success,
  .bp3-select.bp3-minimal select.bp3-intent-success{
    color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover{
      background:rgba(15, 153, 96, 0.15);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:rgba(15, 153, 96, 0.3);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled{
      background:none;
      color:rgba(13, 128, 80, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active{
        background:rgba(15, 153, 96, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
      stroke:#0d8050; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success{
      color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.2);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(61, 204, 145, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-warning,
  .bp3-select.bp3-minimal select.bp3-intent-warning{
    color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover{
      background:rgba(217, 130, 43, 0.15);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:rgba(217, 130, 43, 0.3);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled{
      background:none;
      color:rgba(191, 115, 38, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active{
        background:rgba(217, 130, 43, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
      stroke:#bf7326; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning{
      color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.2);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(255, 179, 102, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-danger,
  .bp3-select.bp3-minimal select.bp3-intent-danger{
    color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover{
      background:rgba(219, 55, 55, 0.15);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:rgba(219, 55, 55, 0.3);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled{
      background:none;
      color:rgba(194, 48, 48, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active{
        background:rgba(219, 55, 55, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
      stroke:#c23030; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger{
      color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.2);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(255, 115, 115, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }

.bp3-html-select.bp3-large select,
.bp3-select.bp3-large select{
  font-size:16px;
  height:40px;
  padding-right:35px; }

.bp3-dark .bp3-html-select select, .bp3-dark .bp3-select select{
  background-color:#394b59;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
  color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover, .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    background-color:#202b33;
    background-image:none;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-html-select select:disabled, .bp3-dark .bp3-select select:disabled, .bp3-dark .bp3-html-select select.bp3-disabled, .bp3-dark .bp3-select select.bp3-disabled{
    background-color:rgba(57, 75, 89, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-html-select select:disabled.bp3-active, .bp3-dark .bp3-select select:disabled.bp3-active, .bp3-dark .bp3-html-select select.bp3-disabled.bp3-active, .bp3-dark .bp3-select select.bp3-disabled.bp3-active{
      background:rgba(57, 75, 89, 0.7); }
  .bp3-dark .bp3-html-select select .bp3-button-spinner .bp3-spinner-head, .bp3-dark .bp3-select select .bp3-button-spinner .bp3-spinner-head{
    background:rgba(16, 22, 26, 0.5);
    stroke:#8a9ba8; }

.bp3-html-select select:disabled,
.bp3-select select:disabled{
  background-color:rgba(206, 217, 224, 0.5);
  -webkit-box-shadow:none;
          box-shadow:none;
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-html-select .bp3-icon,
.bp3-select .bp3-icon, .bp3-select::after{
  color:#5c7080;
  pointer-events:none;
  position:absolute;
  right:7px;
  top:7px; }
  .bp3-html-select .bp3-disabled.bp3-icon,
  .bp3-select .bp3-disabled.bp3-icon, .bp3-disabled.bp3-select::after{
    color:rgba(92, 112, 128, 0.6); }
.bp3-html-select,
.bp3-select{
  display:inline-block;
  letter-spacing:normal;
  position:relative;
  vertical-align:middle; }
  .bp3-html-select select::-ms-expand,
  .bp3-select select::-ms-expand{
    display:none; }
  .bp3-html-select .bp3-icon,
  .bp3-select .bp3-icon{
    color:#5c7080; }
    .bp3-html-select .bp3-icon:hover,
    .bp3-select .bp3-icon:hover{
      color:#182026; }
    .bp3-dark .bp3-html-select .bp3-icon, .bp3-dark
    .bp3-select .bp3-icon{
      color:#a7b6c2; }
      .bp3-dark .bp3-html-select .bp3-icon:hover, .bp3-dark
      .bp3-select .bp3-icon:hover{
        color:#f5f8fa; }
  .bp3-html-select.bp3-large::after,
  .bp3-html-select.bp3-large .bp3-icon,
  .bp3-select.bp3-large::after,
  .bp3-select.bp3-large .bp3-icon{
    right:12px;
    top:12px; }
  .bp3-html-select.bp3-fill,
  .bp3-html-select.bp3-fill select,
  .bp3-select.bp3-fill,
  .bp3-select.bp3-fill select{
    width:100%; }
  .bp3-dark .bp3-html-select option, .bp3-dark
  .bp3-select option{
    background-color:#30404d;
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select option:disabled, .bp3-dark
  .bp3-select option:disabled{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-html-select::after, .bp3-dark
  .bp3-select::after{
    color:#a7b6c2; }

.bp3-select::after{
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  content:""; }
.bp3-running-text table, table.bp3-html-table{
  border-spacing:0;
  font-size:14px; }
  .bp3-running-text table th, table.bp3-html-table th,
  .bp3-running-text table td,
  table.bp3-html-table td{
    padding:11px;
    text-align:left;
    vertical-align:top; }
  .bp3-running-text table th, table.bp3-html-table th{
    color:#182026;
    font-weight:600; }
  
  .bp3-running-text table td,
  table.bp3-html-table td{
    color:#182026; }
  .bp3-running-text table tbody tr:first-child th, table.bp3-html-table tbody tr:first-child th,
  .bp3-running-text table tbody tr:first-child td,
  table.bp3-html-table tbody tr:first-child td,
  .bp3-running-text table tfoot tr:first-child th,
  table.bp3-html-table tfoot tr:first-child th,
  .bp3-running-text table tfoot tr:first-child td,
  table.bp3-html-table tfoot tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-running-text table th, .bp3-running-text .bp3-dark table th, .bp3-dark table.bp3-html-table th{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table td, .bp3-running-text .bp3-dark table td, .bp3-dark table.bp3-html-table td{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table tbody tr:first-child th, .bp3-running-text .bp3-dark table tbody tr:first-child th, .bp3-dark table.bp3-html-table tbody tr:first-child th,
  .bp3-dark .bp3-running-text table tbody tr:first-child td,
  .bp3-running-text .bp3-dark table tbody tr:first-child td,
  .bp3-dark table.bp3-html-table tbody tr:first-child td,
  .bp3-dark .bp3-running-text table tfoot tr:first-child th,
  .bp3-running-text .bp3-dark table tfoot tr:first-child th,
  .bp3-dark table.bp3-html-table tfoot tr:first-child th,
  .bp3-dark .bp3-running-text table tfoot tr:first-child td,
  .bp3-running-text .bp3-dark table tfoot tr:first-child td,
  .bp3-dark table.bp3-html-table tfoot tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }

table.bp3-html-table.bp3-html-table-condensed th,
table.bp3-html-table.bp3-html-table-condensed td, table.bp3-html-table.bp3-small th,
table.bp3-html-table.bp3-small td{
  padding-bottom:6px;
  padding-top:6px; }

table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
  background:rgba(191, 204, 214, 0.15); }

table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
  -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered tbody tr td,
table.bp3-html-table.bp3-html-table-bordered tfoot tr td{
  -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child),
  table.bp3-html-table.bp3-html-table-bordered tfoot tr td:not(:first-child){
    -webkit-box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
  -webkit-box-shadow:none;
          box-shadow:none; }
  table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:not(:first-child){
    -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-interactive tbody tr:hover td{
  background-color:rgba(191, 204, 214, 0.3);
  cursor:pointer; }

table.bp3-html-table.bp3-interactive tbody tr:active td{
  background-color:rgba(191, 204, 214, 0.4); }

.bp3-dark table.bp3-html-table{ }
  .bp3-dark table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
    background:rgba(92, 112, 128, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
    -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td,
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered tfoot tr td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child),
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered tfoot tr td:not(:first-child){
      -webkit-box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15);
              box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
    -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:first-child{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-dark table.bp3-html-table.bp3-interactive tbody tr:hover td{
    background-color:rgba(92, 112, 128, 0.3);
    cursor:pointer; }
  .bp3-dark table.bp3-html-table.bp3-interactive tbody tr:active td{
    background-color:rgba(92, 112, 128, 0.4); }

.bp3-key-combo{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center; }
  .bp3-key-combo > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-key-combo > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-key-combo::before,
  .bp3-key-combo > *{
    margin-right:5px; }
  .bp3-key-combo:empty::before,
  .bp3-key-combo > :last-child{
    margin-right:0; }

.bp3-hotkey-dialog{
  padding-bottom:0;
  top:40px; }
  .bp3-hotkey-dialog .bp3-dialog-body{
    margin:0;
    padding:0; }
  .bp3-hotkey-dialog .bp3-hotkey-label{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1; }

.bp3-hotkey-column{
  margin:auto;
  max-height:80vh;
  overflow-y:auto;
  padding:30px; }
  .bp3-hotkey-column .bp3-heading{
    margin-bottom:20px; }
    .bp3-hotkey-column .bp3-heading:not(:first-child){
      margin-top:40px; }

.bp3-hotkey{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:justify;
      -ms-flex-pack:justify;
          justify-content:space-between;
  margin-left:0;
  margin-right:0; }
  .bp3-hotkey:not(:last-child){
    margin-bottom:10px; }
.bp3-icon{
  display:inline-block;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  vertical-align:text-bottom; }
  .bp3-icon:not(:empty)::before{
    content:"" !important;
    content:unset !important; }
  .bp3-icon > svg{
    display:block; }
    .bp3-icon > svg:not([fill]){
      fill:currentColor; }

.bp3-icon.bp3-intent-primary, .bp3-icon-standard.bp3-intent-primary, .bp3-icon-large.bp3-intent-primary{
  color:#106ba3; }
  .bp3-dark .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-icon-large.bp3-intent-primary{
    color:#48aff0; }

.bp3-icon.bp3-intent-success, .bp3-icon-standard.bp3-intent-success, .bp3-icon-large.bp3-intent-success{
  color:#0d8050; }
  .bp3-dark .bp3-icon.bp3-intent-success, .bp3-dark .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-icon-large.bp3-intent-success{
    color:#3dcc91; }

.bp3-icon.bp3-intent-warning, .bp3-icon-standard.bp3-intent-warning, .bp3-icon-large.bp3-intent-warning{
  color:#bf7326; }
  .bp3-dark .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-icon-large.bp3-intent-warning{
    color:#ffb366; }

.bp3-icon.bp3-intent-danger, .bp3-icon-standard.bp3-intent-danger, .bp3-icon-large.bp3-intent-danger{
  color:#c23030; }
  .bp3-dark .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-icon-large.bp3-intent-danger{
    color:#ff7373; }

span.bp3-icon-standard{
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon-large{
  font-family:"Icons20", sans-serif;
  font-size:20px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon:empty{
  font-family:"Icons20";
  font-size:inherit;
  font-style:normal;
  font-weight:400;
  line-height:1; }
  span.bp3-icon:empty::before{
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased; }

.bp3-icon-add::before{
  content:""; }

.bp3-icon-add-column-left::before{
  content:""; }

.bp3-icon-add-column-right::before{
  content:""; }

.bp3-icon-add-row-bottom::before{
  content:""; }

.bp3-icon-add-row-top::before{
  content:""; }

.bp3-icon-add-to-artifact::before{
  content:""; }

.bp3-icon-add-to-folder::before{
  content:""; }

.bp3-icon-airplane::before{
  content:""; }

.bp3-icon-align-center::before{
  content:""; }

.bp3-icon-align-justify::before{
  content:""; }

.bp3-icon-align-left::before{
  content:""; }

.bp3-icon-align-right::before{
  content:""; }

.bp3-icon-alignment-bottom::before{
  content:""; }

.bp3-icon-alignment-horizontal-center::before{
  content:""; }

.bp3-icon-alignment-left::before{
  content:""; }

.bp3-icon-alignment-right::before{
  content:""; }

.bp3-icon-alignment-top::before{
  content:""; }

.bp3-icon-alignment-vertical-center::before{
  content:""; }

.bp3-icon-annotation::before{
  content:""; }

.bp3-icon-application::before{
  content:""; }

.bp3-icon-applications::before{
  content:""; }

.bp3-icon-archive::before{
  content:""; }

.bp3-icon-arrow-bottom-left::before{
  content:"↙"; }

.bp3-icon-arrow-bottom-right::before{
  content:"↘"; }

.bp3-icon-arrow-down::before{
  content:"↓"; }

.bp3-icon-arrow-left::before{
  content:"←"; }

.bp3-icon-arrow-right::before{
  content:"→"; }

.bp3-icon-arrow-top-left::before{
  content:"↖"; }

.bp3-icon-arrow-top-right::before{
  content:"↗"; }

.bp3-icon-arrow-up::before{
  content:"↑"; }

.bp3-icon-arrows-horizontal::before{
  content:"↔"; }

.bp3-icon-arrows-vertical::before{
  content:"↕"; }

.bp3-icon-asterisk::before{
  content:"*"; }

.bp3-icon-automatic-updates::before{
  content:""; }

.bp3-icon-badge::before{
  content:""; }

.bp3-icon-ban-circle::before{
  content:""; }

.bp3-icon-bank-account::before{
  content:""; }

.bp3-icon-barcode::before{
  content:""; }

.bp3-icon-blank::before{
  content:""; }

.bp3-icon-blocked-person::before{
  content:""; }

.bp3-icon-bold::before{
  content:""; }

.bp3-icon-book::before{
  content:""; }

.bp3-icon-bookmark::before{
  content:""; }

.bp3-icon-box::before{
  content:""; }

.bp3-icon-briefcase::before{
  content:""; }

.bp3-icon-bring-data::before{
  content:""; }

.bp3-icon-build::before{
  content:""; }

.bp3-icon-calculator::before{
  content:""; }

.bp3-icon-calendar::before{
  content:""; }

.bp3-icon-camera::before{
  content:""; }

.bp3-icon-caret-down::before{
  content:"⌄"; }

.bp3-icon-caret-left::before{
  content:"〈"; }

.bp3-icon-caret-right::before{
  content:"〉"; }

.bp3-icon-caret-up::before{
  content:"⌃"; }

.bp3-icon-cell-tower::before{
  content:""; }

.bp3-icon-changes::before{
  content:""; }

.bp3-icon-chart::before{
  content:""; }

.bp3-icon-chat::before{
  content:""; }

.bp3-icon-chevron-backward::before{
  content:""; }

.bp3-icon-chevron-down::before{
  content:""; }

.bp3-icon-chevron-forward::before{
  content:""; }

.bp3-icon-chevron-left::before{
  content:""; }

.bp3-icon-chevron-right::before{
  content:""; }

.bp3-icon-chevron-up::before{
  content:""; }

.bp3-icon-circle::before{
  content:""; }

.bp3-icon-circle-arrow-down::before{
  content:""; }

.bp3-icon-circle-arrow-left::before{
  content:""; }

.bp3-icon-circle-arrow-right::before{
  content:""; }

.bp3-icon-circle-arrow-up::before{
  content:""; }

.bp3-icon-citation::before{
  content:""; }

.bp3-icon-clean::before{
  content:""; }

.bp3-icon-clipboard::before{
  content:""; }

.bp3-icon-cloud::before{
  content:"☁"; }

.bp3-icon-cloud-download::before{
  content:""; }

.bp3-icon-cloud-upload::before{
  content:""; }

.bp3-icon-code::before{
  content:""; }

.bp3-icon-code-block::before{
  content:""; }

.bp3-icon-cog::before{
  content:""; }

.bp3-icon-collapse-all::before{
  content:""; }

.bp3-icon-column-layout::before{
  content:""; }

.bp3-icon-comment::before{
  content:""; }

.bp3-icon-comparison::before{
  content:""; }

.bp3-icon-compass::before{
  content:""; }

.bp3-icon-compressed::before{
  content:""; }

.bp3-icon-confirm::before{
  content:""; }

.bp3-icon-console::before{
  content:""; }

.bp3-icon-contrast::before{
  content:""; }

.bp3-icon-control::before{
  content:""; }

.bp3-icon-credit-card::before{
  content:""; }

.bp3-icon-cross::before{
  content:"✗"; }

.bp3-icon-crown::before{
  content:""; }

.bp3-icon-cube::before{
  content:""; }

.bp3-icon-cube-add::before{
  content:""; }

.bp3-icon-cube-remove::before{
  content:""; }

.bp3-icon-curved-range-chart::before{
  content:""; }

.bp3-icon-cut::before{
  content:""; }

.bp3-icon-dashboard::before{
  content:""; }

.bp3-icon-data-lineage::before{
  content:""; }

.bp3-icon-database::before{
  content:""; }

.bp3-icon-delete::before{
  content:""; }

.bp3-icon-delta::before{
  content:"Δ"; }

.bp3-icon-derive-column::before{
  content:""; }

.bp3-icon-desktop::before{
  content:""; }

.bp3-icon-diagnosis::before{
  content:""; }

.bp3-icon-diagram-tree::before{
  content:""; }

.bp3-icon-direction-left::before{
  content:""; }

.bp3-icon-direction-right::before{
  content:""; }

.bp3-icon-disable::before{
  content:""; }

.bp3-icon-document::before{
  content:""; }

.bp3-icon-document-open::before{
  content:""; }

.bp3-icon-document-share::before{
  content:""; }

.bp3-icon-dollar::before{
  content:"$"; }

.bp3-icon-dot::before{
  content:"•"; }

.bp3-icon-double-caret-horizontal::before{
  content:""; }

.bp3-icon-double-caret-vertical::before{
  content:""; }

.bp3-icon-double-chevron-down::before{
  content:""; }

.bp3-icon-double-chevron-left::before{
  content:""; }

.bp3-icon-double-chevron-right::before{
  content:""; }

.bp3-icon-double-chevron-up::before{
  content:""; }

.bp3-icon-doughnut-chart::before{
  content:""; }

.bp3-icon-download::before{
  content:""; }

.bp3-icon-drag-handle-horizontal::before{
  content:""; }

.bp3-icon-drag-handle-vertical::before{
  content:""; }

.bp3-icon-draw::before{
  content:""; }

.bp3-icon-drive-time::before{
  content:""; }

.bp3-icon-duplicate::before{
  content:""; }

.bp3-icon-edit::before{
  content:"✎"; }

.bp3-icon-eject::before{
  content:"⏏"; }

.bp3-icon-endorsed::before{
  content:""; }

.bp3-icon-envelope::before{
  content:"✉"; }

.bp3-icon-equals::before{
  content:""; }

.bp3-icon-eraser::before{
  content:""; }

.bp3-icon-error::before{
  content:""; }

.bp3-icon-euro::before{
  content:"€"; }

.bp3-icon-exchange::before{
  content:""; }

.bp3-icon-exclude-row::before{
  content:""; }

.bp3-icon-expand-all::before{
  content:""; }

.bp3-icon-export::before{
  content:""; }

.bp3-icon-eye-off::before{
  content:""; }

.bp3-icon-eye-on::before{
  content:""; }

.bp3-icon-eye-open::before{
  content:""; }

.bp3-icon-fast-backward::before{
  content:""; }

.bp3-icon-fast-forward::before{
  content:""; }

.bp3-icon-feed::before{
  content:""; }

.bp3-icon-feed-subscribed::before{
  content:""; }

.bp3-icon-film::before{
  content:""; }

.bp3-icon-filter::before{
  content:""; }

.bp3-icon-filter-keep::before{
  content:""; }

.bp3-icon-filter-list::before{
  content:""; }

.bp3-icon-filter-open::before{
  content:""; }

.bp3-icon-filter-remove::before{
  content:""; }

.bp3-icon-flag::before{
  content:"⚑"; }

.bp3-icon-flame::before{
  content:""; }

.bp3-icon-flash::before{
  content:""; }

.bp3-icon-floppy-disk::before{
  content:""; }

.bp3-icon-flow-branch::before{
  content:""; }

.bp3-icon-flow-end::before{
  content:""; }

.bp3-icon-flow-linear::before{
  content:""; }

.bp3-icon-flow-review::before{
  content:""; }

.bp3-icon-flow-review-branch::before{
  content:""; }

.bp3-icon-flows::before{
  content:""; }

.bp3-icon-folder-close::before{
  content:""; }

.bp3-icon-folder-new::before{
  content:""; }

.bp3-icon-folder-open::before{
  content:""; }

.bp3-icon-folder-shared::before{
  content:""; }

.bp3-icon-folder-shared-open::before{
  content:""; }

.bp3-icon-follower::before{
  content:""; }

.bp3-icon-following::before{
  content:""; }

.bp3-icon-font::before{
  content:""; }

.bp3-icon-fork::before{
  content:""; }

.bp3-icon-form::before{
  content:""; }

.bp3-icon-full-circle::before{
  content:""; }

.bp3-icon-full-stacked-chart::before{
  content:""; }

.bp3-icon-fullscreen::before{
  content:""; }

.bp3-icon-function::before{
  content:""; }

.bp3-icon-gantt-chart::before{
  content:""; }

.bp3-icon-geolocation::before{
  content:""; }

.bp3-icon-geosearch::before{
  content:""; }

.bp3-icon-git-branch::before{
  content:""; }

.bp3-icon-git-commit::before{
  content:""; }

.bp3-icon-git-merge::before{
  content:""; }

.bp3-icon-git-new-branch::before{
  content:""; }

.bp3-icon-git-pull::before{
  content:""; }

.bp3-icon-git-push::before{
  content:""; }

.bp3-icon-git-repo::before{
  content:""; }

.bp3-icon-glass::before{
  content:""; }

.bp3-icon-globe::before{
  content:""; }

.bp3-icon-globe-network::before{
  content:""; }

.bp3-icon-graph::before{
  content:""; }

.bp3-icon-graph-remove::before{
  content:""; }

.bp3-icon-greater-than::before{
  content:""; }

.bp3-icon-greater-than-or-equal-to::before{
  content:""; }

.bp3-icon-grid::before{
  content:""; }

.bp3-icon-grid-view::before{
  content:""; }

.bp3-icon-group-objects::before{
  content:""; }

.bp3-icon-grouped-bar-chart::before{
  content:""; }

.bp3-icon-hand::before{
  content:""; }

.bp3-icon-hand-down::before{
  content:""; }

.bp3-icon-hand-left::before{
  content:""; }

.bp3-icon-hand-right::before{
  content:""; }

.bp3-icon-hand-up::before{
  content:""; }

.bp3-icon-header::before{
  content:""; }

.bp3-icon-header-one::before{
  content:""; }

.bp3-icon-header-two::before{
  content:""; }

.bp3-icon-headset::before{
  content:""; }

.bp3-icon-heart::before{
  content:"♥"; }

.bp3-icon-heart-broken::before{
  content:""; }

.bp3-icon-heat-grid::before{
  content:""; }

.bp3-icon-heatmap::before{
  content:""; }

.bp3-icon-help::before{
  content:"?"; }

.bp3-icon-helper-management::before{
  content:""; }

.bp3-icon-highlight::before{
  content:""; }

.bp3-icon-history::before{
  content:""; }

.bp3-icon-home::before{
  content:"⌂"; }

.bp3-icon-horizontal-bar-chart::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-asc::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-desc::before{
  content:""; }

.bp3-icon-horizontal-distribution::before{
  content:""; }

.bp3-icon-id-number::before{
  content:""; }

.bp3-icon-image-rotate-left::before{
  content:""; }

.bp3-icon-image-rotate-right::before{
  content:""; }

.bp3-icon-import::before{
  content:""; }

.bp3-icon-inbox::before{
  content:""; }

.bp3-icon-inbox-filtered::before{
  content:""; }

.bp3-icon-inbox-geo::before{
  content:""; }

.bp3-icon-inbox-search::before{
  content:""; }

.bp3-icon-inbox-update::before{
  content:""; }

.bp3-icon-info-sign::before{
  content:"ℹ"; }

.bp3-icon-inheritance::before{
  content:""; }

.bp3-icon-inner-join::before{
  content:""; }

.bp3-icon-insert::before{
  content:""; }

.bp3-icon-intersection::before{
  content:""; }

.bp3-icon-ip-address::before{
  content:""; }

.bp3-icon-issue::before{
  content:""; }

.bp3-icon-issue-closed::before{
  content:""; }

.bp3-icon-issue-new::before{
  content:""; }

.bp3-icon-italic::before{
  content:""; }

.bp3-icon-join-table::before{
  content:""; }

.bp3-icon-key::before{
  content:""; }

.bp3-icon-key-backspace::before{
  content:""; }

.bp3-icon-key-command::before{
  content:""; }

.bp3-icon-key-control::before{
  content:""; }

.bp3-icon-key-delete::before{
  content:""; }

.bp3-icon-key-enter::before{
  content:""; }

.bp3-icon-key-escape::before{
  content:""; }

.bp3-icon-key-option::before{
  content:""; }

.bp3-icon-key-shift::before{
  content:""; }

.bp3-icon-key-tab::before{
  content:""; }

.bp3-icon-known-vehicle::before{
  content:""; }

.bp3-icon-lab-test::before{
  content:""; }

.bp3-icon-label::before{
  content:""; }

.bp3-icon-layer::before{
  content:""; }

.bp3-icon-layers::before{
  content:""; }

.bp3-icon-layout::before{
  content:""; }

.bp3-icon-layout-auto::before{
  content:""; }

.bp3-icon-layout-balloon::before{
  content:""; }

.bp3-icon-layout-circle::before{
  content:""; }

.bp3-icon-layout-grid::before{
  content:""; }

.bp3-icon-layout-group-by::before{
  content:""; }

.bp3-icon-layout-hierarchy::before{
  content:""; }

.bp3-icon-layout-linear::before{
  content:""; }

.bp3-icon-layout-skew-grid::before{
  content:""; }

.bp3-icon-layout-sorted-clusters::before{
  content:""; }

.bp3-icon-learning::before{
  content:""; }

.bp3-icon-left-join::before{
  content:""; }

.bp3-icon-less-than::before{
  content:""; }

.bp3-icon-less-than-or-equal-to::before{
  content:""; }

.bp3-icon-lifesaver::before{
  content:""; }

.bp3-icon-lightbulb::before{
  content:""; }

.bp3-icon-link::before{
  content:""; }

.bp3-icon-list::before{
  content:"☰"; }

.bp3-icon-list-columns::before{
  content:""; }

.bp3-icon-list-detail-view::before{
  content:""; }

.bp3-icon-locate::before{
  content:""; }

.bp3-icon-lock::before{
  content:""; }

.bp3-icon-log-in::before{
  content:""; }

.bp3-icon-log-out::before{
  content:""; }

.bp3-icon-manual::before{
  content:""; }

.bp3-icon-manually-entered-data::before{
  content:""; }

.bp3-icon-map::before{
  content:""; }

.bp3-icon-map-create::before{
  content:""; }

.bp3-icon-map-marker::before{
  content:""; }

.bp3-icon-maximize::before{
  content:""; }

.bp3-icon-media::before{
  content:""; }

.bp3-icon-menu::before{
  content:""; }

.bp3-icon-menu-closed::before{
  content:""; }

.bp3-icon-menu-open::before{
  content:""; }

.bp3-icon-merge-columns::before{
  content:""; }

.bp3-icon-merge-links::before{
  content:""; }

.bp3-icon-minimize::before{
  content:""; }

.bp3-icon-minus::before{
  content:"−"; }

.bp3-icon-mobile-phone::before{
  content:""; }

.bp3-icon-mobile-video::before{
  content:""; }

.bp3-icon-moon::before{
  content:""; }

.bp3-icon-more::before{
  content:""; }

.bp3-icon-mountain::before{
  content:""; }

.bp3-icon-move::before{
  content:""; }

.bp3-icon-mugshot::before{
  content:""; }

.bp3-icon-multi-select::before{
  content:""; }

.bp3-icon-music::before{
  content:""; }

.bp3-icon-new-drawing::before{
  content:""; }

.bp3-icon-new-grid-item::before{
  content:""; }

.bp3-icon-new-layer::before{
  content:""; }

.bp3-icon-new-layers::before{
  content:""; }

.bp3-icon-new-link::before{
  content:""; }

.bp3-icon-new-object::before{
  content:""; }

.bp3-icon-new-person::before{
  content:""; }

.bp3-icon-new-prescription::before{
  content:""; }

.bp3-icon-new-text-box::before{
  content:""; }

.bp3-icon-ninja::before{
  content:""; }

.bp3-icon-not-equal-to::before{
  content:""; }

.bp3-icon-notifications::before{
  content:""; }

.bp3-icon-notifications-updated::before{
  content:""; }

.bp3-icon-numbered-list::before{
  content:""; }

.bp3-icon-numerical::before{
  content:""; }

.bp3-icon-office::before{
  content:""; }

.bp3-icon-offline::before{
  content:""; }

.bp3-icon-oil-field::before{
  content:""; }

.bp3-icon-one-column::before{
  content:""; }

.bp3-icon-outdated::before{
  content:""; }

.bp3-icon-page-layout::before{
  content:""; }

.bp3-icon-panel-stats::before{
  content:""; }

.bp3-icon-panel-table::before{
  content:""; }

.bp3-icon-paperclip::before{
  content:""; }

.bp3-icon-paragraph::before{
  content:""; }

.bp3-icon-path::before{
  content:""; }

.bp3-icon-path-search::before{
  content:""; }

.bp3-icon-pause::before{
  content:""; }

.bp3-icon-people::before{
  content:""; }

.bp3-icon-percentage::before{
  content:""; }

.bp3-icon-person::before{
  content:""; }

.bp3-icon-phone::before{
  content:"☎"; }

.bp3-icon-pie-chart::before{
  content:""; }

.bp3-icon-pin::before{
  content:""; }

.bp3-icon-pivot::before{
  content:""; }

.bp3-icon-pivot-table::before{
  content:""; }

.bp3-icon-play::before{
  content:""; }

.bp3-icon-plus::before{
  content:"+"; }

.bp3-icon-polygon-filter::before{
  content:""; }

.bp3-icon-power::before{
  content:""; }

.bp3-icon-predictive-analysis::before{
  content:""; }

.bp3-icon-prescription::before{
  content:""; }

.bp3-icon-presentation::before{
  content:""; }

.bp3-icon-print::before{
  content:"⎙"; }

.bp3-icon-projects::before{
  content:""; }

.bp3-icon-properties::before{
  content:""; }

.bp3-icon-property::before{
  content:""; }

.bp3-icon-publish-function::before{
  content:""; }

.bp3-icon-pulse::before{
  content:""; }

.bp3-icon-random::before{
  content:""; }

.bp3-icon-record::before{
  content:""; }

.bp3-icon-redo::before{
  content:""; }

.bp3-icon-refresh::before{
  content:""; }

.bp3-icon-regression-chart::before{
  content:""; }

.bp3-icon-remove::before{
  content:""; }

.bp3-icon-remove-column::before{
  content:""; }

.bp3-icon-remove-column-left::before{
  content:""; }

.bp3-icon-remove-column-right::before{
  content:""; }

.bp3-icon-remove-row-bottom::before{
  content:""; }

.bp3-icon-remove-row-top::before{
  content:""; }

.bp3-icon-repeat::before{
  content:""; }

.bp3-icon-reset::before{
  content:""; }

.bp3-icon-resolve::before{
  content:""; }

.bp3-icon-rig::before{
  content:""; }

.bp3-icon-right-join::before{
  content:""; }

.bp3-icon-ring::before{
  content:""; }

.bp3-icon-rotate-document::before{
  content:""; }

.bp3-icon-rotate-page::before{
  content:""; }

.bp3-icon-satellite::before{
  content:""; }

.bp3-icon-saved::before{
  content:""; }

.bp3-icon-scatter-plot::before{
  content:""; }

.bp3-icon-search::before{
  content:""; }

.bp3-icon-search-around::before{
  content:""; }

.bp3-icon-search-template::before{
  content:""; }

.bp3-icon-search-text::before{
  content:""; }

.bp3-icon-segmented-control::before{
  content:""; }

.bp3-icon-select::before{
  content:""; }

.bp3-icon-selection::before{
  content:"⦿"; }

.bp3-icon-send-to::before{
  content:""; }

.bp3-icon-send-to-graph::before{
  content:""; }

.bp3-icon-send-to-map::before{
  content:""; }

.bp3-icon-series-add::before{
  content:""; }

.bp3-icon-series-configuration::before{
  content:""; }

.bp3-icon-series-derived::before{
  content:""; }

.bp3-icon-series-filtered::before{
  content:""; }

.bp3-icon-series-search::before{
  content:""; }

.bp3-icon-settings::before{
  content:""; }

.bp3-icon-share::before{
  content:""; }

.bp3-icon-shield::before{
  content:""; }

.bp3-icon-shop::before{
  content:""; }

.bp3-icon-shopping-cart::before{
  content:""; }

.bp3-icon-signal-search::before{
  content:""; }

.bp3-icon-sim-card::before{
  content:""; }

.bp3-icon-slash::before{
  content:""; }

.bp3-icon-small-cross::before{
  content:""; }

.bp3-icon-small-minus::before{
  content:""; }

.bp3-icon-small-plus::before{
  content:""; }

.bp3-icon-small-tick::before{
  content:""; }

.bp3-icon-snowflake::before{
  content:""; }

.bp3-icon-social-media::before{
  content:""; }

.bp3-icon-sort::before{
  content:""; }

.bp3-icon-sort-alphabetical::before{
  content:""; }

.bp3-icon-sort-alphabetical-desc::before{
  content:""; }

.bp3-icon-sort-asc::before{
  content:""; }

.bp3-icon-sort-desc::before{
  content:""; }

.bp3-icon-sort-numerical::before{
  content:""; }

.bp3-icon-sort-numerical-desc::before{
  content:""; }

.bp3-icon-split-columns::before{
  content:""; }

.bp3-icon-square::before{
  content:""; }

.bp3-icon-stacked-chart::before{
  content:""; }

.bp3-icon-star::before{
  content:"★"; }

.bp3-icon-star-empty::before{
  content:"☆"; }

.bp3-icon-step-backward::before{
  content:""; }

.bp3-icon-step-chart::before{
  content:""; }

.bp3-icon-step-forward::before{
  content:""; }

.bp3-icon-stop::before{
  content:""; }

.bp3-icon-stopwatch::before{
  content:""; }

.bp3-icon-strikethrough::before{
  content:""; }

.bp3-icon-style::before{
  content:""; }

.bp3-icon-swap-horizontal::before{
  content:""; }

.bp3-icon-swap-vertical::before{
  content:""; }

.bp3-icon-symbol-circle::before{
  content:""; }

.bp3-icon-symbol-cross::before{
  content:""; }

.bp3-icon-symbol-diamond::before{
  content:""; }

.bp3-icon-symbol-square::before{
  content:""; }

.bp3-icon-symbol-triangle-down::before{
  content:""; }

.bp3-icon-symbol-triangle-up::before{
  content:""; }

.bp3-icon-tag::before{
  content:""; }

.bp3-icon-take-action::before{
  content:""; }

.bp3-icon-taxi::before{
  content:""; }

.bp3-icon-text-highlight::before{
  content:""; }

.bp3-icon-th::before{
  content:""; }

.bp3-icon-th-derived::before{
  content:""; }

.bp3-icon-th-disconnect::before{
  content:""; }

.bp3-icon-th-filtered::before{
  content:""; }

.bp3-icon-th-list::before{
  content:""; }

.bp3-icon-thumbs-down::before{
  content:""; }

.bp3-icon-thumbs-up::before{
  content:""; }

.bp3-icon-tick::before{
  content:"✓"; }

.bp3-icon-tick-circle::before{
  content:""; }

.bp3-icon-time::before{
  content:"⏲"; }

.bp3-icon-timeline-area-chart::before{
  content:""; }

.bp3-icon-timeline-bar-chart::before{
  content:""; }

.bp3-icon-timeline-events::before{
  content:""; }

.bp3-icon-timeline-line-chart::before{
  content:""; }

.bp3-icon-tint::before{
  content:""; }

.bp3-icon-torch::before{
  content:""; }

.bp3-icon-tractor::before{
  content:""; }

.bp3-icon-train::before{
  content:""; }

.bp3-icon-translate::before{
  content:""; }

.bp3-icon-trash::before{
  content:""; }

.bp3-icon-tree::before{
  content:""; }

.bp3-icon-trending-down::before{
  content:""; }

.bp3-icon-trending-up::before{
  content:""; }

.bp3-icon-truck::before{
  content:""; }

.bp3-icon-two-columns::before{
  content:""; }

.bp3-icon-unarchive::before{
  content:""; }

.bp3-icon-underline::before{
  content:"⎁"; }

.bp3-icon-undo::before{
  content:"⎌"; }

.bp3-icon-ungroup-objects::before{
  content:""; }

.bp3-icon-unknown-vehicle::before{
  content:""; }

.bp3-icon-unlock::before{
  content:""; }

.bp3-icon-unpin::before{
  content:""; }

.bp3-icon-unresolve::before{
  content:""; }

.bp3-icon-updated::before{
  content:""; }

.bp3-icon-upload::before{
  content:""; }

.bp3-icon-user::before{
  content:""; }

.bp3-icon-variable::before{
  content:""; }

.bp3-icon-vertical-bar-chart-asc::before{
  content:""; }

.bp3-icon-vertical-bar-chart-desc::before{
  content:""; }

.bp3-icon-vertical-distribution::before{
  content:""; }

.bp3-icon-video::before{
  content:""; }

.bp3-icon-volume-down::before{
  content:""; }

.bp3-icon-volume-off::before{
  content:""; }

.bp3-icon-volume-up::before{
  content:""; }

.bp3-icon-walk::before{
  content:""; }

.bp3-icon-warning-sign::before{
  content:""; }

.bp3-icon-waterfall-chart::before{
  content:""; }

.bp3-icon-widget::before{
  content:""; }

.bp3-icon-widget-button::before{
  content:""; }

.bp3-icon-widget-footer::before{
  content:""; }

.bp3-icon-widget-header::before{
  content:""; }

.bp3-icon-wrench::before{
  content:""; }

.bp3-icon-zoom-in::before{
  content:""; }

.bp3-icon-zoom-out::before{
  content:""; }

.bp3-icon-zoom-to-fit::before{
  content:""; }
.bp3-submenu > .bp3-popover-wrapper{
  display:block; }

.bp3-submenu .bp3-popover-target{
  display:block; }
  .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{ }

.bp3-submenu.bp3-popover{
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0 5px; }
  .bp3-submenu.bp3-popover > .bp3-popover-content{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-submenu.bp3-popover, .bp3-submenu.bp3-popover.bp3-dark{
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-dark .bp3-submenu.bp3-popover > .bp3-popover-content, .bp3-submenu.bp3-popover.bp3-dark > .bp3-popover-content{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
.bp3-menu{
  background:#ffffff;
  border-radius:3px;
  color:#182026;
  list-style:none;
  margin:0;
  min-width:180px;
  padding:5px;
  text-align:left; }

.bp3-menu-divider{
  border-top:1px solid rgba(16, 22, 26, 0.15);
  display:block;
  margin:5px; }
  .bp3-dark .bp3-menu-divider{
    border-top-color:rgba(255, 255, 255, 0.15); }

.bp3-menu-item{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  border-radius:2px;
  color:inherit;
  line-height:20px;
  padding:5px 7px;
  text-decoration:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-menu-item > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-menu-item > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-menu-item::before,
  .bp3-menu-item > *{
    margin-right:7px; }
  .bp3-menu-item:empty::before,
  .bp3-menu-item > :last-child{
    margin-right:0; }
  .bp3-menu-item > .bp3-fill{
    word-break:break-word; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    background-color:rgba(167, 182, 194, 0.3);
    cursor:pointer;
    text-decoration:none; }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-dark .bp3-menu-item{
    color:inherit; }
    .bp3-dark .bp3-menu-item:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
      background-color:rgba(138, 155, 168, 0.15);
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-disabled{
      background-color:inherit;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-menu-item.bp3-intent-primary{
    color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-primary::before, .bp3-menu-item.bp3-intent-primary::after,
    .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
      color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary.bp3-active{
      background-color:#137cbd; }
    .bp3-menu-item.bp3-intent-primary:active{
      background-color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary:active, .bp3-menu-item.bp3-intent-primary:active::before, .bp3-menu-item.bp3-intent-primary:active::after,
    .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-menu-item.bp3-intent-primary.bp3-active::after,
    .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-success{
    color:#0d8050; }
    .bp3-menu-item.bp3-intent-success .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-success::before, .bp3-menu-item.bp3-intent-success::after,
    .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
      color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success.bp3-active{
      background-color:#0f9960; }
    .bp3-menu-item.bp3-intent-success:active{
      background-color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-menu-item.bp3-intent-success:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success:active, .bp3-menu-item.bp3-intent-success:active::before, .bp3-menu-item.bp3-intent-success:active::after,
    .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-menu-item.bp3-intent-success.bp3-active::after,
    .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-warning{
    color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-warning::before, .bp3-menu-item.bp3-intent-warning::after,
    .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
      color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning.bp3-active{
      background-color:#d9822b; }
    .bp3-menu-item.bp3-intent-warning:active{
      background-color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning:active, .bp3-menu-item.bp3-intent-warning:active::before, .bp3-menu-item.bp3-intent-warning:active::after,
    .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-menu-item.bp3-intent-warning.bp3-active::after,
    .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-danger{
    color:#c23030; }
    .bp3-menu-item.bp3-intent-danger .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-danger::before, .bp3-menu-item.bp3-intent-danger::after,
    .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
      color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger.bp3-active{
      background-color:#db3737; }
    .bp3-menu-item.bp3-intent-danger:active{
      background-color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger:active, .bp3-menu-item.bp3-intent-danger:active::before, .bp3-menu-item.bp3-intent-danger:active::after,
    .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-menu-item.bp3-intent-danger.bp3-active::after,
    .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    margin-right:7px; }
  .bp3-menu-item::before,
  .bp3-menu-item > .bp3-icon{
    color:#5c7080;
    margin-top:2px; }
  .bp3-menu-item .bp3-menu-item-label{
    color:#5c7080; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    color:inherit; }
  .bp3-menu-item.bp3-active, .bp3-menu-item:active{
    background-color:rgba(115, 134, 148, 0.3); }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit !important;
    color:rgba(92, 112, 128, 0.6) !important;
    cursor:not-allowed !important;
    outline:none !important; }
    .bp3-menu-item.bp3-disabled::before,
    .bp3-menu-item.bp3-disabled > .bp3-icon,
    .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-large .bp3-menu-item{
    font-size:16px;
    line-height:22px;
    padding:9px 7px; }
    .bp3-large .bp3-menu-item .bp3-icon{
      margin-top:3px; }
    .bp3-large .bp3-menu-item::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      margin-right:10px;
      margin-top:1px; }

button.bp3-menu-item{
  background:none;
  border:none;
  text-align:left;
  width:100%; }
.bp3-menu-header{
  border-top:1px solid rgba(16, 22, 26, 0.15);
  display:block;
  margin:5px;
  cursor:default;
  padding-left:2px; }
  .bp3-dark .bp3-menu-header{
    border-top-color:rgba(255, 255, 255, 0.15); }
  .bp3-menu-header:first-of-type{
    border-top:none; }
  .bp3-menu-header > h6{
    color:#182026;
    font-weight:600;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    line-height:17px;
    margin:0;
    padding:10px 7px 0 1px; }
    .bp3-dark .bp3-menu-header > h6{
      color:#f5f8fa; }
  .bp3-menu-header:first-of-type > h6{
    padding-top:0; }
  .bp3-large .bp3-menu-header > h6{
    font-size:18px;
    padding-bottom:5px;
    padding-top:15px; }
  .bp3-large .bp3-menu-header:first-of-type > h6{
    padding-top:0; }

.bp3-dark .bp3-menu{
  background:#30404d;
  color:#f5f8fa; }

.bp3-dark .bp3-menu-item{ }
  .bp3-dark .bp3-menu-item.bp3-intent-primary{
    color:#48aff0; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary::before, .bp3-dark .bp3-menu-item.bp3-intent-primary::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
      color:#48aff0; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active{
      background-color:#137cbd; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:active{
      background-color:#106ba3; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary:active, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-success{
    color:#3dcc91; }
    .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-success::before, .bp3-dark .bp3-menu-item.bp3-intent-success::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
      color:#3dcc91; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active{
      background-color:#0f9960; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:active{
      background-color:#0d8050; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success:active, .bp3-dark .bp3-menu-item.bp3-intent-success:active::before, .bp3-dark .bp3-menu-item.bp3-intent-success:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning{
    color:#ffb366; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning::before, .bp3-dark .bp3-menu-item.bp3-intent-warning::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
      color:#ffb366; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active{
      background-color:#d9822b; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:active{
      background-color:#bf7326; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning:active, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger{
    color:#ff7373; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger::before, .bp3-dark .bp3-menu-item.bp3-intent-danger::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
      color:#ff7373; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active{
      background-color:#db3737; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:active{
      background-color:#c23030; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger:active, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item::before,
  .bp3-dark .bp3-menu-item > .bp3-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-menu-item .bp3-menu-item-label{
    color:#a7b6c2; }
  .bp3-dark .bp3-menu-item.bp3-active, .bp3-dark .bp3-menu-item:active{
    background-color:rgba(138, 155, 168, 0.3); }
  .bp3-dark .bp3-menu-item.bp3-disabled{
    color:rgba(167, 182, 194, 0.6) !important; }
    .bp3-dark .bp3-menu-item.bp3-disabled::before,
    .bp3-dark .bp3-menu-item.bp3-disabled > .bp3-icon,
    .bp3-dark .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
      color:rgba(167, 182, 194, 0.6) !important; }

.bp3-dark .bp3-menu-divider,
.bp3-dark .bp3-menu-header{
  border-color:rgba(255, 255, 255, 0.15); }

.bp3-dark .bp3-menu-header > h6{
  color:#f5f8fa; }

.bp3-label .bp3-menu{
  margin-top:5px; }
.bp3-navbar{
  background-color:#ffffff;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  height:50px;
  padding:0 15px;
  position:relative;
  width:100%;
  z-index:10; }
  .bp3-navbar.bp3-dark,
  .bp3-dark .bp3-navbar{
    background-color:#394b59; }
  .bp3-navbar.bp3-dark{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-navbar{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-navbar.bp3-fixed-top{
    left:0;
    position:fixed;
    right:0;
    top:0; }

.bp3-navbar-heading{
  font-size:16px;
  margin-right:15px; }

.bp3-navbar-group{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:50px; }
  .bp3-navbar-group.bp3-align-left{
    float:left; }
  .bp3-navbar-group.bp3-align-right{
    float:right; }

.bp3-navbar-divider{
  border-left:1px solid rgba(16, 22, 26, 0.15);
  height:20px;
  margin:0 10px; }
  .bp3-dark .bp3-navbar-divider{
    border-left-color:rgba(255, 255, 255, 0.15); }
.bp3-non-ideal-state{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  height:100%;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  text-align:center;
  width:100%; }
  .bp3-non-ideal-state > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-non-ideal-state > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-non-ideal-state::before,
  .bp3-non-ideal-state > *{
    margin-bottom:20px; }
  .bp3-non-ideal-state:empty::before,
  .bp3-non-ideal-state > :last-child{
    margin-bottom:0; }
  .bp3-non-ideal-state > *{
    max-width:400px; }

.bp3-non-ideal-state-visual{
  color:rgba(92, 112, 128, 0.6);
  font-size:60px; }
  .bp3-dark .bp3-non-ideal-state-visual{
    color:rgba(167, 182, 194, 0.6); }

.bp3-overflow-list{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:nowrap;
      flex-wrap:nowrap;
  min-width:0; }

.bp3-overflow-list-spacer{
  -ms-flex-negative:1;
      flex-shrink:1;
  width:1px; }

body.bp3-overlay-open{
  overflow:hidden; }

.bp3-overlay{
  bottom:0;
  left:0;
  position:static;
  right:0;
  top:0;
  z-index:20; }
  .bp3-overlay:not(.bp3-overlay-open){
    pointer-events:none; }
  .bp3-overlay.bp3-overlay-container{
    overflow:hidden;
    position:fixed; }
    .bp3-overlay.bp3-overlay-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-scroll-container{
    overflow:auto;
    position:fixed; }
    .bp3-overlay.bp3-overlay-scroll-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-inline{
    display:inline;
    overflow:visible; }

.bp3-overlay-content{
  position:fixed;
  z-index:20; }
  .bp3-overlay-inline .bp3-overlay-content,
  .bp3-overlay-scroll-container .bp3-overlay-content{
    position:absolute; }

.bp3-overlay-backdrop{
  bottom:0;
  left:0;
  position:fixed;
  right:0;
  top:0;
  opacity:1;
  background-color:rgba(16, 22, 26, 0.7);
  overflow:auto;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none;
  z-index:20; }
  .bp3-overlay-backdrop.bp3-overlay-enter, .bp3-overlay-backdrop.bp3-overlay-appear{
    opacity:0; }
  .bp3-overlay-backdrop.bp3-overlay-enter-active, .bp3-overlay-backdrop.bp3-overlay-appear-active{
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-overlay-backdrop.bp3-overlay-exit{
    opacity:1; }
  .bp3-overlay-backdrop.bp3-overlay-exit-active{
    opacity:0;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-overlay-backdrop:focus{
    outline:none; }
  .bp3-overlay-inline .bp3-overlay-backdrop{
    position:absolute; }
.bp3-panel-stack{
  overflow:hidden;
  position:relative; }

.bp3-panel-stack-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-shadow:0 1px rgba(16, 22, 26, 0.15);
          box-shadow:0 1px rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-negative:0;
      flex-shrink:0;
  height:30px;
  z-index:1; }
  .bp3-dark .bp3-panel-stack-header{
    -webkit-box-shadow:0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 1px rgba(255, 255, 255, 0.15); }
  .bp3-panel-stack-header > span{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1;
            flex:1; }
  .bp3-panel-stack-header .bp3-heading{
    margin:0 5px; }

.bp3-button.bp3-panel-stack-header-back{
  margin-left:5px;
  padding-left:0;
  white-space:nowrap; }
  .bp3-button.bp3-panel-stack-header-back .bp3-icon{
    margin:0 2px; }

.bp3-panel-stack-view{
  bottom:0;
  left:0;
  position:absolute;
  right:0;
  top:0;
  background-color:#ffffff;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin-right:-1px;
  overflow-y:auto;
  z-index:1; }
  .bp3-dark .bp3-panel-stack-view{
    background-color:#30404d; }
  .bp3-panel-stack-view:nth-last-child(n + 4){
    display:none; }

.bp3-panel-stack-push .bp3-panel-stack-enter, .bp3-panel-stack-push .bp3-panel-stack-appear{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0; }

.bp3-panel-stack-push .bp3-panel-stack-enter-active, .bp3-panel-stack-push .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-push .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-push .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-pop .bp3-panel-stack-enter, .bp3-panel-stack-pop .bp3-panel-stack-appear{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0; }

.bp3-panel-stack-pop .bp3-panel-stack-enter-active, .bp3-panel-stack-pop .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-pop .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-pop .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }
.bp3-panel-stack2{
  overflow:hidden;
  position:relative; }

.bp3-panel-stack2-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-shadow:0 1px rgba(16, 22, 26, 0.15);
          box-shadow:0 1px rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-negative:0;
      flex-shrink:0;
  height:30px;
  z-index:1; }
  .bp3-dark .bp3-panel-stack2-header{
    -webkit-box-shadow:0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 1px rgba(255, 255, 255, 0.15); }
  .bp3-panel-stack2-header > span{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1;
            flex:1; }
  .bp3-panel-stack2-header .bp3-heading{
    margin:0 5px; }

.bp3-button.bp3-panel-stack2-header-back{
  margin-left:5px;
  padding-left:0;
  white-space:nowrap; }
  .bp3-button.bp3-panel-stack2-header-back .bp3-icon{
    margin:0 2px; }

.bp3-panel-stack2-view{
  bottom:0;
  left:0;
  position:absolute;
  right:0;
  top:0;
  background-color:#ffffff;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin-right:-1px;
  overflow-y:auto;
  z-index:1; }
  .bp3-dark .bp3-panel-stack2-view{
    background-color:#30404d; }
  .bp3-panel-stack2-view:nth-last-child(n + 4){
    display:none; }

.bp3-panel-stack2-push .bp3-panel-stack2-enter, .bp3-panel-stack2-push .bp3-panel-stack2-appear{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0; }

.bp3-panel-stack2-push .bp3-panel-stack2-enter-active, .bp3-panel-stack2-push .bp3-panel-stack2-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-push .bp3-panel-stack2-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack2-push .bp3-panel-stack2-exit-active{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-pop .bp3-panel-stack2-enter, .bp3-panel-stack2-pop .bp3-panel-stack2-appear{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0; }

.bp3-panel-stack2-pop .bp3-panel-stack2-enter-active, .bp3-panel-stack2-pop .bp3-panel-stack2-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-pop .bp3-panel-stack2-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack2-pop .bp3-panel-stack2-exit-active{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }
.bp3-popover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1);
  border-radius:3px;
  display:inline-block;
  z-index:20; }
  .bp3-popover .bp3-popover-arrow{
    height:30px;
    position:absolute;
    width:30px; }
    .bp3-popover .bp3-popover-arrow::before{
      height:20px;
      margin:5px;
      width:20px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover{
    margin-bottom:17px;
    margin-top:-17px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
      bottom:-11px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover{
    margin-left:17px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
      left:-11px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover{
    margin-top:17px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
      top:-11px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover{
    margin-left:-17px;
    margin-right:17px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
      right:-11px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-popover > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-popover > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
    top:-0.3934px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
    right:-0.3934px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
    left:-0.3934px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
    bottom:-0.3934px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-popover .bp3-popover-content{
    background:#ffffff;
    color:inherit; }
  .bp3-popover .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-popover .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-popover .bp3-popover-arrow-fill{
    fill:#ffffff; }
  .bp3-popover-enter > .bp3-popover, .bp3-popover-appear > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3); }
  .bp3-popover-enter-active > .bp3-popover, .bp3-popover-appear-active > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-popover-exit > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-popover .bp3-popover-content{
    border-radius:3px;
    position:relative; }
  .bp3-popover.bp3-popover-content-sizing .bp3-popover-content{
    max-width:350px;
    padding:20px; }
  .bp3-popover-target + .bp3-overlay .bp3-popover.bp3-popover-content-sizing{
    width:350px; }
  .bp3-popover.bp3-minimal{
    margin:0 !important; }
    .bp3-popover.bp3-minimal .bp3-popover-arrow{
      display:none; }
    .bp3-popover.bp3-minimal.bp3-popover{
      -webkit-transform:scale(1);
              transform:scale(1); }
      .bp3-popover-enter > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-enter-active > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-delay:0;
                transition-delay:0;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
      .bp3-popover-exit > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-exit-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-delay:0;
                transition-delay:0;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-popover.bp3-dark,
  .bp3-dark .bp3-popover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-popover .bp3-popover-content{
      background:#30404d;
      color:inherit; }
    .bp3-popover.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-popover .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-popover .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-popover.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-popover .bp3-popover-arrow-fill{
      fill:#30404d; }

.bp3-popover-arrow::before{
  border-radius:2px;
  content:"";
  display:block;
  position:absolute;
  -webkit-transform:rotate(45deg);
          transform:rotate(45deg); }

.bp3-tether-pinned .bp3-popover-arrow{
  display:none; }

.bp3-popover-backdrop{
  background:rgba(255, 255, 255, 0); }

.bp3-transition-container{
  opacity:1;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  z-index:20; }
  .bp3-transition-container.bp3-popover-enter, .bp3-transition-container.bp3-popover-appear{
    opacity:0; }
  .bp3-transition-container.bp3-popover-enter-active, .bp3-transition-container.bp3-popover-appear-active{
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-transition-container.bp3-popover-exit{
    opacity:1; }
  .bp3-transition-container.bp3-popover-exit-active{
    opacity:0;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-transition-container:focus{
    outline:none; }
  .bp3-transition-container.bp3-popover-leave .bp3-popover-content{
    pointer-events:none; }
  .bp3-transition-container[data-x-out-of-boundaries]{
    display:none; }

span.bp3-popover-target{
  display:inline-block; }

.bp3-popover-wrapper.bp3-fill{
  width:100%; }

.bp3-portal{
  left:0;
  position:absolute;
  right:0;
  top:0; }
@-webkit-keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }
@keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }

.bp3-progress-bar{
  background:rgba(92, 112, 128, 0.2);
  border-radius:40px;
  display:block;
  height:8px;
  overflow:hidden;
  position:relative;
  width:100%; }
  .bp3-progress-bar .bp3-progress-meter{
    background:linear-gradient(-45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%);
    background-color:rgba(92, 112, 128, 0.8);
    background-size:30px 30px;
    border-radius:40px;
    height:100%;
    position:absolute;
    -webkit-transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    width:100%; }
  .bp3-progress-bar:not(.bp3-no-animation):not(.bp3-no-stripes) .bp3-progress-meter{
    animation:linear-progress-bar-stripes 300ms linear infinite reverse; }
  .bp3-progress-bar.bp3-no-stripes .bp3-progress-meter{
    background-image:none; }

.bp3-dark .bp3-progress-bar{
  background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-progress-bar .bp3-progress-meter{
    background-color:#8a9ba8; }

.bp3-progress-bar.bp3-intent-primary .bp3-progress-meter{
  background-color:#137cbd; }

.bp3-progress-bar.bp3-intent-success .bp3-progress-meter{
  background-color:#0f9960; }

.bp3-progress-bar.bp3-intent-warning .bp3-progress-meter{
  background-color:#d9822b; }

.bp3-progress-bar.bp3-intent-danger .bp3-progress-meter{
  background-color:#db3737; }
@-webkit-keyframes skeleton-glow{
  from{
    background:rgba(206, 217, 224, 0.2);
    border-color:rgba(206, 217, 224, 0.2); }
  to{
    background:rgba(92, 112, 128, 0.2);
    border-color:rgba(92, 112, 128, 0.2); } }
@keyframes skeleton-glow{
  from{
    background:rgba(206, 217, 224, 0.2);
    border-color:rgba(206, 217, 224, 0.2); }
  to{
    background:rgba(92, 112, 128, 0.2);
    border-color:rgba(92, 112, 128, 0.2); } }
.bp3-skeleton{
  -webkit-animation:1000ms linear infinite alternate skeleton-glow;
          animation:1000ms linear infinite alternate skeleton-glow;
  background:rgba(206, 217, 224, 0.2);
  background-clip:padding-box !important;
  border-color:rgba(206, 217, 224, 0.2) !important;
  border-radius:2px;
  -webkit-box-shadow:none !important;
          box-shadow:none !important;
  color:transparent !important;
  cursor:default;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-skeleton::before, .bp3-skeleton::after,
  .bp3-skeleton *{
    visibility:hidden !important; }
.bp3-slider{
  height:40px;
  min-width:150px;
  width:100%;
  cursor:default;
  outline:none;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-slider:hover{
    cursor:pointer; }
  .bp3-slider:active{
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-slider.bp3-disabled{
    cursor:not-allowed;
    opacity:0.5; }
  .bp3-slider.bp3-slider-unlabeled{
    height:16px; }

.bp3-slider-track,
.bp3-slider-progress{
  height:6px;
  left:0;
  right:0;
  top:5px;
  position:absolute; }

.bp3-slider-track{
  border-radius:3px;
  overflow:hidden; }

.bp3-slider-progress{
  background:rgba(92, 112, 128, 0.2); }
  .bp3-dark .bp3-slider-progress{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-slider-progress.bp3-intent-primary{
    background-color:#137cbd; }
  .bp3-slider-progress.bp3-intent-success{
    background-color:#0f9960; }
  .bp3-slider-progress.bp3-intent-warning{
    background-color:#d9822b; }
  .bp3-slider-progress.bp3-intent-danger{
    background-color:#db3737; }

.bp3-slider-handle{
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  color:#182026;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
  cursor:pointer;
  height:16px;
  left:0;
  position:absolute;
  top:0;
  width:16px; }
  .bp3-slider-handle:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-slider-handle:active, .bp3-slider-handle.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-slider-handle:disabled, .bp3-slider-handle.bp3-disabled{
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    outline:none; }
    .bp3-slider-handle:disabled.bp3-active, .bp3-slider-handle:disabled.bp3-active:hover, .bp3-slider-handle.bp3-disabled.bp3-active, .bp3-slider-handle.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }
  .bp3-slider-handle:focus{
    z-index:1; }
  .bp3-slider-handle:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
    cursor:-webkit-grab;
    cursor:grab;
    z-index:2; }
  .bp3-slider-handle.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-disabled .bp3-slider-handle{
    background:#bfccd6;
    -webkit-box-shadow:none;
            box-shadow:none;
    pointer-events:none; }
  .bp3-dark .bp3-slider-handle{
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover, .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-slider-handle:disabled, .bp3-dark .bp3-slider-handle.bp3-disabled{
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-slider-handle:disabled.bp3-active, .bp3-dark .bp3-slider-handle.bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-slider-handle .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-slider-handle, .bp3-dark .bp3-slider-handle:hover{
      background-color:#394b59; }
    .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#293742; }
  .bp3-dark .bp3-disabled .bp3-slider-handle{
    background:#5c7080;
    border-color:#5c7080;
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-slider-handle .bp3-slider-label{
    background:#394b59;
    border-radius:3px;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
    color:#f5f8fa;
    margin-left:8px; }
    .bp3-dark .bp3-slider-handle .bp3-slider-label{
      background:#e1e8ed;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
      color:#394b59; }
    .bp3-disabled .bp3-slider-handle .bp3-slider-label{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-slider-handle.bp3-start, .bp3-slider-handle.bp3-end{
    width:8px; }
  .bp3-slider-handle.bp3-start{
    border-bottom-right-radius:0;
    border-top-right-radius:0; }
  .bp3-slider-handle.bp3-end{
    border-bottom-left-radius:0;
    border-top-left-radius:0;
    margin-left:8px; }
    .bp3-slider-handle.bp3-end .bp3-slider-label{
      margin-left:0; }

.bp3-slider-label{
  -webkit-transform:translate(-50%, 20px);
          transform:translate(-50%, 20px);
  display:inline-block;
  font-size:12px;
  line-height:1;
  padding:2px 5px;
  position:absolute;
  vertical-align:top; }

.bp3-slider.bp3-vertical{
  height:150px;
  min-width:40px;
  width:40px; }
  .bp3-slider.bp3-vertical .bp3-slider-track,
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    bottom:0;
    height:auto;
    left:5px;
    top:0;
    width:6px; }
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    top:auto; }
  .bp3-slider.bp3-vertical .bp3-slider-label{
    -webkit-transform:translate(20px, 50%);
            transform:translate(20px, 50%); }
  .bp3-slider.bp3-vertical .bp3-slider-handle{
    top:auto; }
    .bp3-slider.bp3-vertical .bp3-slider-handle .bp3-slider-label{
      margin-left:0;
      margin-top:-8px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end, .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      height:8px;
      margin-left:0;
      width:16px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      border-bottom-right-radius:3px;
      border-top-left-radius:0; }
      .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start .bp3-slider-label{
        -webkit-transform:translate(20px);
                transform:translate(20px); }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end{
      border-bottom-left-radius:0;
      border-bottom-right-radius:0;
      border-top-left-radius:3px;
      margin-bottom:8px; }

@-webkit-keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

@keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

.bp3-spinner{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  overflow:visible;
  vertical-align:middle; }
  .bp3-spinner svg{
    display:block; }
  .bp3-spinner path{
    fill-opacity:0; }
  .bp3-spinner .bp3-spinner-head{
    stroke:rgba(92, 112, 128, 0.8);
    stroke-linecap:round;
    -webkit-transform-origin:center;
            transform-origin:center;
    -webkit-transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-spinner .bp3-spinner-track{
    stroke:rgba(92, 112, 128, 0.2); }

.bp3-spinner-animation{
  -webkit-animation:pt-spinner-animation 500ms linear infinite;
          animation:pt-spinner-animation 500ms linear infinite; }
  .bp3-no-spin > .bp3-spinner-animation{
    -webkit-animation:none;
            animation:none; }

.bp3-dark .bp3-spinner .bp3-spinner-head{
  stroke:#8a9ba8; }

.bp3-dark .bp3-spinner .bp3-spinner-track{
  stroke:rgba(16, 22, 26, 0.5); }

.bp3-spinner.bp3-intent-primary .bp3-spinner-head{
  stroke:#137cbd; }

.bp3-spinner.bp3-intent-success .bp3-spinner-head{
  stroke:#0f9960; }

.bp3-spinner.bp3-intent-warning .bp3-spinner-head{
  stroke:#d9822b; }

.bp3-spinner.bp3-intent-danger .bp3-spinner-head{
  stroke:#db3737; }
.bp3-tabs.bp3-vertical{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-tabs.bp3-vertical > .bp3-tab-list{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start;
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab{
      border-radius:3px;
      padding:0 10px;
      width:100%; }
      .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab[aria-selected="true"]{
        background-color:rgba(19, 124, 189, 0.2);
        -webkit-box-shadow:none;
                box-shadow:none; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab-indicator-wrapper .bp3-tab-indicator{
      background-color:rgba(19, 124, 189, 0.2);
      border-radius:3px;
      bottom:0;
      height:auto;
      left:0;
      right:0;
      top:0; }
  .bp3-tabs.bp3-vertical > .bp3-tab-panel{
    margin-top:0;
    padding-left:20px; }

.bp3-tab-list{
  -webkit-box-align:end;
      -ms-flex-align:end;
          align-items:flex-end;
  border:none;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  list-style:none;
  margin:0;
  padding:0;
  position:relative; }
  .bp3-tab-list > *:not(:last-child){
    margin-right:20px; }

.bp3-tab{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  color:#182026;
  cursor:pointer;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  font-size:14px;
  line-height:30px;
  max-width:100%;
  position:relative;
  vertical-align:top; }
  .bp3-tab a{
    color:inherit;
    display:block;
    text-decoration:none; }
  .bp3-tab-indicator-wrapper ~ .bp3-tab{
    background-color:transparent !important;
    -webkit-box-shadow:none !important;
            box-shadow:none !important; }
  .bp3-tab[aria-disabled="true"]{
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-tab[aria-selected="true"]{
    border-radius:0;
    -webkit-box-shadow:inset 0 -3px 0 #106ba3;
            box-shadow:inset 0 -3px 0 #106ba3; }
  .bp3-tab[aria-selected="true"], .bp3-tab:not([aria-disabled="true"]):hover{
    color:#106ba3; }
  .bp3-tab:focus{
    -moz-outline-radius:0; }
  .bp3-large > .bp3-tab{
    font-size:16px;
    line-height:40px; }

.bp3-tab-panel{
  margin-top:20px; }
  .bp3-tab-panel[aria-hidden="true"]{
    display:none; }

.bp3-tab-indicator-wrapper{
  left:0;
  pointer-events:none;
  position:absolute;
  top:0;
  -webkit-transform:translateX(0), translateY(0);
          transform:translateX(0), translateY(0);
  -webkit-transition:height, width, -webkit-transform;
  transition:height, width, -webkit-transform;
  transition:height, transform, width;
  transition:height, transform, width, -webkit-transform;
  -webkit-transition-duration:200ms;
          transition-duration:200ms;
  -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
          transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tab-indicator-wrapper .bp3-tab-indicator{
    background-color:#106ba3;
    bottom:0;
    height:3px;
    left:0;
    position:absolute;
    right:0; }
  .bp3-tab-indicator-wrapper.bp3-no-animation{
    -webkit-transition:none;
    transition:none; }

.bp3-dark .bp3-tab{
  color:#f5f8fa; }
  .bp3-dark .bp3-tab[aria-disabled="true"]{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tab[aria-selected="true"]{
    -webkit-box-shadow:inset 0 -3px 0 #48aff0;
            box-shadow:inset 0 -3px 0 #48aff0; }
  .bp3-dark .bp3-tab[aria-selected="true"], .bp3-dark .bp3-tab:not([aria-disabled="true"]):hover{
    color:#48aff0; }

.bp3-dark .bp3-tab-indicator{
  background-color:#48aff0; }

.bp3-flex-expander{
  -webkit-box-flex:1;
      -ms-flex:1 1;
          flex:1 1; }
.bp3-tag{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:#5c7080;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:none;
          box-shadow:none;
  color:#f5f8fa;
  font-size:12px;
  line-height:16px;
  max-width:100%;
  min-height:20px;
  min-width:20px;
  padding:2px 6px;
  position:relative; }
  .bp3-tag.bp3-interactive{
    cursor:pointer; }
    .bp3-tag.bp3-interactive:hover{
      background-color:rgba(92, 112, 128, 0.85); }
    .bp3-tag.bp3-interactive.bp3-active, .bp3-tag.bp3-interactive:active{
      background-color:rgba(92, 112, 128, 0.7); }
  .bp3-tag > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag::before,
  .bp3-tag > *{
    margin-right:4px; }
  .bp3-tag:empty::before,
  .bp3-tag > :last-child{
    margin-right:0; }
  .bp3-tag:focus{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:0;
    -moz-outline-radius:6px; }
  .bp3-tag.bp3-round{
    border-radius:30px;
    padding-left:8px;
    padding-right:8px; }
  .bp3-dark .bp3-tag{
    background-color:#bfccd6;
    color:#182026; }
    .bp3-dark .bp3-tag.bp3-interactive{
      cursor:pointer; }
      .bp3-dark .bp3-tag.bp3-interactive:hover{
        background-color:rgba(191, 204, 214, 0.85); }
      .bp3-dark .bp3-tag.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-interactive:active{
        background-color:rgba(191, 204, 214, 0.7); }
    .bp3-dark .bp3-tag > .bp3-icon, .bp3-dark .bp3-tag .bp3-icon-standard, .bp3-dark .bp3-tag .bp3-icon-large{
      fill:currentColor; }
  .bp3-tag > .bp3-icon, .bp3-tag .bp3-icon-standard, .bp3-tag .bp3-icon-large{
    fill:#ffffff; }
  .bp3-tag.bp3-large,
  .bp3-large .bp3-tag{
    font-size:14px;
    line-height:20px;
    min-height:30px;
    min-width:30px;
    padding:5px 10px; }
    .bp3-tag.bp3-large::before,
    .bp3-tag.bp3-large > *,
    .bp3-large .bp3-tag::before,
    .bp3-large .bp3-tag > *{
      margin-right:7px; }
    .bp3-tag.bp3-large:empty::before,
    .bp3-tag.bp3-large > :last-child,
    .bp3-large .bp3-tag:empty::before,
    .bp3-large .bp3-tag > :last-child{
      margin-right:0; }
    .bp3-tag.bp3-large.bp3-round,
    .bp3-large .bp3-tag.bp3-round{
      padding-left:12px;
      padding-right:12px; }
  .bp3-tag.bp3-intent-primary{
    background:#137cbd;
    color:#ffffff; }
    .bp3-tag.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.85); }
      .bp3-tag.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.7); }
  .bp3-tag.bp3-intent-success{
    background:#0f9960;
    color:#ffffff; }
    .bp3-tag.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.85); }
      .bp3-tag.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.7); }
  .bp3-tag.bp3-intent-warning{
    background:#d9822b;
    color:#ffffff; }
    .bp3-tag.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.85); }
      .bp3-tag.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.7); }
  .bp3-tag.bp3-intent-danger{
    background:#db3737;
    color:#ffffff; }
    .bp3-tag.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.85); }
      .bp3-tag.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.7); }
  .bp3-tag.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-tag.bp3-minimal > .bp3-icon, .bp3-tag.bp3-minimal .bp3-icon-standard, .bp3-tag.bp3-minimal .bp3-icon-large{
    fill:#5c7080; }
  .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
    background-color:rgba(138, 155, 168, 0.2);
    color:#182026; }
    .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
        background-color:rgba(92, 112, 128, 0.3); }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
        background-color:rgba(92, 112, 128, 0.4); }
    .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
      color:#f5f8fa; }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
          background-color:rgba(191, 204, 214, 0.3); }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
          background-color:rgba(191, 204, 214, 0.4); }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) > .bp3-icon, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-large{
        fill:#a7b6c2; }
  .bp3-tag.bp3-minimal.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15);
    color:#106ba3; }
    .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-primary > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-large{
      fill:#137cbd; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25);
      color:#48aff0; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
          background-color:rgba(19, 124, 189, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
          background-color:rgba(19, 124, 189, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15);
    color:#0d8050; }
    .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-success > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-large{
      fill:#0f9960; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25);
      color:#3dcc91; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
          background-color:rgba(15, 153, 96, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
          background-color:rgba(15, 153, 96, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15);
    color:#bf7326; }
    .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-warning > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-large{
      fill:#d9822b; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25);
      color:#ffb366; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
          background-color:rgba(217, 130, 43, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
          background-color:rgba(217, 130, 43, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15);
    color:#c23030; }
    .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-danger > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-large{
      fill:#db3737; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25);
      color:#ff7373; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
          background-color:rgba(219, 55, 55, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
          background-color:rgba(219, 55, 55, 0.45); }

.bp3-tag-remove{
  background:none;
  border:none;
  color:inherit;
  cursor:pointer;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin-bottom:-2px;
  margin-right:-6px !important;
  margin-top:-2px;
  opacity:0.5;
  padding:2px;
  padding-left:0; }
  .bp3-tag-remove:hover{
    background:none;
    opacity:0.8;
    text-decoration:none; }
  .bp3-tag-remove:active{
    opacity:1; }
  .bp3-tag-remove:empty::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    content:""; }
  .bp3-large .bp3-tag-remove{
    margin-right:-10px !important;
    padding:0 5px 0 0; }
    .bp3-large .bp3-tag-remove:empty::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1; }
.bp3-tag-input{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  cursor:text;
  height:auto;
  line-height:inherit;
  min-height:30px;
  padding-left:5px;
  padding-right:0; }
  .bp3-tag-input > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag-input > .bp3-tag-input-values{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag-input .bp3-tag-input-icon{
    color:#5c7080;
    margin-left:2px;
    margin-right:7px;
    margin-top:7px; }
  .bp3-tag-input .bp3-tag-input-values{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row;
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    -ms-flex-item-align:stretch;
        align-self:stretch;
    -ms-flex-wrap:wrap;
        flex-wrap:wrap;
    margin-right:7px;
    margin-top:5px;
    min-width:0; }
    .bp3-tag-input .bp3-tag-input-values > *{
      -webkit-box-flex:0;
          -ms-flex-positive:0;
              flex-grow:0;
      -ms-flex-negative:0;
          flex-shrink:0; }
    .bp3-tag-input .bp3-tag-input-values > .bp3-fill{
      -webkit-box-flex:1;
          -ms-flex-positive:1;
              flex-grow:1;
      -ms-flex-negative:1;
          flex-shrink:1; }
    .bp3-tag-input .bp3-tag-input-values::before,
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-right:5px; }
    .bp3-tag-input .bp3-tag-input-values:empty::before,
    .bp3-tag-input .bp3-tag-input-values > :last-child{
      margin-right:0; }
    .bp3-tag-input .bp3-tag-input-values:first-child .bp3-input-ghost:first-child{
      padding-left:5px; }
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-bottom:5px; }
  .bp3-tag-input .bp3-tag{
    overflow-wrap:break-word; }
    .bp3-tag-input .bp3-tag.bp3-active{
      outline:rgba(19, 124, 189, 0.6) auto 2px;
      outline-offset:0;
      -moz-outline-radius:6px; }
  .bp3-tag-input .bp3-input-ghost{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:20px;
    width:80px; }
    .bp3-tag-input .bp3-input-ghost:disabled, .bp3-tag-input .bp3-input-ghost.bp3-disabled{
      cursor:not-allowed; }
  .bp3-tag-input .bp3-button,
  .bp3-tag-input .bp3-spinner{
    margin:3px;
    margin-left:0; }
  .bp3-tag-input .bp3-button{
    min-height:24px;
    min-width:24px;
    padding:0 7px; }
  .bp3-tag-input.bp3-large{
    height:auto;
    min-height:40px; }
    .bp3-tag-input.bp3-large::before,
    .bp3-tag-input.bp3-large > *{
      margin-right:10px; }
    .bp3-tag-input.bp3-large:empty::before,
    .bp3-tag-input.bp3-large > :last-child{
      margin-right:0; }
    .bp3-tag-input.bp3-large .bp3-tag-input-icon{
      margin-left:5px;
      margin-top:10px; }
    .bp3-tag-input.bp3-large .bp3-input-ghost{
      line-height:30px; }
    .bp3-tag-input.bp3-large .bp3-button{
      min-height:30px;
      min-width:30px;
      padding:5px 10px;
      margin:5px;
      margin-left:0; }
    .bp3-tag-input.bp3-large .bp3-spinner{
      margin:8px;
      margin-left:0; }
  .bp3-tag-input.bp3-active{
    background-color:#ffffff;
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-tag-input .bp3-tag-input-icon, .bp3-tag-input.bp3-dark .bp3-tag-input-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-tag-input .bp3-input-ghost, .bp3-tag-input.bp3-dark .bp3-input-ghost{
    color:#f5f8fa; }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-webkit-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-moz-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost:-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::placeholder{
      color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tag-input.bp3-active, .bp3-tag-input.bp3-dark.bp3-active{
    background-color:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-primary, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-success, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-warning, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-danger, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-input-ghost{
  background:none;
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0; }
  .bp3-input-ghost::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost:focus{
    outline:none !important; }
.bp3-toast{
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin:20px 0 0;
  max-width:500px;
  min-width:300px;
  pointer-events:all;
  position:relative !important; }
  .bp3-toast.bp3-toast-enter, .bp3-toast.bp3-toast-appear{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active, .bp3-toast.bp3-toast-appear-active{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-toast.bp3-toast-enter ~ .bp3-toast, .bp3-toast.bp3-toast-appear ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active ~ .bp3-toast, .bp3-toast.bp3-toast-appear-active ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-toast.bp3-toast-exit{
    opacity:1;
    -webkit-filter:blur(0);
            filter:blur(0); }
  .bp3-toast.bp3-toast-exit-active{
    opacity:0;
    -webkit-filter:blur(10px);
            filter:blur(10px);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:opacity, filter;
    transition-property:opacity, filter, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-toast.bp3-toast-exit ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0); }
  .bp3-toast.bp3-toast-exit-active ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px);
    -webkit-transition-delay:50ms;
            transition-delay:50ms;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-toast .bp3-button-group{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    padding:5px;
    padding-left:0; }
  .bp3-toast > .bp3-icon{
    color:#5c7080;
    margin:12px;
    margin-right:0; }
  .bp3-toast.bp3-dark,
  .bp3-dark .bp3-toast{
    background-color:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-toast.bp3-dark > .bp3-icon,
    .bp3-dark .bp3-toast > .bp3-icon{
      color:#a7b6c2; }
  .bp3-toast[class*="bp3-intent-"] a{
    color:rgba(255, 255, 255, 0.7); }
    .bp3-toast[class*="bp3-intent-"] a:hover{
      color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] > .bp3-icon{
    color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button, .bp3-toast[class*="bp3-intent-"] .bp3-button::before,
  .bp3-toast[class*="bp3-intent-"] .bp3-button .bp3-icon, .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    color:rgba(255, 255, 255, 0.7) !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:focus{
    outline-color:rgba(255, 255, 255, 0.5); }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:hover{
    background-color:rgba(255, 255, 255, 0.15) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    background-color:rgba(255, 255, 255, 0.3) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button::after{
    background:rgba(255, 255, 255, 0.3) !important; }
  .bp3-toast.bp3-intent-primary{
    background-color:#137cbd;
    color:#ffffff; }
  .bp3-toast.bp3-intent-success{
    background-color:#0f9960;
    color:#ffffff; }
  .bp3-toast.bp3-intent-warning{
    background-color:#d9822b;
    color:#ffffff; }
  .bp3-toast.bp3-intent-danger{
    background-color:#db3737;
    color:#ffffff; }

.bp3-toast-message{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  padding:11px;
  word-break:break-word; }

.bp3-toast-container{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box !important;
  display:-ms-flexbox !important;
  display:flex !important;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  left:0;
  overflow:hidden;
  padding:0 20px 20px;
  pointer-events:none;
  right:0;
  z-index:40; }
  .bp3-toast-container.bp3-toast-container-in-portal{
    position:fixed; }
  .bp3-toast-container.bp3-toast-container-inline{
    position:absolute; }
  .bp3-toast-container.bp3-toast-container-top{
    top:0; }
  .bp3-toast-container.bp3-toast-container-bottom{
    bottom:0;
    -webkit-box-orient:vertical;
    -webkit-box-direction:reverse;
        -ms-flex-direction:column-reverse;
            flex-direction:column-reverse;
    top:auto; }
  .bp3-toast-container.bp3-toast-container-left{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start; }
  .bp3-toast-container.bp3-toast-container-right{
    -webkit-box-align:end;
        -ms-flex-align:end;
            align-items:flex-end; }

.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active) ~ .bp3-toast, .bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active) ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-exit-active ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-leave-active ~ .bp3-toast{
  -webkit-transform:translateY(60px);
          transform:translateY(60px); }
.bp3-tooltip{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1); }
  .bp3-tooltip .bp3-popover-arrow{
    height:22px;
    position:absolute;
    width:22px; }
    .bp3-tooltip .bp3-popover-arrow::before{
      height:14px;
      margin:4px;
      width:14px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip{
    margin-bottom:11px;
    margin-top:-11px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
      bottom:-8px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip{
    margin-left:11px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
      left:-8px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip{
    margin-top:11px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
      top:-8px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip{
    margin-left:-11px;
    margin-right:11px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
      right:-8px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-tooltip > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-tooltip > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
    top:-0.22183px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
    right:-0.22183px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
    left:-0.22183px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
    bottom:-0.22183px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-tooltip .bp3-popover-content{
    background:#394b59;
    color:#f5f8fa; }
  .bp3-tooltip .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-tooltip .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-tooltip .bp3-popover-arrow-fill{
    fill:#394b59; }
  .bp3-popover-enter > .bp3-tooltip, .bp3-popover-appear > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8); }
  .bp3-popover-enter-active > .bp3-tooltip, .bp3-popover-appear-active > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-popover-exit > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tooltip .bp3-popover-content{
    padding:10px 12px; }
  .bp3-tooltip.bp3-dark,
  .bp3-dark .bp3-tooltip{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-tooltip .bp3-popover-content{
      background:#e1e8ed;
      color:#394b59; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-fill{
      fill:#e1e8ed; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-content{
    background:#137cbd;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-arrow-fill{
    fill:#137cbd; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-content{
    background:#0f9960;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-arrow-fill{
    fill:#0f9960; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-content{
    background:#d9822b;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-arrow-fill{
    fill:#d9822b; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-content{
    background:#db3737;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-arrow-fill{
    fill:#db3737; }

.bp3-tooltip-indicator{
  border-bottom:dotted 1px;
  cursor:help; }
.bp3-tree .bp3-icon, .bp3-tree .bp3-icon-standard, .bp3-tree .bp3-icon-large{
  color:#5c7080; }
  .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-tree .bp3-icon.bp3-intent-success, .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-tree-node-list{
  list-style:none;
  margin:0;
  padding-left:0; }

.bp3-tree-root{
  background-color:transparent;
  cursor:default;
  padding-left:0;
  position:relative; }

.bp3-tree-node-content-0{
  padding-left:0px; }

.bp3-tree-node-content-1{
  padding-left:23px; }

.bp3-tree-node-content-2{
  padding-left:46px; }

.bp3-tree-node-content-3{
  padding-left:69px; }

.bp3-tree-node-content-4{
  padding-left:92px; }

.bp3-tree-node-content-5{
  padding-left:115px; }

.bp3-tree-node-content-6{
  padding-left:138px; }

.bp3-tree-node-content-7{
  padding-left:161px; }

.bp3-tree-node-content-8{
  padding-left:184px; }

.bp3-tree-node-content-9{
  padding-left:207px; }

.bp3-tree-node-content-10{
  padding-left:230px; }

.bp3-tree-node-content-11{
  padding-left:253px; }

.bp3-tree-node-content-12{
  padding-left:276px; }

.bp3-tree-node-content-13{
  padding-left:299px; }

.bp3-tree-node-content-14{
  padding-left:322px; }

.bp3-tree-node-content-15{
  padding-left:345px; }

.bp3-tree-node-content-16{
  padding-left:368px; }

.bp3-tree-node-content-17{
  padding-left:391px; }

.bp3-tree-node-content-18{
  padding-left:414px; }

.bp3-tree-node-content-19{
  padding-left:437px; }

.bp3-tree-node-content-20{
  padding-left:460px; }

.bp3-tree-node-content{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:30px;
  padding-right:5px;
  width:100%; }
  .bp3-tree-node-content:hover{
    background-color:rgba(191, 204, 214, 0.4); }

.bp3-tree-node-caret,
.bp3-tree-node-caret-none{
  min-width:30px; }

.bp3-tree-node-caret{
  color:#5c7080;
  cursor:pointer;
  padding:7px;
  -webkit-transform:rotate(0deg);
          transform:rotate(0deg);
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tree-node-caret:hover{
    color:#182026; }
  .bp3-dark .bp3-tree-node-caret{
    color:#a7b6c2; }
    .bp3-dark .bp3-tree-node-caret:hover{
      color:#f5f8fa; }
  .bp3-tree-node-caret.bp3-tree-node-caret-open{
    -webkit-transform:rotate(90deg);
            transform:rotate(90deg); }
  .bp3-tree-node-caret.bp3-icon-standard::before{
    content:""; }

.bp3-tree-node-icon{
  margin-right:7px;
  position:relative; }

.bp3-tree-node-label{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-label span{
    display:inline; }

.bp3-tree-node-secondary-label{
  padding:0 5px;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-secondary-label .bp3-popover-wrapper,
  .bp3-tree-node-secondary-label .bp3-popover-target{
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-content{
  background-color:inherit;
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-caret,
.bp3-tree-node.bp3-disabled .bp3-tree-node-icon{
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content,
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-standard, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-large{
    color:#ffffff; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret::before{
    color:rgba(255, 255, 255, 0.7); }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret:hover::before{
    color:#ffffff; }

.bp3-dark .bp3-tree-node-content:hover{
  background-color:rgba(92, 112, 128, 0.3); }

.bp3-dark .bp3-tree .bp3-icon, .bp3-dark .bp3-tree .bp3-icon-standard, .bp3-dark .bp3-tree .bp3-icon-large{
  color:#a7b6c2; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-dark .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
.bp3-omnibar{
  -webkit-filter:blur(0);
          filter:blur(0);
  opacity:1;
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  left:calc(50% - 250px);
  top:20vh;
  width:500px;
  z-index:21; }
  .bp3-omnibar.bp3-overlay-enter, .bp3-omnibar.bp3-overlay-appear{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2; }
  .bp3-omnibar.bp3-overlay-enter-active, .bp3-omnibar.bp3-overlay-appear-active{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-omnibar.bp3-overlay-exit{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1; }
  .bp3-omnibar.bp3-overlay-exit-active{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-omnibar .bp3-input{
    background-color:transparent;
    border-radius:0; }
    .bp3-omnibar .bp3-input, .bp3-omnibar .bp3-input:focus{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-omnibar .bp3-menu{
    background-color:transparent;
    border-radius:0;
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
    max-height:calc(60vh - 40px);
    overflow:auto; }
    .bp3-omnibar .bp3-menu:empty{
      display:none; }
  .bp3-dark .bp3-omnibar, .bp3-omnibar.bp3-dark{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-omnibar-overlay .bp3-overlay-backdrop{
  background-color:rgba(16, 22, 26, 0.2); }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }

.bp3-multi-select{
  min-width:150px; }

.bp3-multi-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto; }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1pY29uLWJyYW5kMSBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNmZmYiPgogICAgPHBhdGggZD0iTTEwNSAxMjcuM2g0MHYxMi44aC00MHpNNTEuMSA3N0w3NCA5OS45bC0yMy4zIDIzLjMgMTAuNSAxMC41IDIzLjMtMjMuM0w5NSA5OS45IDg0LjUgODkuNCA2MS42IDY2LjV6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMSBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNGOUE4MjUiPgogICAgPHBhdGggZD0iTTIwLjIgMTEuOGMtMS42IDAtMS43LjUtMS43IDEgMCAuNC4xLjkuMSAxLjMuMS41LjEuOS4xIDEuMyAwIDEuNy0xLjQgMi4zLTMuNSAyLjNoLS45di0xLjloLjVjMS4xIDAgMS40IDAgMS40LS44IDAtLjMgMC0uNi0uMS0xIDAtLjQtLjEtLjgtLjEtMS4yIDAtMS4zIDAtMS44IDEuMy0yLTEuMy0uMi0xLjMtLjctMS4zLTIgMC0uNC4xLS44LjEtMS4yLjEtLjQuMS0uNy4xLTEgMC0uOC0uNC0uNy0xLjQtLjhoLS41VjQuMWguOWMyLjIgMCAzLjUuNyAzLjUgMi4zIDAgLjQtLjEuOS0uMSAxLjMtLjEuNS0uMS45LS4xIDEuMyAwIC41LjIgMSAxLjcgMXYxLjh6TTEuOCAxMC4xYzEuNiAwIDEuNy0uNSAxLjctMSAwLS40LS4xLS45LS4xLTEuMy0uMS0uNS0uMS0uOS0uMS0xLjMgMC0xLjYgMS40LTIuMyAzLjUtMi4zaC45djEuOWgtLjVjLTEgMC0xLjQgMC0xLjQuOCAwIC4zIDAgLjYuMSAxIDAgLjIuMS42LjEgMSAwIDEuMyAwIDEuOC0xLjMgMkM2IDExLjIgNiAxMS43IDYgMTNjMCAuNC0uMS44LS4xIDEuMi0uMS4zLS4xLjctLjEgMSAwIC44LjMuOCAxLjQuOGguNXYxLjloLS45Yy0yLjEgMC0zLjUtLjYtMy41LTIuMyAwLS40LjEtLjkuMS0xLjMuMS0uNS4xLS45LjEtMS4zIDAtLjUtLjItMS0xLjctMXYtMS45eiIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSIxMy44IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY3g9IjExIiBjeT0iOC4yIiByPSIyLjEiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgPGcgY2xhc3M9ImpwLWljb24td2FybjAiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4=);
  --jp-icon-listings-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MC45NzggNTAuOTc4IiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1MC45NzggNTAuOTc4OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+Cgk8Zz4KCQk8cGF0aCBzdHlsZT0iZmlsbDojMDEwMDAyOyIgZD0iTTQzLjUyLDcuNDU4QzM4LjcxMSwyLjY0OCwzMi4zMDcsMCwyNS40ODksMEMxOC42NywwLDEyLjI2NiwyLjY0OCw3LjQ1OCw3LjQ1OAoJCQljLTkuOTQzLDkuOTQxLTkuOTQzLDI2LjExOSwwLDM2LjA2MmM0LjgwOSw0LjgwOSwxMS4yMTIsNy40NTYsMTguMDMxLDcuNDU4YzAsMCwwLjAwMSwwLDAuMDAyLDAKCQkJYzYuODE2LDAsMTMuMjIxLTIuNjQ4LDE4LjAyOS03LjQ1OGM0LjgwOS00LjgwOSw3LjQ1Ny0xMS4yMTIsNy40NTctMTguMDNDNTAuOTc3LDE4LjY3LDQ4LjMyOCwxMi4yNjYsNDMuNTIsNy40NTh6CgkJCSBNNDIuMTA2LDQyLjEwNWMtNC40MzIsNC40MzEtMTAuMzMyLDYuODcyLTE2LjYxNSw2Ljg3MmgtMC4wMDJjLTYuMjg1LTAuMDAxLTEyLjE4Ny0yLjQ0MS0xNi42MTctNi44NzIKCQkJYy05LjE2Mi05LjE2My05LjE2Mi0yNC4wNzEsMC0zMy4yMzNDMTMuMzAzLDQuNDQsMTkuMjA0LDIsMjUuNDg5LDJjNi4yODQsMCwxMi4xODYsMi40NCwxNi42MTcsNi44NzIKCQkJYzQuNDMxLDQuNDMxLDYuODcxLDEwLjMzMiw2Ljg3MSwxNi42MTdDNDguOTc3LDMxLjc3Miw0Ni41MzYsMzcuNjc1LDQyLjEwNiw0Mi4xMDV6Ii8+CgkJPHBhdGggc3R5bGU9ImZpbGw6IzAxMDAwMjsiIGQ9Ik0yMy41NzgsMzIuMjE4Yy0wLjAyMy0xLjczNCwwLjE0My0zLjA1OSwwLjQ5Ni0zLjk3MmMwLjM1My0wLjkxMywxLjExLTEuOTk3LDIuMjcyLTMuMjUzCgkJCWMwLjQ2OC0wLjUzNiwwLjkyMy0xLjA2MiwxLjM2Ny0xLjU3NWMwLjYyNi0wLjc1MywxLjEwNC0xLjQ3OCwxLjQzNi0yLjE3NWMwLjMzMS0wLjcwNywwLjQ5NS0xLjU0MSwwLjQ5NS0yLjUKCQkJYzAtMS4wOTYtMC4yNi0yLjA4OC0wLjc3OS0yLjk3OWMtMC41NjUtMC44NzktMS41MDEtMS4zMzYtMi44MDYtMS4zNjljLTEuODAyLDAuMDU3LTIuOTg1LDAuNjY3LTMuNTUsMS44MzIKCQkJYy0wLjMwMSwwLjUzNS0wLjUwMywxLjE0MS0wLjYwNywxLjgxNGMtMC4xMzksMC43MDctMC4yMDcsMS40MzItMC4yMDcsMi4xNzRoLTIuOTM3Yy0wLjA5MS0yLjIwOCwwLjQwNy00LjExNCwxLjQ5My01LjcxOQoJCQljMS4wNjItMS42NCwyLjg1NS0yLjQ4MSw1LjM3OC0yLjUyN2MyLjE2LDAuMDIzLDMuODc0LDAuNjA4LDUuMTQxLDEuNzU4YzEuMjc4LDEuMTYsMS45MjksMi43NjQsMS45NSw0LjgxMQoJCQljMCwxLjE0Mi0wLjEzNywyLjExMS0wLjQxLDIuOTExYy0wLjMwOSwwLjg0NS0wLjczMSwxLjU5My0xLjI2OCwyLjI0M2MtMC40OTIsMC42NS0xLjA2OCwxLjMxOC0xLjczLDIuMDAyCgkJCWMtMC42NSwwLjY5Ny0xLjMxMywxLjQ3OS0xLjk4NywyLjM0NmMtMC4yMzksMC4zNzctMC40MjksMC43NzctMC41NjUsMS4xOTljLTAuMTYsMC45NTktMC4yMTcsMS45NTEtMC4xNzEsMi45NzkKCQkJQzI2LjU4OSwzMi4yMTgsMjMuNTc4LDMyLjIxOCwyMy41NzgsMzIuMjE4eiBNMjMuNTc4LDM4LjIydi0zLjQ4NGgzLjA3NnYzLjQ4NEgyMy41Nzh6Ii8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMEQ0N0ExIj4KICAgIDxwYXRoIGQ9Ik0xMS4xIDYuOVY1LjhINi45YzAtLjUgMC0xLjMuMi0xLjYuNC0uNy44LTEuMSAxLjctMS40IDEuNy0uMyAyLjUtLjMgMy45LS4xIDEgLjEgMS45LjkgMS45IDEuOXY0LjJjMCAuNS0uOSAxLjYtMiAxLjZIOC44Yy0xLjUgMC0yLjQgMS40LTIuNCAyLjh2Mi4ySDQuN0MzLjUgMTUuMSAzIDE0IDMgMTMuMVY5Yy0uMS0xIC42LTIgMS44LTIgMS41LS4xIDYuMy0uMSA2LjMtLjF6Ii8+CiAgICA8cGF0aCBkPSJNMTAuOSAxNS4xdjEuMWg0LjJjMCAuNSAwIDEuMy0uMiAxLjYtLjQuNy0uOCAxLjEtMS43IDEuNC0xLjcuMy0yLjUuMy0zLjkuMS0xLS4xLTEuOS0uOS0xLjktMS45di00LjJjMC0uNS45LTEuNiAyLTEuNmgzLjhjMS41IDAgMi40LTEuNCAyLjQtMi44VjYuNmgxLjdDMTguNSA2LjkgMTkgOCAxOSA4LjlWMTNjMCAxLS43IDIuMS0xLjkgMi4xaC02LjJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4=);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMikiIGZpbGw9IiMzMzMzMzMiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uLWFjY2VudDIganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGQ9Ik01LjA1NjY0IDguNzYxNzJDNS4wNTY2NCA4LjU5NzY2IDUuMDMxMjUgOC40NTMxMiA0Ljk4MDQ3IDguMzI4MTJDNC45MzM1OSA4LjE5OTIyIDQuODU1NDcgOC4wODIwMyA0Ljc0NjA5IDcuOTc2NTZDNC42NDA2MiA3Ljg3MTA5IDQuNSA3Ljc3NTM5IDQuMzI0MjIgNy42ODk0NUM0LjE1MjM0IDcuNTk5NjEgMy45NDMzNiA3LjUxMTcyIDMuNjk3MjcgNy40MjU3OEMzLjMwMjczIDcuMjg1MTYgMi45NDMzNiA3LjEzNjcyIDIuNjE5MTQgNi45ODA0N0MyLjI5NDkyIDYuODI0MjIgMi4wMTc1OCA2LjY0MjU4IDEuNzg3MTEgNi40MzU1NUMxLjU2MDU1IDYuMjI4NTIgMS4zODQ3NyA1Ljk4ODI4IDEuMjU5NzcgNS43MTQ4NEMxLjEzNDc3IDUuNDM3NSAxLjA3MjI3IDUuMTA5MzggMS4wNzIyNyA0LjczMDQ3QzEuMDcyMjcgNC4zOTg0NCAxLjEyODkxIDQuMDk1NyAxLjI0MjE5IDMuODIyMjdDMS4zNTU0NyAzLjU0NDkyIDEuNTE1NjIgMy4zMDQ2OSAxLjcyMjY2IDMuMTAxNTZDMS45Mjk2OSAyLjg5ODQ0IDIuMTc5NjkgMi43MzQzNyAyLjQ3MjY2IDIuNjA5MzhDMi43NjU2MiAyLjQ4NDM4IDMuMDkxOCAyLjQwNDMgMy40NTExNyAyLjM2OTE0VjEuMTA5MzhINC4zODg2N1YyLjM4MDg2QzQuNzQwMjMgMi40Mjc3MyA1LjA1NjY0IDIuNTIzNDQgNS4zMzc4OSAyLjY2Nzk3QzUuNjE5MTQgMi44MTI1IDUuODU3NDIgMy4wMDE5NSA2LjA1MjczIDMuMjM2MzNDNi4yNTE5NSAzLjQ2NjggNi40MDQzIDMuNzQwMjMgNi41MDk3NyA0LjA1NjY0QzYuNjE5MTQgNC4zNjkxNCA2LjY3MzgzIDQuNzIwNyA2LjY3MzgzIDUuMTExMzNINS4wNDQ5MkM1LjA0NDkyIDQuNjM4NjcgNC45Mzc1IDQuMjgxMjUgNC43MjI2NiA0LjAzOTA2QzQuNTA3ODEgMy43OTI5NyA0LjIxNjggMy42Njk5MiAzLjg0OTYxIDMuNjY5OTJDMy42NTAzOSAzLjY2OTkyIDMuNDc2NTYgMy42OTcyNyAzLjMyODEyIDMuNzUxOTVDMy4xODM1OSAzLjgwMjczIDMuMDY0NDUgMy44NzY5NSAyLjk3MDcgMy45NzQ2MUMyLjg3Njk1IDQuMDY4MzYgMi44MDY2NCA0LjE3OTY5IDIuNzU5NzcgNC4zMDg1OUMyLjcxNjggNC40Mzc1IDIuNjk1MzEgNC41NzgxMiAyLjY5NTMxIDQuNzMwNDdDMi42OTUzMSA0Ljg4MjgxIDIuNzE2OCA1LjAxOTUzIDIuNzU5NzcgNS4xNDA2MkMyLjgwNjY0IDUuMjU3ODEgMi44ODI4MSA1LjM2NzE5IDIuOTg4MjggNS40Njg3NUMzLjA5NzY2IDUuNTcwMzEgMy4yNDAyMyA1LjY2Nzk3IDMuNDE2MDIgNS43NjE3MkMzLjU5MTggNS44NTE1NiAzLjgxMDU1IDUuOTQzMzYgNC4wNzIyNyA2LjAzNzExQzQuNDY2OCA2LjE4NTU1IDQuODI0MjIgNi4zMzk4NCA1LjE0NDUzIDYuNUM1LjQ2NDg0IDYuNjU2MjUgNS43MzgyOCA2LjgzOTg0IDUuOTY0ODQgNy4wNTA3OEM2LjE5NTMxIDcuMjU3ODEgNi4zNzEwOSA3LjUgNi40OTIxOSA3Ljc3NzM0QzYuNjE3MTkgOC4wNTA3OCA2LjY3OTY5IDguMzc1IDYuNjc5NjkgOC43NUM2LjY3OTY5IDkuMDkzNzUgNi42MjMwNSA5LjQwNDMgNi41MDk3NyA5LjY4MTY0QzYuMzk2NDggOS45NTUwOCA2LjIzNDM4IDEwLjE5MTQgNi4wMjM0NCAxMC4zOTA2QzUuODEyNSAxMC41ODk4IDUuNTU4NTkgMTAuNzUgNS4yNjE3MiAxMC44NzExQzQuOTY0ODQgMTAuOTg4MyA0LjYzMjgxIDExLjA2NDUgNC4yNjU2MiAxMS4wOTk2VjEyLjI0OEgzLjMzMzk4VjExLjA5OTZDMy4wMDE5NSAxMS4wNjg0IDIuNjc5NjkgMTAuOTk2MSAyLjM2NzE5IDEwLjg4MjhDMi4wNTQ2OSAxMC43NjU2IDEuNzc3MzQgMTAuNTk3NyAxLjUzNTE2IDEwLjM3ODlDMS4yOTY4OCAxMC4xNjAyIDEuMTA1NDcgOS44ODQ3NyAwLjk2MDkzOCA5LjU1MjczQzAuODE2NDA2IDkuMjE2OCAwLjc0NDE0MSA4LjgxNDQ1IDAuNzQ0MTQxIDguMzQ1N0gyLjM3ODkxQzIuMzc4OTEgOC42MjY5NSAyLjQxOTkyIDguODYzMjggMi41MDE5NSA5LjA1NDY5QzIuNTgzOTggOS4yNDIxOSAyLjY4OTQ1IDkuMzkyNTggMi44MTgzNiA5LjUwNTg2QzIuOTUxMTcgOS42MTUyMyAzLjEwMTU2IDkuNjkzMzYgMy4yNjk1MyA5Ljc0MDIzQzMuNDM3NSA5Ljc4NzExIDMuNjA5MzggOS44MTA1NSAzLjc4NTE2IDkuODEwNTVDNC4yMDMxMiA5LjgxMDU1IDQuNTE5NTMgOS43MTI4OSA0LjczNDM4IDkuNTE3NThDNC45NDkyMiA5LjMyMjI3IDUuMDU2NjQgOS4wNzAzMSA1LjA1NjY0IDguNzYxNzJaTTEzLjQxOCAxMi4yNzE1SDguMDc0MjJWMTFIMTMuNDE4VjEyLjI3MTVaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzLjk1MjY0IDYpIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTUgMTVIM3YyaDEydi0yem0wLThIM3YyaDEyVjd6TTMgMTNoMTh2LTJIM3Yyem0wIDhoMTh2LTJIM3Yyek0zIDN2MmgxOFYzSDN6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4=);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}
.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}
.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}
.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}
.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}
.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}
.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}
.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}
.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}
.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}
.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}
.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}
.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}
.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}
.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}
.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}
.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}
.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}
.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}
.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}
.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}
.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}
.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}
.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}
.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}
.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}
.jp-FileIcon {
  background-image: var(--jp-icon-file);
}
.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}
.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}
.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}
.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}
.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}
.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}
.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}
.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}
.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}
.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}
.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}
.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}
.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}
.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}
.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}
.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}
.jp-ListIcon {
  background-image: var(--jp-icon-list);
}
.jp-ListingsInfoIcon {
  background-image: var(--jp-icon-listings-info);
}
.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}
.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}
.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}
.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}
.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}
.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}
.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}
.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}
.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}
.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}
.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}
.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}
.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}
.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}
.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}
.jp-RunIcon {
  background-image: var(--jp-icon-run);
}
.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}
.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}
.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}
.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}
.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}
.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}
.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}
.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}
.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}
.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}
.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}
.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}
.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}
.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}
.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}
.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}
.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}
/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}
/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}
/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}
.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}
.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}
.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}
.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}
.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}
.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}
.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}
.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}
/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}
.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}
.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}
.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}
.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}
.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}
.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}
/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

/* CSS for icons in selected items in the settings editor */
#setting-editor .jp-PluginList .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
#setting-editor
  .jp-PluginList
  .jp-mod-selected
  .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected tabs in the sidebar tab manager */
#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable[fill] {
  fill: #fff;
}

#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable[fill] {
  fill: var(--jp-brand-color1);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable-inverse[fill] {
  fill: #fff;
}

/**
 * TODO: come up with non css-hack solution for showing the busy icon on top
 *  of the close icon
 * CSS for complex behavior of close icon of tabs in the sidebar tab manager
 */
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-dirty.jp-mod-active
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: #fff;
}

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) svg {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-border-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0px;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-warn-color0);
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

/* Override Blueprint's _reset.scss styles */
html {
  box-sizing: unset;
}

*,
*::before,
*::after {
  box-sizing: unset;
}

body {
  color: unset;
  font-family: var(--jp-ui-font-family);
}

p {
  margin-top: unset;
  margin-bottom: unset;
}

small {
  font-size: unset;
}

strong {
  font-weight: unset;
}

/* Override Blueprint's _typography.scss styles */
a {
  text-decoration: unset;
  color: unset;
}
a:hover {
  text-decoration: unset;
  color: unset;
}

/* Override Blueprint's _accessibility.scss styles */
:focus {
  outline: unset;
  outline-offset: unset;
  -moz-outline-radius: unset;
}

/* Styles for ui-components */
.jp-Button {
  border-radius: var(--jp-border-radius);
  padding: 0px 12px;
  font-size: var(--jp-ui-font-size1);
}

/* Use our own theme for hover styles */
button.jp-Button.bp3-button.bp3-minimal:hover {
  background-color: var(--jp-layout-color2);
}
.jp-Button.minimal {
  color: unset !important;
}

.jp-Button.jp-ToolbarButtonComponent {
  text-transform: none;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color3);
}

.jp-BPIcon {
  display: inline-block;
  vertical-align: middle;
  margin: auto;
}

/* Stop blueprint futzing with our icon fills */
.bp3-icon.jp-BPIcon > svg:not([fill]) {
  fill: var(--jp-inverse-layout-color3);
}

.jp-InputGroupAction {
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

/* Use our own theme for hover and option styles */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}
select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-top: 1px solid var(--jp-border-color2);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-Collapse-header {
  padding: 1px 12px;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size2);
}

.jp-Collapse-header:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Collapse-contents {
  padding: 0px 12px 0px 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0px;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0px 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px 5px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0px;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty:after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0px 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0px;
  left: 0px;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px;
  padding-bottom: 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0px;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0px 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

.jp-HoverBox.jp-mod-outofview {
  display: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;

  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;

  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #aa00ff;

  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;

  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;

  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;

  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;

  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;

  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;

  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;

  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;

  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;

  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ffff00;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;

  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;

  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;

  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;

  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;

  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eeeeee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;

  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent:before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent:after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0px 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FileDialog-Checkbox {
  margin-top: 35px;
  display: flex;
  flex-direction: row;
  align-items: end;
  width: 100%;
}

.jp-FileDialog-Checkbox > label {
  flex: 1 1 auto;
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  height: 28px;
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  background-color: var(--jp-layout-color1);
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0px 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  height: 32px;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 1;
  overflow-x: auto;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px;
  margin: 0px;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px 6px;
  margin: 0px;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent span {
  padding: 0px;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ body.p-mod-override-cursor *, /* </DEPRECATED> */
body.lm-mod-override-cursor * {
  cursor: inherit !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/* BASICS */

.CodeMirror {
  /* Set height, width, borders, and global font properties here */
  font-family: monospace;
  height: 300px;
  color: black;
  direction: ltr;
}

/* PADDING */

.CodeMirror-lines {
  padding: 4px 0; /* Vertical padding around content */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  padding: 0 4px; /* Horizontal padding of content */
}

.CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  background-color: white; /* The little square between H and V scrollbars */
}

/* GUTTER */

.CodeMirror-gutters {
  border-right: 1px solid #ddd;
  background-color: #f7f7f7;
  white-space: nowrap;
}
.CodeMirror-linenumbers {}
.CodeMirror-linenumber {
  padding: 0 3px 0 5px;
  min-width: 20px;
  text-align: right;
  color: #999;
  white-space: nowrap;
}

.CodeMirror-guttermarker { color: black; }
.CodeMirror-guttermarker-subtle { color: #999; }

/* CURSOR */

.CodeMirror-cursor {
  border-left: 1px solid black;
  border-right: none;
  width: 0;
}
/* Shown when moving in bi-directional text */
.CodeMirror div.CodeMirror-secondarycursor {
  border-left: 1px solid silver;
}
.cm-fat-cursor .CodeMirror-cursor {
  width: auto;
  border: 0 !important;
  background: #7e7;
}
.cm-fat-cursor div.CodeMirror-cursors {
  z-index: 1;
}
.cm-fat-cursor-mark {
  background-color: rgba(20, 255, 20, 0.5);
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
}
.cm-animate-fat-cursor {
  width: auto;
  border: 0;
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
  background-color: #7e7;
}
@-moz-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@-webkit-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}

/* Can style cursor different in overwrite (non-insert) mode */
.CodeMirror-overwrite .CodeMirror-cursor {}

.cm-tab { display: inline-block; text-decoration: inherit; }

.CodeMirror-rulers {
  position: absolute;
  left: 0; right: 0; top: -50px; bottom: 0;
  overflow: hidden;
}
.CodeMirror-ruler {
  border-left: 1px solid #ccc;
  top: 0; bottom: 0;
  position: absolute;
}

/* DEFAULT THEME */

.cm-s-default .cm-header {color: blue;}
.cm-s-default .cm-quote {color: #090;}
.cm-negative {color: #d44;}
.cm-positive {color: #292;}
.cm-header, .cm-strong {font-weight: bold;}
.cm-em {font-style: italic;}
.cm-link {text-decoration: underline;}
.cm-strikethrough {text-decoration: line-through;}

.cm-s-default .cm-keyword {color: #708;}
.cm-s-default .cm-atom {color: #219;}
.cm-s-default .cm-number {color: #164;}
.cm-s-default .cm-def {color: #00f;}
.cm-s-default .cm-variable,
.cm-s-default .cm-punctuation,
.cm-s-default .cm-property,
.cm-s-default .cm-operator {}
.cm-s-default .cm-variable-2 {color: #05a;}
.cm-s-default .cm-variable-3, .cm-s-default .cm-type {color: #085;}
.cm-s-default .cm-comment {color: #a50;}
.cm-s-default .cm-string {color: #a11;}
.cm-s-default .cm-string-2 {color: #f50;}
.cm-s-default .cm-meta {color: #555;}
.cm-s-default .cm-qualifier {color: #555;}
.cm-s-default .cm-builtin {color: #30a;}
.cm-s-default .cm-bracket {color: #997;}
.cm-s-default .cm-tag {color: #170;}
.cm-s-default .cm-attribute {color: #00c;}
.cm-s-default .cm-hr {color: #999;}
.cm-s-default .cm-link {color: #00c;}

.cm-s-default .cm-error {color: #f00;}
.cm-invalidchar {color: #f00;}

.CodeMirror-composing { border-bottom: 2px solid; }

/* Default styles for common addons */

div.CodeMirror span.CodeMirror-matchingbracket {color: #0b0;}
div.CodeMirror span.CodeMirror-nonmatchingbracket {color: #a22;}
.CodeMirror-matchingtag { background: rgba(255, 150, 0, .3); }
.CodeMirror-activeline-background {background: #e8f2ff;}

/* STOP */

/* The rest of this file contains styles related to the mechanics of
   the editor. You probably shouldn't touch them. */

.CodeMirror {
  position: relative;
  overflow: hidden;
  background: white;
}

.CodeMirror-scroll {
  overflow: scroll !important; /* Things will break if this is overridden */
  /* 50px is the magic margin used to hide the element's real scrollbars */
  /* See overflow: hidden in .CodeMirror */
  margin-bottom: -50px; margin-right: -50px;
  padding-bottom: 50px;
  height: 100%;
  outline: none; /* Prevent dragging from highlighting the element */
  position: relative;
}
.CodeMirror-sizer {
  position: relative;
  border-right: 50px solid transparent;
}

/* The fake, visible scrollbars. Used to force redraw during scrolling
   before actual scrolling happens, thus preventing shaking and
   flickering artifacts. */
.CodeMirror-vscrollbar, .CodeMirror-hscrollbar, .CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  position: absolute;
  z-index: 6;
  display: none;
  outline: none;
}
.CodeMirror-vscrollbar {
  right: 0; top: 0;
  overflow-x: hidden;
  overflow-y: scroll;
}
.CodeMirror-hscrollbar {
  bottom: 0; left: 0;
  overflow-y: hidden;
  overflow-x: scroll;
}
.CodeMirror-scrollbar-filler {
  right: 0; bottom: 0;
}
.CodeMirror-gutter-filler {
  left: 0; bottom: 0;
}

.CodeMirror-gutters {
  position: absolute; left: 0; top: 0;
  min-height: 100%;
  z-index: 3;
}
.CodeMirror-gutter {
  white-space: normal;
  height: 100%;
  display: inline-block;
  vertical-align: top;
  margin-bottom: -50px;
}
.CodeMirror-gutter-wrapper {
  position: absolute;
  z-index: 4;
  background: none !important;
  border: none !important;
}
.CodeMirror-gutter-background {
  position: absolute;
  top: 0; bottom: 0;
  z-index: 4;
}
.CodeMirror-gutter-elt {
  position: absolute;
  cursor: default;
  z-index: 4;
}
.CodeMirror-gutter-wrapper ::selection { background-color: transparent }
.CodeMirror-gutter-wrapper ::-moz-selection { background-color: transparent }

.CodeMirror-lines {
  cursor: text;
  min-height: 1px; /* prevents collapsing before first draw */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  /* Reset some styles that the rest of the page might have set */
  -moz-border-radius: 0; -webkit-border-radius: 0; border-radius: 0;
  border-width: 0;
  background: transparent;
  font-family: inherit;
  font-size: inherit;
  margin: 0;
  white-space: pre;
  word-wrap: normal;
  line-height: inherit;
  color: inherit;
  z-index: 2;
  position: relative;
  overflow: visible;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-variant-ligatures: contextual;
  font-variant-ligatures: contextual;
}
.CodeMirror-wrap pre.CodeMirror-line,
.CodeMirror-wrap pre.CodeMirror-line-like {
  word-wrap: break-word;
  white-space: pre-wrap;
  word-break: normal;
}

.CodeMirror-linebackground {
  position: absolute;
  left: 0; right: 0; top: 0; bottom: 0;
  z-index: 0;
}

.CodeMirror-linewidget {
  position: relative;
  z-index: 2;
  padding: 0.1px; /* Force widget margins to stay inside of the container */
}

.CodeMirror-widget {}

.CodeMirror-rtl pre { direction: rtl; }

.CodeMirror-code {
  outline: none;
}

/* Force content-box sizing for the elements where we expect it */
.CodeMirror-scroll,
.CodeMirror-sizer,
.CodeMirror-gutter,
.CodeMirror-gutters,
.CodeMirror-linenumber {
  -moz-box-sizing: content-box;
  box-sizing: content-box;
}

.CodeMirror-measure {
  position: absolute;
  width: 100%;
  height: 0;
  overflow: hidden;
  visibility: hidden;
}

.CodeMirror-cursor {
  position: absolute;
  pointer-events: none;
}
.CodeMirror-measure pre { position: static; }

div.CodeMirror-cursors {
  visibility: hidden;
  position: relative;
  z-index: 3;
}
div.CodeMirror-dragcursors {
  visibility: visible;
}

.CodeMirror-focused div.CodeMirror-cursors {
  visibility: visible;
}

.CodeMirror-selected { background: #d9d9d9; }
.CodeMirror-focused .CodeMirror-selected { background: #d7d4f0; }
.CodeMirror-crosshair { cursor: crosshair; }
.CodeMirror-line::selection, .CodeMirror-line > span::selection, .CodeMirror-line > span > span::selection { background: #d7d4f0; }
.CodeMirror-line::-moz-selection, .CodeMirror-line > span::-moz-selection, .CodeMirror-line > span > span::-moz-selection { background: #d7d4f0; }

.cm-searching {
  background-color: #ffa;
  background-color: rgba(255, 255, 0, .4);
}

/* Used to force a border model for a node */
.cm-force-border { padding-right: .1px; }

@media print {
  /* Hide the cursor when printing */
  .CodeMirror div.CodeMirror-cursors {
    visibility: hidden;
  }
}

/* See issue #2901 */
.cm-tab-wrap-hack:after { content: ''; }

/* Help users use markselection to safely style text background */
span.CodeMirror-selectedtext { background: none; }

.CodeMirror-dialog {
  position: absolute;
  left: 0; right: 0;
  background: inherit;
  z-index: 15;
  padding: .1em .8em;
  overflow: hidden;
  color: inherit;
}

.CodeMirror-dialog-top {
  border-bottom: 1px solid #eee;
  top: 0;
}

.CodeMirror-dialog-bottom {
  border-top: 1px solid #eee;
  bottom: 0;
}

.CodeMirror-dialog input {
  border: none;
  outline: none;
  background: transparent;
  width: 20em;
  color: inherit;
  font-family: monospace;
}

.CodeMirror-dialog button {
  font-size: 70%;
}

.CodeMirror-foldmarker {
  color: blue;
  text-shadow: #b9f 1px 1px 2px, #b9f -1px -1px 2px, #b9f 1px -1px 2px, #b9f -1px 1px 2px;
  font-family: arial;
  line-height: .3;
  cursor: pointer;
}
.CodeMirror-foldgutter {
  width: .7em;
}
.CodeMirror-foldgutter-open,
.CodeMirror-foldgutter-folded {
  cursor: pointer;
}
.CodeMirror-foldgutter-open:after {
  content: "\25BE";
}
.CodeMirror-foldgutter-folded:after {
  content: "\25B8";
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.CodeMirror {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;
  /* Changed to auto to autogrow */
}

.CodeMirror pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* This causes https://github.com/jupyter/jupyterlab/issues/522 */
/* May not cause it not because we changed it! */
.CodeMirror-lines {
  padding: var(--jp-code-padding) 0;
}

.CodeMirror-linenumber {
  padding: 0 8px;
}

.jp-CodeMirrorEditor {
  cursor: text;
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.CodeMirror.jp-mod-readOnly .CodeMirror-cursor {
  display: none;
}

.CodeMirror-gutters {
  border-right: 1px solid var(--jp-border-color2);
  background-color: var(--jp-layout-color0);
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.CodeMirror-selectedtext.cm-searching {
  background-color: var(--jp-search-selected-match-background-color) !important;
  color: var(--jp-search-selected-match-color) !important;
}

.cm-searching {
  background-color: var(
    --jp-search-unselected-match-background-color
  ) !important;
  color: var(--jp-search-unselected-match-color) !important;
}

.CodeMirror-focused .CodeMirror-selected {
  background-color: var(--jp-editor-selected-focused-background);
}

.CodeMirror-selected {
  background-color: var(--jp-editor-selected-background);
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/**
 * Here is our jupyter theme for CodeMirror syntax highlighting
 * This is used in our marked.js syntax highlighting and CodeMirror itself
 * The string "jupyter" is set in ../codemirror/widget.DEFAULT_CODEMIRROR_THEME
 * This came from the classic notebook, which came form highlight.js/GitHub
 */

/**
 * CodeMirror themes are handling the background/color in this way. This works
 * fine for CodeMirror editors outside the notebook, but the notebook styles
 * these things differently.
 */
.CodeMirror.cm-s-jupyter {
  background: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* In the notebook, we want this styling to be handled by its container */
.jp-CodeConsole .CodeMirror.cm-s-jupyter,
.jp-Notebook .CodeMirror.cm-s-jupyter {
  background: transparent;
}

.cm-s-jupyter .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}
.cm-s-jupyter span.cm-keyword {
  color: var(--jp-mirror-editor-keyword-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-atom {
  color: var(--jp-mirror-editor-atom-color);
}
.cm-s-jupyter span.cm-number {
  color: var(--jp-mirror-editor-number-color);
}
.cm-s-jupyter span.cm-def {
  color: var(--jp-mirror-editor-def-color);
}
.cm-s-jupyter span.cm-variable {
  color: var(--jp-mirror-editor-variable-color);
}
.cm-s-jupyter span.cm-variable-2 {
  color: var(--jp-mirror-editor-variable-2-color);
}
.cm-s-jupyter span.cm-variable-3 {
  color: var(--jp-mirror-editor-variable-3-color);
}
.cm-s-jupyter span.cm-punctuation {
  color: var(--jp-mirror-editor-punctuation-color);
}
.cm-s-jupyter span.cm-property {
  color: var(--jp-mirror-editor-property-color);
}
.cm-s-jupyter span.cm-operator {
  color: var(--jp-mirror-editor-operator-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-comment {
  color: var(--jp-mirror-editor-comment-color);
  font-style: italic;
}
.cm-s-jupyter span.cm-string {
  color: var(--jp-mirror-editor-string-color);
}
.cm-s-jupyter span.cm-string-2 {
  color: var(--jp-mirror-editor-string-2-color);
}
.cm-s-jupyter span.cm-meta {
  color: var(--jp-mirror-editor-meta-color);
}
.cm-s-jupyter span.cm-qualifier {
  color: var(--jp-mirror-editor-qualifier-color);
}
.cm-s-jupyter span.cm-builtin {
  color: var(--jp-mirror-editor-builtin-color);
}
.cm-s-jupyter span.cm-bracket {
  color: var(--jp-mirror-editor-bracket-color);
}
.cm-s-jupyter span.cm-tag {
  color: var(--jp-mirror-editor-tag-color);
}
.cm-s-jupyter span.cm-attribute {
  color: var(--jp-mirror-editor-attribute-color);
}
.cm-s-jupyter span.cm-header {
  color: var(--jp-mirror-editor-header-color);
}
.cm-s-jupyter span.cm-quote {
  color: var(--jp-mirror-editor-quote-color);
}
.cm-s-jupyter span.cm-link {
  color: var(--jp-mirror-editor-link-color);
}
.cm-s-jupyter span.cm-error {
  color: var(--jp-mirror-editor-error-color);
}
.cm-s-jupyter span.cm-hr {
  color: #999;
}

.cm-s-jupyter span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}

.cm-s-jupyter .CodeMirror-activeline-background,
.cm-s-jupyter .CodeMirror-gutter {
  background-color: var(--jp-layout-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .remote-caret {
  position: relative;
  border-left: 2px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .remote-caret > div {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -2px;
  font-size: 0.95em;
  background-color: rgb(250, 129, 0);
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 3;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .remote-caret.hide-name > div {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .remote-caret:hover > div {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0px;
  padding: 0px;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}
.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}
.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}
.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}
.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}
.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}
.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}
.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}
.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}
.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}
.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}
.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}
.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}
.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}
.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}
.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}
.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0em;
}

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: 12px;
  table-layout: fixed;
  margin-left: auto;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon table {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0px;
}

.jp-RenderedHTMLCommon p {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}
/* ...or leave it untouched if they don't */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-dark-background {
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-light-background {
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}
.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}
.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}
.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}
.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}
.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}
.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}
.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}
.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: 0.8em;
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser {
  display: flex;
  flex-direction: column;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  border-bottom: none;
  height: auto;
  margin: var(--jp-toolbar-header-margin);
  box-shadow: none;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0px 2px;
  padding: 0px 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0px;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar.jp-Toolbar {
  padding: 0px;
  margin: 8px 12px 0px 12px;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  justify-content: flex-start;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0px;
  padding-right: 2px;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-ToolbarButtonComponent {
  width: 40px;
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent {
  width: 72px;
  background: var(--jp-brand-color1);
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent:focus-visible {
  background-color: var(--jp-brand-color0);
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent
  .jp-icon3 {
  fill: white;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileBrowser-filterBox {
  padding: 0px;
  flex: 0 0 auto;
  margin: 8px 12px 0px 12px;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing:focus-visible {
  border: 1px solid var(--jp-brand-color1);
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px 12px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon:before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon:before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0px;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-DirListing-deadSpace {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
}

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: flex;
  flex-direction: row;
}

body[data-format='mobile'] .jp-OutputArea-child {
  flex-direction: column;
}

.jp-OutputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

body[data-format='mobile'] .jp-OutputPrompt {
  flex: 0 0 auto;
  text-align: left;
}

.jp-OutputArea-output {
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea-child .jp-OutputArea-output {
  flex-grow: 1;
  flex-shrink: 1;
}

body[data-format='mobile'] .jp-OutputArea-child .jp-OutputArea-output {
  margin-left: var(--jp-notebook-padding);
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0px;
  padding: 0px;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0px;
  flex: 1 1 auto;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-OutputArea-stdin {
  line-height: var(--jp-code-line-height);
  padding-top: var(--jp-code-padding);
  display: flex;
}

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;
  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0px;
  bottom: 0px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0px;
  width: 100%;
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: flex;
  flex-direction: row;
  overflow: hidden;
}

body[data-format='mobile'] .jp-InputArea {
  flex-direction: column;
}

.jp-InputArea-editor {
  flex: 1 1 auto;
  overflow: hidden;
}

.jp-InputArea-editor {
  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0px;
  background: var(--jp-cell-editor-background);
}

body[data-format='mobile'] .jp-InputArea-editor {
  margin-left: var(--jp-notebook-padding);
}

.jp-InputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

body[data-format='mobile'] .jp-InputPrompt {
  flex: 0 0 auto;
  text-align: left;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: flex;
  flex-direction: row;
  flex: 1 1 auto;
}

.jp-Placeholder-prompt {
  box-sizing: border-box;
}

.jp-Placeholder-content {
  flex: 1 1 auto;
  border: none;
  background: transparent;
  height: 20px;
  box-sizing: border-box;
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0px;
  margin: 0px;
  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 200px;
  box-shadow: inset 0 0 6px 2px rgba(0, 0, 0, 0.3);
  margin-left: var(--jp-private-cell-scrolling-output-offset);
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  flex: 0 0
    calc(
      var(--jp-cell-prompt-width) -
        var(--jp-private-cell-scrolling-output-offset)
    );
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  flex: 1 1 auto;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

.jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
}

.jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-collapseHeadingButton {
  display: none;
}

.jp-MarkdownCell:hover .jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: 2px;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook-render * {
  contain: none !important;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
  float: left;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt:before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0px;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-NotebookTools-tool {
  padding: 0px 12px 0 12px;
}

.jp-ActiveCellTool {
  padding: 12px;
  background-color: var(--jp-layout-color1);
  border-top: none !important;
}

.jp-ActiveCellTool .jp-InputArea-prompt {
  flex: 0 0 auto;
  padding-left: 0px;
}

.jp-ActiveCellTool .jp-InputArea-editor {
  flex: 1 1 auto;
  background: var(--jp-cell-editor-background);
  border-color: var(--jp-cell-editor-border-color);
}

.jp-ActiveCellTool .jp-InputArea-editor .CodeMirror {
  background: transparent;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0px 12px 0px;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body div {
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>

    <style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0px 2px 1px -1px var(--jp-shadow-umbra-color),
    0px 1px 1px 0px var(--jp-shadow-penumbra-color),
    0px 1px 3px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0px 3px 1px -2px var(--jp-shadow-umbra-color),
    0px 2px 2px 0px var(--jp-shadow-penumbra-color),
    0px 1px 5px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0px 2px 4px -1px var(--jp-shadow-umbra-color),
    0px 4px 5px 0px var(--jp-shadow-penumbra-color),
    0px 1px 10px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0px 3px 5px -1px var(--jp-shadow-umbra-color),
    0px 6px 10px 0px var(--jp-shadow-penumbra-color),
    0px 1px 18px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0px 5px 5px -3px var(--jp-shadow-umbra-color),
    0px 8px 10px 1px var(--jp-shadow-penumbra-color),
    0px 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0px 7px 8px -4px var(--jp-shadow-umbra-color),
    0px 12px 17px 2px var(--jp-shadow-penumbra-color),
    0px 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0px 8px 10px -5px var(--jp-shadow-umbra-color),
    0px 16px 24px 2px var(--jp-shadow-penumbra-color),
    0px 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0px 10px 13px -6px var(--jp-shadow-umbra-color),
    0px 20px 31px 3px var(--jp-shadow-penumbra-color),
    0px 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0px 11px 15px -7px var(--jp-shadow-umbra-color),
    0px 24px 38px 3px var(--jp-shadow-penumbra-color),
    0px 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;

  --jp-ui-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica,
    Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;

  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);

  --jp-content-link-color: var(--md-blue-700);

  --jp-content-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: Menlo, Consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);

  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);

  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);

  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);

  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;

  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;

  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);

  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0px;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0px 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-border-color1);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: #05a;
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #aa22ff;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #aa22ff;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);
}
</style>

<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

.highlight  {
  margin: 0.4em;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.CodeMirror pre {
  margin: 0;
  padding: 0;
}

/* Using table instead of flexbox so that we can use break-inside property */
/* CSS rules under this comment should not be required anymore after we move to the JupyterLab 4.0 CSS */


.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  min-width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-OutputArea-child {
  display: table;
  width: 100%;
}

.jp-OutputPrompt {
  display: table-cell;
  vertical-align: top;
  min-width: var(--jp-cell-prompt-width);
}

body[data-format='mobile'] .jp-OutputPrompt {
  display: table-row;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
}

body[data-format='mobile'] .jp-OutputArea-child .jp-OutputArea-output {
  display: table-row;
}

.jp-OutputArea-output.jp-OutputArea-executeResult {
  width: 100%;
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }

  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}
</style>

<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                CommonHTML: {
                    linebreaks: {
                    automatic: true
                    }
                }
            });

            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
    <!-- End of mathjax configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[26]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">dask.dataframe</span> <span class="k">as</span> <span class="nn">dd</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="n">kaz_2014</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\Kazakhstan_2014\KAZ_2014_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">kaz_2015</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\Kazakhstan_2015\KAZ_2015_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">kaz_2016</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\Kazakhstan_2016\KAZ_2016_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">kaz_2017</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\Kazakhstan_2017\KAZ_2017_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>

<span class="n">pandas_df_kaz_2014</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">kaz_2014</span><span class="p">)</span>
<span class="n">pandas_df_kaz_2015</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">kaz_2015</span><span class="p">)</span>
<span class="n">pandas_df_kaz_2016</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">kaz_2016</span><span class="p">)</span>
<span class="n">pandas_df_kaz_2017</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">kaz_2017</span><span class="p">)</span>

<span class="n">numeric_columns_kaz_2014</span> <span class="o">=</span> <span class="n">pandas_df_kaz_2014</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_kaz_2014</span><span class="p">[</span><span class="n">numeric_columns_kaz_2014</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_kaz_2014</span><span class="p">[</span><span class="n">numeric_columns_kaz_2014</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_kaz_2015</span> <span class="o">=</span> <span class="n">pandas_df_kaz_2015</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_kaz_2015</span><span class="p">[</span><span class="n">numeric_columns_kaz_2015</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_kaz_2015</span><span class="p">[</span><span class="n">numeric_columns_kaz_2015</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_kaz_2016</span> <span class="o">=</span> <span class="n">pandas_df_kaz_2016</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_kaz_2016</span><span class="p">[</span><span class="n">numeric_columns_kaz_2016</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_kaz_2016</span><span class="p">[</span><span class="n">numeric_columns_kaz_2016</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_kaz_2017</span> <span class="o">=</span> <span class="n">pandas_df_kaz_2017</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_kaz_2017</span><span class="p">[</span><span class="n">numeric_columns_kaz_2017</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_kaz_2017</span><span class="p">[</span><span class="n">numeric_columns_kaz_2017</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">dask_df_kaz_2014</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_kaz_2014</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_kaz_2015</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_kaz_2015</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_kaz_2016</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_kaz_2016</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_kaz_2017</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_kaz_2017</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

<span class="n">dask_df_kaz_2014</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\kaz_2014.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_kaz_2015</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\kaz_2015.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_kaz_2016</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\kaz_2016.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_kaz_2017</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\kaz_2017.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

<span class="n">F_ad_Prob_Mod_Sev_kaz_2014</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_kaz_2014</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_kaz_2014</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_kaz_2014</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_kaz_2015</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_kaz_2015</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_kaz_2015</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_kaz_2015</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_kaz_2016</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_kaz_2016</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_kaz_2016</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_kaz_2016</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_kaz_2017</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_kaz_2017</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_kaz_2017</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_kaz_2017</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>

<span class="n">F_ad_Prob_Mod_Sev_kaz_2014</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span>

<span class="n">F_ad_Prob_Mod_Sev_kaz_2015</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span>

<span class="n">F_ad_Prob_Mod_Sev_kaz_2016</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span>

<span class="n">F_ad_Prob_Mod_Sev_kaz_2017</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span>

<span class="n">F_ad_Prob_Mod_Sev_kaz_values</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.0737473506983265</span><span class="p">,</span> <span class="mf">0.044529239425859325</span><span class="p">,</span> <span class="mf">0.07208697980276833</span><span class="p">,</span> <span class="mf">0.09025550050680399</span><span class="p">]</span>

<span class="n">years</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span> <span class="mi">2018</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">6</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">'Казахстан'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">years</span><span class="p">,</span> <span class="n">F_ad_Prob_Mod_Sev_kaz_values</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">'o'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'-'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">years</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">yticks</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mf">0.31</span><span class="p">,</span> <span class="mf">0.05</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA0MAAAIOCAYAAAB6cdbpAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABIiElEQVR4nO3de3yU5Z3///fkNJPTBJKQE4cQAUkCVjAoBIrVKlHselhlYe0W2y1YKWrF7K4liy6HrqVuuxpRofKoK0u7ataf9Yfs0krcWsSCVhGochIrNBpmCCGQyXEymdzfP5IMGWYCmZCECffr+XjMI8w919y5bvFi8s513Z/LYhiGIQAAAAAwmYiL3QEAAAAAuBgIQwAAAABMiTAEAAAAwJQIQwAAAABMiTAEAAAAwJQIQwAAAABMiTAEAAAAwJQIQwAAAABMiTAEAAAAwJQIQwCAc9qwYYMsFos+/PDDgNeee+45WSwWzZkzR62trRehdwAA9B5hCADQK+vWrdMDDzygO++8U6+88oqioqIudpcAAAgJYQgAELL169fr/vvv1x133EEQAgAMWoQhAEBIfvGLX2jRokW67bbb9N///d+Kjo72vVZeXq7bb79dI0aMkM1m09ixY3Xfffepurra7xw//elPlZubq4SEBMXFxWnixIkqLS31a/Phhx/qb//2bzV69GjFxsZq9OjRuvvuu/WXv/zF18YwDN1yyy1KSUlRRUWF73hjY6MmTJigvLw8NTQ0+I4fPHhQd999t9LT02W1WjVq1Cjdc889crvdvuWA53ps2LChx32Tul9iWF1dLYvFohUrVvTmrwAA0Ef4VR4AoMdefPFFfe9739PMmTP16quv+gUhSfrzn/+swsJCLVy4UElJSTp69KiefPJJffWrX9XHH3/saz9u3DitWLFC6enpkqRt27bpH/7hHxQfH697771XknT06FGNHz9ef/u3f6vk5GQ5HA6tW7dOV199tfbv36/U1FRZLBb98pe/1KRJkzR37lxt375d0dHRWrx4sY4cOaL3339f8fHxkqS9e/fqq1/9qlJTU7Vq1SqNGzdODodDb7zxhlpaWvSNb3xDO3fu9F3L4sWLJUlr1671HRszZkyP+wYACH+EIQBAj2zcuFHPPfecYmJidODAAZ06dUppaWl+bRYtWuT7s2EYmj59uq677jplZ2frN7/5jW67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"
class="
"
>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[58]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">dask.dataframe</span> <span class="k">as</span> <span class="nn">dd</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="n">kgz_2014</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\KGZ_2014\KGZ_2014_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">kgz_2015</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\KGZ_2015\KGZ_2015_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">kgz_2016</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\KGZ_2016\KGZ_2016_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">kgz_2017</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\KGZ_2017\KGZ_2017_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>

<span class="n">pandas_df_kgz_2014</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">kgz_2014</span><span class="p">)</span>
<span class="n">pandas_df_kgz_2015</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">kgz_2015</span><span class="p">)</span>
<span class="n">pandas_df_kgz_2016</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">kgz_2016</span><span class="p">)</span>
<span class="n">pandas_df_kgz_2017</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">kgz_2017</span><span class="p">)</span>

<span class="n">numeric_columns_kgz_2014</span> <span class="o">=</span> <span class="n">pandas_df_kgz_2014</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_kgz_2014</span><span class="p">[</span><span class="n">numeric_columns_kgz_2014</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_kgz_2014</span><span class="p">[</span><span class="n">numeric_columns_kgz_2014</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_kgz_2015</span> <span class="o">=</span> <span class="n">pandas_df_kgz_2015</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_kgz_2015</span><span class="p">[</span><span class="n">numeric_columns_kgz_2015</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_kgz_2015</span><span class="p">[</span><span class="n">numeric_columns_kgz_2015</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_kgz_2016</span> <span class="o">=</span> <span class="n">pandas_df_kgz_2016</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_kgz_2016</span><span class="p">[</span><span class="n">numeric_columns_kgz_2016</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_kgz_2016</span><span class="p">[</span><span class="n">numeric_columns_kgz_2016</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_kgz_2017</span> <span class="o">=</span> <span class="n">pandas_df_kgz_2017</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_kgz_2017</span><span class="p">[</span><span class="n">numeric_columns_kgz_2017</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_kgz_2017</span><span class="p">[</span><span class="n">numeric_columns_kgz_2017</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">dask_df_kgz_2014</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_kgz_2014</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_kgz_2015</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_kgz_2015</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_kgz_2016</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_kgz_2016</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_kgz_2017</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_kgz_2017</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

<span class="n">dask_df_kgz_2014</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\kgz_2014.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_kgz_2015</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\kgz_2015.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_kgz_2016</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\kgz_2016.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_kgz_2017</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\kgz_2017.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

<span class="n">F_ad_Prob_Mod_Sev_kgz_2014</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_kgz_2014</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_kgz_2014</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_kgz_2014</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_kgz_2015</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_kgz_2015</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_kgz_2015</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_kgz_2015</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_kgz_2016</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_kgz_2016</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_kgz_2016</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_kgz_2016</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_kgz_2017</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_kgz_2017</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_kgz_2017</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_kgz_2017</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>

<span class="n">F_ad_Prob_Mod_Sev_kgz_values</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.1875365079274166</span><span class="p">,</span> <span class="mf">0.21059007745097164</span><span class="p">,</span> <span class="mf">0.19581301002148638</span><span class="p">,</span> <span class="mf">0.19449654750600165</span><span class="p">]</span>

<span class="n">years</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span> <span class="mi">2018</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">6</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">'Кыргызстан'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">years</span><span class="p">,</span> <span class="n">F_ad_Prob_Mod_Sev_kgz_values</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">'o'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'-'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">years</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">yticks</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mf">0.31</span><span class="p">,</span> <span class="mf">0.05</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA0MAAAIOCAYAAAB6cdbpAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABBYUlEQVR4nO3df3xU1YH///ckmcwkgURIQgIaYog+BMQWDAoJxR9VglitVlmydYu1QpUiKsR2FwRXwCrVqgQsoKwKS10xtepS27QSv7UKJVpFwrZq+7UajaWJ+cGP/CKTSeZ+/khmyDCZJBMSmHBez8djHsycOffOucHj5M059xybZVmWAAAAAMAwEae6AQAAAABwKhCGAAAAABiJMAQAAADASIQhAAAAAEYiDAEAAAAwEmEIAAAAgJEIQwAAAACMRBgCAAAAYCTCEAAAAAAjEYYAANq6datsNpvee++9gPc2bNggm82m2bNnq7W19RS0DgCAgUEYAgAEtWnTJi1atEg33HCDXnjhBUVFRZ3qJgEA0G8IQwCALm3evFl33HGHrr/+eoIQAOC0RBgCAAR4+umntWDBAn3zm9/UL37xC9ntdt97l112mSZMmBD02M8++0w2m01bt271ld1yyy0aMmSIPvjgA11xxRWKi4tTcnKyFi1apKamJr/jbTZbl4+VK1f6nf/RRx8N2oaVK1fKZrP5Xv/zn//UpZdeqpSUFEVHRys1NVU33nij/va3v/kd53K5tHr1ao0bN05Op1OJiYm6/PLLtWfPnm7b5n1cdtllkqTm5mbdc889mjhxohISEjR8+HBlZ2drx44dAW212WxatGhRQPk111yjs88+O+g1AgBOHP/MBwDws2XLFt12222aPn26XnzxRb8gdCLcbreuvvpq3X777Vq6dKn27NmjH//4x/r888/16quv+tWdPXu27rnnHr+ys846q8+fHR0drdmzZ+ucc87R0KFDVVFRoUceeURXXnmlysvLZbPZ1NraqlmzZmnXrl1avHixvv71r6u1tVVvv/22ysvLlZOTo5KSEt85f/Ob3+jHP/6xXn75ZY0cOVKSFB8fL6k9VB08eFA//OEPdeaZZ6qlpUWvv/66brjhBm3ZskU333xzn68FANB/CEMAAJ9t27Zpw4YNio6O1kcffaRDhw5pxIgR/XLulpYW3XPPPbrrrrskSTNmzJDd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"
class="
"
>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[50]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">dask.dataframe</span> <span class="k">as</span> <span class="nn">dd</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="n">uzb_2014</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\UZB_2014\UZB_2014_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">uzb_2015</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\UZB_2015\UZB_2015_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">uzb_2016</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\UZB_2016\UZB_2016_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">uzb_2017</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\UZB_2017\UZB_2017_FIES_v01_EN_M_v01_A_OCS (2).dta'</span>

<span class="n">pandas_df_uzb_2014</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">uzb_2014</span><span class="p">)</span>
<span class="n">pandas_df_uzb_2015</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">uzb_2015</span><span class="p">)</span>
<span class="n">pandas_df_uzb_2016</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">uzb_2016</span><span class="p">)</span>
<span class="n">pandas_df_uzb_2017</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">uzb_2017</span><span class="p">)</span>

<span class="n">numeric_columns_uzb_2014</span> <span class="o">=</span> <span class="n">pandas_df_uzb_2014</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_uzb_2014</span><span class="p">[</span><span class="n">numeric_columns_uzb_2014</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_uzb_2014</span><span class="p">[</span><span class="n">numeric_columns_uzb_2014</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_uzb_2015</span> <span class="o">=</span> <span class="n">pandas_df_uzb_2015</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_uzb_2015</span><span class="p">[</span><span class="n">numeric_columns_uzb_2015</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_uzb_2015</span><span class="p">[</span><span class="n">numeric_columns_uzb_2015</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_uzb_2016</span> <span class="o">=</span> <span class="n">pandas_df_uzb_2016</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_uzb_2016</span><span class="p">[</span><span class="n">numeric_columns_uzb_2016</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_uzb_2016</span><span class="p">[</span><span class="n">numeric_columns_uzb_2016</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_uzb_2017</span> <span class="o">=</span> <span class="n">pandas_df_uzb_2017</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_uzb_2017</span><span class="p">[</span><span class="n">numeric_columns_uzb_2017</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_uzb_2017</span><span class="p">[</span><span class="n">numeric_columns_uzb_2017</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">dask_df_uzb_2014</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_uzb_2014</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_uzb_2015</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_uzb_2015</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_uzb_2016</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_uzb_2016</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_uzb_2017</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_uzb_2017</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

<span class="n">dask_df_uzb_2014</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\uzb_2014.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_uzb_2015</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\uzb_2015.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_uzb_2016</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\uzb_2016.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_uzb_2017</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\uzb_2017.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

<span class="n">F_ad_Prob_Mod_Sev_uzb_2014</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_uzb_2014</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_uzb_2014</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_uzb_2014</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_uzb_2015</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_uzb_2015</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_uzb_2015</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_uzb_2015</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_uzb_2016</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_uzb_2016</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_uzb_2016</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_uzb_2016</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_uzb_2017</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_uzb_2017</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_uzb_2017</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_uzb_2017</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>

<span class="n">F_ad_Prob_Mod_Sev_uzb_2017</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span>

<span class="n">F_ad_Prob_Mod_Sev_uzb_values</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.09872602667454446</span><span class="p">,</span> <span class="mf">0.12482079148104783</span><span class="p">,</span> <span class="mf">0.1033934827101725</span><span class="p">,</span> <span class="mf">0.16342414956949367</span><span class="p">]</span>
<span class="n">years</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span> <span class="mi">2018</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">6</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">'Узбекистан'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">years</span><span class="p">,</span> <span class="n">F_ad_Prob_Mod_Sev_uzb_values</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">'o'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'-'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">years</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">yticks</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mf">0.31</span><span class="p">,</span> <span class="mf">0.05</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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//ov7dixQ3v37vV6fMCAAdq2bZucTud5B6KXX35ZaWlpys3NdXvGyWazea0/a9Ys/fu//7tb2eLFi1VUVHRe7QAA+IYwBADwEBkZqfDwcKWnp+vqq68+Z/2GhgZ9+umnrtfXXXed/uu//kvHjx9XfHy8q3zDhg2KiopSRkaGpNYV1J544gnFxMQoLS3tnF/nZz/7mWtq3MqVK3XfffcpKytL06ZNc6tXW1urf//3f9e9996rUaNGeb3WjBkztHHjRq1fv/68p8pZLBYFBQW5BaHS0lKvq8lJrUGsLUy2iYqKIgwBQDcjDAEAXI4cOaK///3v2rRpk8rLy/XUU0951Jk/f74yMzM1dOhQNTc366233lJubq7bVLQHHnhAr732mq666io9/PDD6tevn9avX68PPvhAq1evdi2ysGjRIr3++uu64oortHjxYl1++eVyOp0qLCzUli1b9Mtf/lITJ0702tZFixbp7bff1g9/+EPt27dP/fr1cx3btGmT4uPj9cgjj7R7r3PnztW6deu0YMECHThwQFdffbWcTqd27typkSNHas6cOR3+//b9739fb7zxhhYuXKiZM2eqqKhIjz32mBITE3Xw4MEOXwcA0L0IQwAAl/fee0/z589XQkKC7rvvPq+roPXr109PPfWUjh49qsDAQKWmpurxxx/X4sWLXXUGDx6sbdu2admyZfr5z38um82mUaNG6eWXX9a//uu/uuqFhYVp69at+vWvf621a9fq0KFDCgkJUUpKir773e+edd8di8Wi9evX6/LLL9eCBQuUk5PjOuZwOLwumnC6gIAAbd68WStXrtTGjRuVnZ2tiIgIfetb39J1113n0/+3f/u3f1NZWZleeOEFvfTSS7rkkku0dOlSHT16VMuXL/fpWgCA7mMxWL4GAAAAgAmxmhwAAAAAUyIMAQAAADAlwhAAAAAAU+pUGFqzZo3S0tIUHBysjIwMbd26td2627Zt09SpUxUTE6OQkBCNGDFCq1at8qj3+uuva9SoUbJarRo1apTefPPNzjQNAAAAADrE5zCUm5urRYsW6cEHH9SePXs0bdo0zZgxQ4WFhV7rh4WF6e6779aHH36oL774Qg899JAeeughrV271lVnx44dmj17tubNm6d9+/Zp3rx5mjVrlnbu3Nn5OwMAAACAs/B5NbmJEydq3Lhxev75511lI0eO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"
class="
"
>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[49]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">dask.dataframe</span> <span class="k">as</span> <span class="nn">dd</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="n">taij_2014</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\TAIJ_2014\TJK_2014_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">taij_2015</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\TAIJ_2015\TJK_2015_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">taij_2016</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\TAIJ_2016\TJK_2016_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>
<span class="n">taij_2017</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\TAIJ_2017\TJK_2017_FIES_v01_EN_M_v01_A_OCS (1).dta'</span>

<span class="n">pandas_df_taij_2014</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">taij_2014</span><span class="p">)</span>
<span class="n">pandas_df_taij_2015</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">taij_2015</span><span class="p">)</span>
<span class="n">pandas_df_taij_2016</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">taij_2016</span><span class="p">)</span>
<span class="n">pandas_df_taij_2017</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_stata</span><span class="p">(</span><span class="n">taij_2017</span><span class="p">)</span>

<span class="n">numeric_columns_taij_2014</span> <span class="o">=</span> <span class="n">pandas_df_taij_2014</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_taij_2014</span><span class="p">[</span><span class="n">numeric_columns_taij_2014</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_taij_2014</span><span class="p">[</span><span class="n">numeric_columns_taij_2014</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_taij_2015</span> <span class="o">=</span> <span class="n">pandas_df_taij_2015</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_taij_2015</span><span class="p">[</span><span class="n">numeric_columns_taij_2015</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_taij_2015</span><span class="p">[</span><span class="n">numeric_columns_taij_2015</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_taij_2016</span> <span class="o">=</span> <span class="n">pandas_df_taij_2016</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_taij_2016</span><span class="p">[</span><span class="n">numeric_columns_taij_2016</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_taij_2016</span><span class="p">[</span><span class="n">numeric_columns_taij_2016</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">numeric_columns_taij_2017</span> <span class="o">=</span> <span class="n">pandas_df_taij_2017</span><span class="o">.</span><span class="n">select_dtypes</span><span class="p">(</span><span class="n">include</span><span class="o">=</span><span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">number</span><span class="p">])</span><span class="o">.</span><span class="n">columns</span>
<span class="n">pandas_df_taij_2017</span><span class="p">[</span><span class="n">numeric_columns_taij_2017</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas_df_taij_2017</span><span class="p">[</span><span class="n">numeric_columns_taij_2017</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="n">dask_df_taij_2014</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_taij_2014</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_taij_2015</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_taij_2015</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_taij_2016</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_taij_2016</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">dask_df_taij_2017</span> <span class="o">=</span> <span class="n">dd</span><span class="o">.</span><span class="n">from_pandas</span><span class="p">(</span><span class="n">pandas_df_taij_2017</span><span class="p">,</span> <span class="n">npartitions</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>

<span class="n">dask_df_taij_2014</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\taij_2014.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_taij_2015</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\taij_2015.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_taij_2016</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\taij_2016.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">dask_df_taij_2017</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span><span class="o">.</span><span class="n">to_excel</span><span class="p">(</span><span class="sa">r</span><span class="s2">"D:\taij_2017.xlsx"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

<span class="n">F_ad_Prob_Mod_Sev_taij_2014</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_taij_2014</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_taij_2014</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_taij_2014</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_taij_2015</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_taij_2015</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_taij_2015</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_taij_2015</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_taij_2016</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_taij_2016</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_taij_2016</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_taij_2016</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
<span class="n">F_ad_Prob_Mod_Sev_taij_2017</span> <span class="o">=</span> <span class="p">(</span><span class="n">dask_df_taij_2017</span><span class="p">[</span><span class="s1">'Prob_Mod_Sev'</span><span class="p">]</span> <span class="o">*</span> <span class="n">dask_df_taij_2017</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">])</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span> <span class="o">/</span> <span class="n">dask_df_taij_2017</span><span class="p">[</span><span class="s1">'wt'</span><span class="p">]</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>

<span class="n">F_ad_Prob_Mod_Sev_taij_2017</span><span class="o">.</span><span class="n">compute</span><span class="p">()</span>

<span class="n">F_ad_Prob_Mod_Sev_taij_values</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.13234311608076732</span><span class="p">,</span> <span class="mf">0.11086727498562164</span><span class="p">,</span> <span class="mf">0.19598527440470287</span><span class="p">,</span> <span class="mf">0.23921461895440915</span><span class="p">]</span>
<span class="n">years</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span> <span class="mi">2018</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">6</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">'Таджикистан'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">years</span><span class="p">,</span> <span class="n">F_ad_Prob_Mod_Sev_taij_values</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">'o'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'-'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">years</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">yticks</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mf">0.31</span><span class="p">,</span> <span class="mf">0.05</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA0MAAAIOCAYAAAB6cdbpAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABWY0lEQVR4nO3deXxU9b3/8fdkm0lCEsjOEpIQwia2YFBIkMUqYbGt1vKTayvWFq9F3IBqBaFFcEGtImLF7apc60OkXvV6rSgEK4uyVBGwyi6BQEzMRnaSTGbO74/AwDgJJCFhJjmv5+ORR8z5fs/J54hfkzff7/kei2EYhgAAAADAZPy8XQAAAAAAeANhCAAAAIApEYYAAAAAmBJhCAAAAIApEYYAAAAAmBJhCAAAAIApEYYAAAAAmBJhCAAAAIApEYYAAAAAmBJhCAAAAIApEYYAwAQsFkuzPtavX+/tUgEAuGACvF0AAKD9bdmyxe3rBx98UJ988on++c9/uh0fNGjQhSwLAACvIgwBgAmMGDHC7euYmBj5+fl5HAcAwExYJgcAcFNTU6M//OEPGjJkiCIiIhQZGan09HS99957jfZfv359k8vuzvTAAw/IZrPp448/9jj3zOV5H3/8sWw2mxYtWuR27g+vd/z4ccXExHicP3bsWI0dO9at79y5cxUYGKj/+Z//cR27+eablZSU5Nbv4MGDstlsslgsOnz4sFvbG2+8ofT0dHXp0kVdunTRkCFD9PLLL7u+57mWIJ7y7LPPavTo0YqNjVVoaKguvvhiPf7447Lb7W7fb+zYsRo8eLB+6Iknnmi0PgBAyzEzBABwU1tbq5KSEt1zzz3q2bOn6urqtG7dOl133XV69dVXddNNNzV63iOPPKIrrrhCkvTkk0+6BQ+pIdCUl5frmmuu0bp16xqdldqyZYuuueYazZgxQ3/+85/PWue8efN0/Pjxc97P/fffryeeeEIrV67U5MmTz9r3rrvuUn19vcfxP//5z3rwwQd13XXX6Q9/+IMiIiL09ddf68iRI5Kk5cuXq7y8XJKUl5en6667TvPnz9fVV1/tca1vv/1Wv/rVr5ScnKygoCDt2rVLDz/8sPbu3atXXnnlnPcDAGg7hCEAgJuIiAi9+uqrrq8dDoeuvPJKHT9+XEuXLvUIQ7W1tZKkAQMGuAJOXFxco9d+8sknVV5erkmTJnls1rBr1y5NmjRJ//Ef/6ElS5actcYdO3bohRde0B133KFly5Y12W/evHn6y1/+0qwg9N5772nNmjWaMWOG/vrXv7qOZ2dn65FHHtGvf/1rvf76667j48aNc/3zmc9anZqxSUlJaTTwnXlvTqdTo0aNUlRUlH7729/qySefVLdu3c5aJwCg7bBMDgDg4a233tLIkSPVpUsXBQQEKDAwUC+//LL27Nnj0beyslKSFBIScs7rWiwWvfDCCwoNDVVmZqYOHDggSdq/f78yMzPVpUsXvfDCC2e9hmEYmjFjhsaNG6df/OIXTfabP3++HnnkEc2aNeucQejEiROaOXOmbr31VqWlpbm1ZWVlyeFw6Pbbbz/n/TXHjh079POf/1xRUVHy9/dXYGCgbrrpJjkcDu3fv9+jf319vduH0+lskzoAAIQhAMAPvPPOO7r++uvVs2dPvf7669qyZYs+//xz/e53v1NNTY1H/9zcXElSjx49mnX9l19+WXl5eUpJSdEdd9whSbrzzjvVt29f5eXlnXOp2Kuvvqovv/xSzzzzTJN9tmzZoscee0yXX365XnrpJR09evSs11y8eLEqKyv18MMPe7QVFhZKknr16nWuWzunnJwcjRo1Srm5uXr66ae1adMmff7553r22WclNYSyM33zzTcKDAx0+7jvvvvOuw4AQAPCEADAzeuvv67k5GStWrVK1157rUaMGKFhw4a5lsP90K5du2Sz2ZSamnrOax8+fFj33HOP/vjHP+rjjz9WRkaGJCkjI0Mff/yx7r33Xv3hD39wPYvzQ6WlpZozZ47uvffes34/p9OplStX6qOPPlJMTIxuvPHGJmdUvv32Wz3++ONavHixIiMjPdpjYmIkSceOHTvn/Z3L//7v/6qqqkrvvPOObrzxRl1++eUaNmyYgoKCGu2fkpKizz//3O3j7rvvPu86AAANCEMAADcWi0VBQUFuO6Dl5+c3uptcfX29PvzwQ1111VWy2Wxnva5hGPrd736npKQk185yCxYskCQtWLBANptNCxcuVFJSkn7729/KMAyPa8yfP1/BwcG6//77z/q9Ro4cqcmTJys0NFSvv/66Nm/erEcffbTRvnfffbd+/OMfa9q0aY22Z2Zmyt/fX88999xZv2dznPp3arVaXccMw9BLL73UaH+bzaZhw4a5fbTFDBUAoAEbKAAA3Pz0pz/VO++8oxkzZmjy5Mk6evSoHnzwQXXv3t31jI/UMKPy0EMPKS8vT2PHjtXWrVtdbd9//70kaevWrRo6dKisVqv++te/6tNPP9W2bduanAkJCgrSf//3f2v48OF69tlnXcvoTnn++ef11ltvNev5pFMuu+wyLViwQAsWLNBVV12lyy67zNV27NgxHT16VNu2bfPYuvuUpKQk3X///XrwwQd14sQJ3XDDDYqIiNDu3btVVFSkhQsXNruWcePGKSgoSDfccIP++Mc/qqamRs8991yzdsUDALQ9whAAwM1vf/tbFRQU6Pnnn9crr7yiPn36aM6cOTp27JjbL/4PPvig/vu//1uSdM899zR6rfT0dGVnZ6u+vl5z5szR/PnzNXTo0LN+/6FDh2revHm67777NGHCBPXt29fVdtVVV51104SmzJ07V2vWrNGvf/1r7dixQ126dJHUsFPe73//ew0bNuys5y9atEipqal65pln9Otf/1oBAQFKTU3VXXfd1aI6BgwYoLffflvz58/Xddddp6ioKP3qV7/S7NmzNXHixBbfFwDg/FiMxtYhAABwDjfffLMkacWKFU32sVgsys7O9ni5KQAAvoCZIQBAq6SkpJyzz/Dhw92ejwEAwJcwMwQAAADAlFq1m9zy5cuVnJwsm82mtLQ0bdq0qcm+n376qUaOHKmoqCgFBwdrwIABeuqppzz6vf322xo0aJCsVqsGDRqkd999tzWlAQAAAECztDgMrVq1SjNnztS8efO0Y8cOjRo1ShMnTlROTk6j/UNDQ3XHHXdo48aN2rNnj+bPn6/58+frxRdfdPXZsmWLpkyZoqlTp2rXrl2aOnWqrr/+em3btq31dwYAAAAAZ9HiZXLDhw/XJZdc4va+hYEDB+raa6/V4sWLm3WN6667TqGhofrb3/4mSZoyZYrKy8v14YcfuvpMmDBB3bp108qVK1tSHgAAAAA0S4s2UKirq9P27ds1Z84ct+OZmZnavHlzs66xY8cObd68WQ899JDr2JYtWzRr1iy3fuPHj9fSpUubvE5tba3b29CdTqdKSkoUFRXV5LsiAAAAAHR+hmGooqJCPXr0kJ9f04vhWhSGioqK5HA4FBcX53Y8Li5O+fn5Zz23V69eKiwsVH19vR544AHdcsstrrb8/PwWX3Px4sUtetEdAAAAAHM5evSoevXq1WR7q7bW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b9z6vPjiixo7dqzCw8NlsVhUWlra5Pesra3VkCFDZLFYtHPnzna4K6DzuZBjNSkpSRaLxe1jzpw57Xl7QKdxoX+ufvDBBxo+fLiCg4MVHR2t6667rr1uDehULtRYXb9+vcfP1FMfn3/+eXvfphvCUCM2bNig22+/XVu3blVWVpbq6+uVmZmpqqoqV5/HH39cS5Ys0V//+ld9/vnnio+P17hx41RRUeHqU11drQkTJuj+++8/5/f84x//qB49erTL/QCd1YUeq6deKXDqY/78+e12b0BnciHH6ttvv62pU6fqt7/9rXbt2qXPPvtMv/rVr9r1/oDO4kKN1YyMDLefp3l5ebrllluUlJSkYcOGtft9ujFwTgUFBYYkY8OGDYZhGIbT6TTi4+ONRx991NWnpqbGiIiIMJ5//nmP8z/55BNDknH8+PFGr7969WpjwIABxjfffGNIMnbs2NEetwF0eu05VhMTE42nnnqqvUoHTKW9xqrdbjd69uxp/Nd//Ve71g+YRXv/DnxKXV2dERsbayxatKhN628OZoaaoaysTJIUGRkpScrOzlZ+fr4yMzNdfaxWq8aMGaPNmze36Nrff/+9/vM//1N/+9vfFBIS0nZFAybUnmNVkh577DFFRUVpyJAhevjhh1VXV9c2hQMm015j9csvv1Rubq78/Pw0dOhQde/eXRMnTvRYwgOgedr75+op//d//6eioiLdfPPN51VvaxCGzsEwDM2ePVuXX365Bg8eLEnKz8+XJMXFxbn1jYuLc7U199o333yzpk+ffuGnBIFOpj3HqiTdfffdevPNN/XJJ5/ojjvu0NKlSzVjxoy2KR4wkfYcq4cOHZIkPfDAA5o/f77+8Y9/qFu3bhozZoxKSkra6A4Ac2jvn6tnevnllzV+/HglJCS0vuBWCrjg37GDueOOO/TVV1/p008/9WizWCxuXxuG4XHsbJ555hmVl5dr7ty5510nYHbtOVYladasWa5//tGPfqRu3bpp8uTJrtkiAM3TnmPV6XRKkubNm6df/vKXkqRXX31VvXr10ltvvaXf//7351E5YC7t/XP1lGPHjmnNmjX6+9//3qrzzxczQ2dx55136v/+7//0ySefqFevXq7j8fHxkuSRgAsKCjyS8tn885//1NatW2W1WhUQEKC+fftKkoYNG6bf/OY3bXAHgDm091htzIgRIyRJBw8ePK/rAGbS3mO1e/fukqRBgwa5jlmtVvXp00c5OTnnUzpgKhfy5+qrr76qqKgo/fznP299weeBMNQIwzB0xx136J133tE///lPJScnu7UnJycrPj5eWVlZrmN1dXXasGGDMjIymv19li1bpl27dmnnzp3auXOnVq9eLUlatWqVHn744ba5GaATu1BjtTE7duyQdPqXLwBNu1BjNS0tTVar1W0rYLvdrsOHDysxMfH8bwTo5C70z1XDMPTqq6/qpptuUmBg4HnX3xosk2vE7bffrjfeeEPvvfeewsLCXOk3IiJCwcHBslgsmjlzph555BGlpqYqNTVVjzzyiEJCQty278zPz1d+fr7rb47//e9/KywsTL1791ZkZKR69+7t9n27dOkiSUpJSXFL4QAad6HG6pYtW7R161ZdccUVioiI0Oeff65Zs2bp5z//ucc4BuDpQo3V8PBwTZ8+XQsWLFBCQoISExP1l7/8RZL0//7f/7vwNw50MBdqrJ7yz3/+U9nZ2Zo2bdqFvdEzXfD96zoASY1+vPrqq64+TqfTWLBggREfH29YrVZj9OjRxr///W+36yxYsOCc1zlTdnY2W2sDLXChxur27duN4cOHGxEREYbNZjP69+9vLFiwwKiqqrqAdwt0XBfy52pdXZ3xhz/8wYiNjTXCwsKMq666yvj6668v0J0CHduF/h34hhtuMDIyMi7AnTXNYhiG0S4pCwAAAAB8GM8MAQAAADAlwhAAAAAAUyIMAQAAADAlwhAAAAAAUyIMAQAAADAlwhAAAAAAUyIMAQAAADAlwhAAAAAAUyIMAQAAADAlwhAAAAAAUyIMAQAAADAlwhAAAAAAU/r/Rv5Q6jvbBeoAAAAASUVORK5CYII="
class="
"
>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[59]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">6</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">years</span><span class="p">,</span> <span class="n">F_ad_Prob_Mod_Sev_kaz_values</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">'o'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'-'</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">'Казахстан'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">years</span><span class="p">,</span> <span class="n">F_ad_Prob_Mod_Sev_uzb_values</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">'o'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'-'</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">'Узбекистан'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">years</span><span class="p">,</span> <span class="n">F_ad_Prob_Mod_Sev_kgz_values</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">'o'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'-'</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">'Кыргызстан'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">years</span><span class="p">,</span> <span class="n">F_ad_Prob_Mod_Sev_taij_values</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s1">'o'</span><span class="p">,</span> <span class="n">linestyle</span><span class="o">=</span><span class="s1">'-'</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">'Таджикистан'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">'Центральная Азия'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">years</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">yticks</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mf">0.3</span><span class="p">,</span> <span class="mf">0.05</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA0MAAAIOCAYAAAB6cdbpAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAC1g0lEQVR4nOzdd3icxb328e82da16tyX3blxxwUAMuMkJ6cEnJJQEklBOguOTEzDdEGx4c0JNICQhcQiBcDgkISQWtmkBgymuFBt3y0W9rvq25/3jkVZaS7YlW9Kq3B+uvWTNzj6aNZa0987MbyyGYRiIiIiIiIgMMtZQD0BERERERCQUFIZERERERGRQUhgSEREREZFBSWFIREREREQGJYUhEREREREZlBSGRERERERkUFIYEhERERGRQUlhSEREREREBiWFIRERERERGZQUhkRE+pi1a9disVjYsmVLh/d/4QtfYNiwYb07KOkxHo+H9PR0LBYL//d//xfq4YiIDCoKQyIiIiH0z3/+k+LiYgCeeuqpEI9GRGRwURgSEREJoaeeeoqwsDAWLlzIhg0bOHbsWKiHJCIyaCgMiYgMEFu2bOGLX/wiiYmJREREMG3aNP73f/83qM/JluCVlZVhsVi4++67Abj77ruxWCynvL355psAzJ8/n0mTJvH2228zZ84cIiMjycrK4o477sDn8wV9nVWrVjF79mwSExNxOp1Mnz6dp556CsMw2j2fN998s8Ov23aJYEuf0y0v6+zzBti/fz/f+c53GD16NFFRUWRlZXHppZfy8ccft7vuhx9+yJIlS0hNTcVqtXY4xlMpKCjglVde4dJLL+W///u/8fv9rF27tl2///qv/2LkyJFERUXhdDqZOXMmzzzzTFCf+fPnM3/+/KC2t99+OzCmtoqKivjud7/L0KFDsdvtQX+/hw8f7tTYRUQGAnuoByAiImfvjTfeYMmSJcyePZtf//rXxMXF8Ze//IVly5ZRX1/P1Vdf3aXrXXvttSxZsiTw+Ve+8hWmT5/OHXfcEWibMGFC4M9FRUX8x3/8B7fccgv33HMP//rXv/jZz35GZWUlv/zlLwP9Dh8+zA9+8AOys7MBeO+99/jhD3/I8ePHufPOOzscy69+9SumT58OwL333sunn37apefSVQUFBSQlJXH//feTkpJCRUUFf/zjH5k9ezbbt29n7NixANTV1bFkyRKSk5N57LHHyM7OxmKx8JOf/KTTsztr167F5/Px3e9+lwULFpCTk8Pvf/97brvttqAAM3XqVObOnUtqaipNTU384x//4IorriAtLY2FCxd2eG2fz8eNN96IzWZrF0qvuuoq3nnnHR544AGmTJmC3W7n2Wef5bHHHjvDvzURkf5JYUhEZAC44YYbmDhxIq+//jp2u/mjffHixZSVlXHrrbdy5ZVXYrV2fjHAkCFDGDJkSODz8PBwUlJSmDNnTof9y8vLeemll/jiF78IwKJFi2hoaOCJJ57gpz/9aSD8/OEPfwg8xu/3M3/+fAzD4JFHHuGOO+4ICgButxuAc845J/B1U1JSOv0cztSFF17IhRdeGPjc5/Px+c9/nokTJ/Lkk0/y4IMPArB7924qKir4+c9/zrJlywL94+PjOxWGDMPgD3/4A1lZWSxevBiLxcLVV1/NqlWreOONN7j44osDfa+44goMw8Dn81FfX095eTm//OUv+fTTT08ahn75y19y8OBBrrrqKn7/+98H3ffOO+/w1a9+lRtvvDHQtmnTps79BYmIDCBaJici0s/t37+fzz77jG9961sAeL3ewG3p0qUUFhayZ8+eoMf4fL6gfifOHHRVbGxsIAi1uPzyy/H7/bz11luBttdff50FCxYQFxeHzWbD4XBw5513Ul5eTklJSdDjGxoaAIiIiDjt1/f7/Xi9Xvx+/yn7deZ5e71eVq9ezYQJEwgLC8NutxMWFsa+ffvYvXt3oF92djYOh4Nnn32WgwcP4vF48Hq9HS7568i///1v9u/fz1VXXYXNZgPgO9/5DhaLpV14AXjppZdwOBzExcXxzW9+k2nTpgX+n5+ouLiYu+66izvuuIOhQ4e2u3/UqFG8/vrrvP/++zQ2Nnbq705EZCBSGBIR6edaKpH95Cc/weFwBN1uuOEGwNwb09acOXOC+qWnp5/VGNLS0tq1tVyzvLwcgA8++IBFixYB8Nvf/pZ33nmHDz/8kNtuuw1oDT8tWsacnJx82q+/bNkyHA4HdrudtLQ0/uM//qPDvS+ded4rVqzgjjvu4Mtf/jIvv/wy77//Ph9++CFTpkwJGmNqaip/+tOf2Lt3LyNHjiQsLAyHw8G6detOO15orRz3la98haqqKqqqqoiLi+P888/nxRdfpKqqKqj//Pnz+fDDD3nllVf4zne+Q25uLrGxsR1e+7//+79JT0/nxz/+cYf3//GPfyQzMzOwx8vhcHDzzTd3atwiIgOJlsmJiPRzLWFh5cqVfPWrX+2wT8s+lxZPP/0048ePD3xeXV3NggULzngMLYGsraKiIgCSkpIA+Mtf/oLD4eCf//xn0GzP3//+9w6vuW/fPiIiIoKW653MAw88wMUXX4zP52P37t389Kc/5ctf/jI7duwI6teZ5/3MM89w5ZVXsnr16qD2srIy4uPjg9qWLVuG1+vliiuu4Omnn2bcuHH8+Mc/5ujRo6ccb3V1NS+++CIA5557bod9nn322UCYBXP53cyZMwFzGeLo0aPxer088MADQY/btGkTzzzzDOvXrycsLKzDa0+ZMoU///nPTJ06leuuu45vfvObPPPMMzzyyCOnHLeIyECjMCQi0s+NHTuW0aNHs3PnznYv4E9m/PjxgRfW0H7mqKtqamr4xz/+EbRU7tlnn8VqtQb231gsFux2e2BJGJizQX/605/aXc/j8bBu3Trmzp0b2AN1KiNGjAg8n9mzZ7Nz504efvhhmpqaCA8PD/TrzPO2WCxBjwH417/+xfHjxxk1alRQ+5EjR7jxxhtZvnw53/72twGIi4s7bRh69tlnaWho4N577+X8889vd/83vvENfv/73weFoba8Xi9ut7tdhTufz8d//ud/8rWvfe2ke4laHv+tb32LSZMm8cADD2C32wPVAUVEBhOFIRGRPur111/vcKlXUVER9fX1/N///R+f+9znSElJ4cknnyQ3N5fFixdz9dVXk5WVRUVFBbt372bbtm288MILPTrWpKQkrr/+eo4cOcKYMWNYt24dv/3tb7n++usDxRM+//nP8+CDD3L55Zfz/e9/n/Lycv7nf/6nXfB48803WbNmDZ988gl5eXmd+voFBQV89tln+Hw+9u7dywsvvMDUqVPbXbszvvCFL7B27VrGjRvHOeecw9atW/n5z3/ebobK7/dzxRVXkJ2dzZo1a7r0NZ566ikSEhL4yU9+0uGeqCuvvJIHH3yQnTt3kpWVxQ9/+EO+8IUvMGTIEMrKynjiiSc4evQot956a9DjNm/eTEREBC+//PIpv/7dd9/Nrl272L59e6fCpojIQKWfgCIifdTp9nB84xvf4I033mD+/PlcdNFFfPDBB9x3330sX76cyspKkpKSmDBhApdddlmP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2JOSOn1Ni81G1LnnUlNaStS55/abIAQKQyIiIiIiA5q3spKajRtx5eVR//4H4PcH7oucNs1cArd4MY601BCOMjQUhkREREREBhify0XNq6/hysujbvNm8HoD90VMnowzNxfnksU4MjNDOMrQUxgSERERERkAfLV11L7xhhmA3n4bw+MJ3Bc+bhzOpUtx5i4hbOjQEI6yb1EYEhERERHpp/wNDdT++9+41uVR++9/B537EzZqpDkDlLuU8BHDQzjKvkthSERERESkH/E3NVH39tu41uVR8+abGPX1gfvCcnKIXZqLMzeXiDFjQjjK/kFhSERERESkjzPcbmrffZeavDxqXnsdf21t4D5HVhbO5gAUPn48luZDT+X0FIZERERERPogw+ul7v33ceXlUbPxVfzV1YH77OnpOJcswbk0l4jJkxWAzpDCkIiIiIhIH2H4fNRv2Yorbx01Gzbiq6gI3GdLTsa5eDHOpblETpuGxWoN4UgHBoUhEREREZEQMvx+GnbswLUuD9f6V/CVlgXusyUkELtoEc7cXKLOndmvDjTtDxSGRERERER6mWEYNH78cXMAWo+3sDBwn9XpJHbhApy5S4meMxuLXS/Ze4r+ZkVEREREeoFhGDTt3o0rLw9X3it4jh0L3GeNjiZ2wSXE5uYSc955WMLCQjjSwUNhSERERESkBzXt22cGoHV5uA8fDrRbIiOJvWi+GYAuvBBreHjIxjhYKQyJiIiIiHSzpkOHzCpweXk07dsfaLeEhxNz4YU4l+YS87nPYY2KCuEoRWFIRERERKQbuI8dM/cA5eXRtHt36x0OBzHnn28GoIsuxhYTHbpBShCFIRERERGRM+QpLMSV9wquvDwaP/649Q6bjejzzsOZm0vsgkuwOZ2hG6SclMKQiIiIiEgXeEpKqFm/AVdeHg3btrXeYbUSNWuWGYAWLcSekBC6QUqnKAyJiIiIiJyGt6KCmg0bcK3Lo/7DD8EwzDssFiJnTMeZm4tz8WLsycmhHah0icKQiIiIiEgHfFVV1Lz6Kq51edS9/z74fIH7IqdMwbk0l9glS3CkpYVwlHI2FIZERERERJr5amqoee01XHl51L27GTyewH0REybg/PxSnEuW4MjKCuEopbsoDImIiIjIoOavq6PmzTfNAPTW2xhud+C+8DFjcC7NxZmbS1hOTghHKT1BYUhERERE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fD2bN29m165duLu74+LiQlhYGACRkZEMGjSoHHog4hgqeqwWp127dgD8/PPPt1SPiCOp6LFat25dAMLDw61p7u7uhIaGkpycfCtNF3Eolfm5umTJEmrVqsUjjzxy8w2+BQqGimGxWBgxYgSffvopmzdvJiQkxOZ4SEgIgYGBJCQkWNNyc3PZsmULUVFRpT7PnDlzOHjwIImJiSQmJhIfHw/AihUrmD59evl0RqQaq6yxWpwDBw4A//3jS0RKVlljtVWrVri7u9ssBZyXl8eJEycIDg6+9Y6IVHOV/blqsVhYsmQJzzzzDK6urrfc/puhy+SK8cILL/DRRx/x+eef4+3tbY1+TSYTnp6eGAwGRo0axRtvvEGTJk1o0qQJb7zxBl5eXjbLd6amppKammr95vjQoUN4e3vTsGFDatasScOGDW3OazQaAWjcuLFNFC4ixaussbpz50527dpF586dMZlM7Nmzh9GjR/PII4/YjWMRsVdZY9XHx4dhw4YRExNDgwYNCA4O5q233gLg8ccfr/yOi9xhKmusFtm8eTNJSUn89a9/rdyOXqvS16+7AwDFbkuWLLHmMZvNlpiYGEtgYKDF3d3d8sADD1gOHTpkU09MTMwN67lWUlKSltYWKYPKGqv79u2ztG3b1mIymSweHh6Wu+66yxITE2O5dOlSJfZW5M5VmZ+rubm5lrFjx1rq1Klj8fb2tnTt2tXyn//8p5J6KnJnq+y/gQcMGGCJioqqhJ6VzGCxWCwVEmWJiIiIiIhUYbpnSEREREREHJKCIRERERERcUgKhkRERERExCEpGBIREREREYekYEhERERERBySgiEREREREXFICoZERERERMQhKRgSERERERGHpGBIREREREQckoIhERERERFxSAqGRERERETEISkYEhERERERh/T/AebYQBOmFnlpAAAAAElFTkSuQmCC"
class="
"
>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

     </div>
</div>
</div>
</div>

</div>
</body>







</html>
