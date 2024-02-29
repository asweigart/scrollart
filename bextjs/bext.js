/*
BextJS by Al Sweigart al@inventwithpython.com
https://github.com/asweigart/bextjs
*/

// TODO - create BextJS objects so pages can have multiple terminals.
// TODO - add color? add goto()? Change size? Print emojis?
/*
When calling input(), you must call it with await:
    await input();
Otherwise, the entire page will freeze. Also, any function that calls input()
must itself be called with an await or else it will be skipped over.

When calling sleep(), you must call it with await:
    await sleep(2);
Or else it will not pause the program. Also, any function that calls input()
must itself be called with an await or else the program won't pause.
*/

"use strict";

let bextRowBufferSize = 256;  // 256 was selected arbitrarily.

function _countNewlines(str) {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === '\n') {
            count++;
        }
    }
    return count;
}


function _truncateForRowBuffer(bextOutputElem, rowBufferSize) {
    if (rowBufferSize === null) {
        return;  // a null row buffer size means never truncate
    }

    let totalNewlines = _countNewlines(bextOutputElem.value);
    if (totalNewlines >= bextRowBufferSize) {
        let newlineCount = 0;
        let cutAt = 0;
        for (cutAt = 0; cutAt < bextOutputElem.value.length; cutAt++) {
            if (bextOutputElem.value[cutAt] === '\n') {
                if (newlineCount == totalNewlines - bextRowBufferSize) {
                    break;
                } else {
                    newlineCount++;
                }
            }
        }
        bextOutputElem.value = bextOutputElem.value.substring(cutAt + 1);
    }
}


// These are the global print(), input(), clear(), and sleep() functions:
function print() {
    const bextOutputElem = document.getElementById("bextOutput");

    if (bextOutputElem === null) {
        throw "print() has been called but bextOutput element does not exist.";
    }
    var args = Array.prototype.slice.call(arguments);
    var newline = "\n";
    if (args.length !== 1 && args[args.length - 1] == "") {
        // If the last argument is a blank string, suppress the newline character we automatically add to the end.
        newline = "";
    }

    bextOutputElem.value = bextOutputElem.value + args.join("") + newline;
    _truncateForRowBuffer(bextOutputElem, bextRowBufferSize);
    bextOutputElem.scrollTop = bextOutputElem.scrollHeight; // Scroll to the bottom of the text field.
}

function input() {
    // Wait for the user to type something into the input text field and press Enter. Return this string.
    const bextInputElem = document.getElementById("bextInput");

    if (bextInputElem === null) {
        throw "input() has been called but bextInput element does not exist.";
    }

    bextInputElem.readOnly = false;
    bextInputElem.focus();

    return new Promise((resolve) => {
        function handleKeypress(e) {
            if (e.key === "Enter") {
                print(e.target.value);
                resolve(e.target.value);
                e.target.value = "";  // Blank the input text field
                bextInputElem.removeEventListener('keypress', handleKeypress)
                bextInputElem.readOnly = true;
            }
        }
        bextInputElem.addEventListener('keypress', handleKeypress)
    });
}

function sleep(delayInMilliseconds) {
    // Pause the program.
    return new Promise(resolve => setTimeout(resolve, delayInMilliseconds));
}

function clear() {
    // Erase all the text in the bextOutput text field:
    const bextOutputElem = document.getElementById("bextOutput");
    if (bextOutputElem === null) {
        throw "clear() has been called but bextOutput element does not exist.";
    }
    document.getElementById("bextOutput").value = "";
}

/*
function _getWidthInColumns(textarea) {
    // Get the font size of the textarea
    var computedStyle = window.getComputedStyle(textarea);
    var fontSize = parseFloat(computedStyle.fontSize);

    // Create a temporary span element to calculate the width
    var tempSpan = document.createElement('span');
    tempSpan.style.visibility = 'hidden';
    tempSpan.style.whiteSpace = 'pre'; // Preserve spaces
    tempSpan.textContent = textarea.value || textarea.placeholder || '';

    // Append the span to the document body to get accurate width calculations
    document.body.appendChild(tempSpan);
    var widthInPixels = tempSpan.offsetWidth;
    document.body.removeChild(tempSpan);

    // Convert the width from pixels to character columns
    var widthInColumns = Math.floor(widthInPixels / fontSize);

    return widthInColumns;
}

function bextWidth() {
    // Return the width of the bextOutput text field in character columns:
    const bextOutputElem = document.getElementById("bextOutput");

    if (bextOutputElem === null) {
        throw "print() has been called but bextOutput element does not exist.";
    }
    
    return _getWidthInColumns(bextOutputElem);
}
*/

// Clear the output and input text fields:
if (document.getElementById("bextOutput") !== null) {
    clear();
}






class Bext {
    constructor(bextOutput=null, bextInput=null, bextRowBufferSize=256) {
        this.bextOutput = bextOutput;
        this.bextInput = bextInput;
        this.bextRowBufferSize = bextRowBufferSize;

        this.bextOutputElem = document.getElementById(this.bextOutput);
        this.bextInputElem = document.getElementById(this.bextInput);

        if (this.bextOutputElem !== null) {
            this.bextOutputElem.readOnly = true;
        }
        if (this.bextInputElem !== null) {
            this.bextInputElem.readOnly = true; 
        }
        this.clear();
    }

    print() {
        if (this.bextOutputElem === null) {
            throw "print() has been called but this.bextOutputElem does not exist.";
        }

        let args = Array.prototype.slice.call(arguments);
        let newline = "\n";
        if (args.length !== 1 && args[args.length - 1] == "") {
            // If the last argument is a blank string, suppress the newline character we automatically add to the end.
            newline = "";
        }

        this.bextOutputElem.value = this.bextOutputElem.value + args.join("") + newline;
        _truncateForRowBuffer(this.bextOutputElem, this.bextRowBufferSize);
        this.bextOutputElem.scrollTop = this.bextOutputElem.scrollHeight; // Scroll to the bottom of the text field.
    }

    input() {
        if (this.bextInputElem === null) {
            throw "input() has been called but this.bextInputElem does not exist.";
        }

        // Wait for the user to type something into the input text field and press Enter. Return this string.
        this.bextInputElem.readOnly = false;
        this.bextInputElem.focus();

        let that = this;
        return new Promise((resolve) => {
            function handleKeypress(e) {
                if (e.key === "Enter") {
                    that.print(e.target.value);
                    resolve(e.target.value);
                    e.target.value = "";  // Blank the input text field
                    that.bextInputElem.removeEventListener('keypress', handleKeypress)
                    that.bextInputElem.readOnly = true;
                }
            }
            this.bextInputElem.addEventListener('keypress', handleKeypress)
        });
    }

    // TODO - Does this delay all JS code on the page?
    sleep(delayInMilliseconds) {
        // Pause the program.
        return new Promise(resolve => setTimeout(resolve, delayInMilliseconds));
    }

    clear() {
        // Erase all the text in the output text field:
        if (this.bextOutputElem === null) {
            throw "clear() has been called but this.bextOutputElem does not exist.";
        }
        this.bextOutputElem.value = "";
    }

/*
    bextWidth() {
        if (this.bextOutputElem === null) {
            throw "print() has been called but bextOutput element does not exist.";
        }
        
        return _getWidthInColumns(this.bextOutputElem);
    }
*/
}


