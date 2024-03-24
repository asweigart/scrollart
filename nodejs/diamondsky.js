// Code adapted from my diamonds.py program here: https://inventwithpython.com/bigbookpython/project16.html

const DELAY = 100;  // Pause after each row in milliseconds.
const WIDTH = 200;  // Number of columns in output.
const MIN_DIAMOND_SIZE = 1;
const MAX_DIAMOND_SIZE = 8;

const CHANCE_FOR_FILLED_DIAMOND = 0.3;  // Set between 0.0 and 1.0

const NUM_DIAMONDS_PER_ROW = 2;

const EMPTY = '                ...,';

function getOutlineDiamond(size) {
    if (size <= 0) throw new Error('Size must be greater than 0');
    let rows = [];
    // Make the top half of the diamond:
    for (let i = 0; i < size; i++) {
        rows.push(new Array(size - i - 1).fill(null).concat('/').concat(new Array(i * 2).fill(' ')).concat('\\'));
    }
    // Make the bottom half of the diamond:
    for (let i = 0; i < size; i++) {
        rows.push(new Array(i).fill(null).concat('\\').concat(new Array((size - i - 1) * 2).fill(' ')).concat('/'));
    }
    return rows;
}

function getFilledDiamond(size) {
    if (size <= 0) throw new Error('Size must be greater than 0');
    let rows = [];
    // Make the top half of the diamond:
    for (let i = 0; i < size; i++) {
        rows.push(new Array(size - i - 1).fill(null).concat(new Array(i + 1).fill('/')).concat(new Array(i + 1).fill('\\')));
    }
    // Make the bottom half of the diamond:
    for (let i = 0; i < size; i++) {
        rows.push(new Array(i).fill(null).concat(new Array(size - i).fill('\\')).concat(new Array(size - i).fill('/')));
    }
    return rows;
}

(async function displayDiamonds() {
    let nextRows = [];
    while (true) {
        for (let j = 0; j < NUM_DIAMONDS_PER_ROW; j++) {
            let size = Math.floor(Math.random() * (MAX_DIAMOND_SIZE - MIN_DIAMOND_SIZE + 1)) + MIN_DIAMOND_SIZE;

            let diamond;
            if (Math.random() < CHANCE_FOR_FILLED_DIAMOND) {
                diamond = getFilledDiamond(size);
            } else {
                diamond = getOutlineDiamond(size);
            }

            let xStart = Math.floor(Math.random() * (WIDTH - 1 - (size * 2)));

            // Make sure there are enough rows in `nextRows`:
            while (nextRows.length < size * 2) {
                nextRows.push(new Array(WIDTH).fill(null).map(() => EMPTY[Math.floor(Math.random() * EMPTY.length)]));
            }

            // Add the diamond to `nextRows`
            for (let y = 0; y < diamond.length; y++) {
                for (let x = 0; x < diamond[y].length; x++) {
                    if (diamond[y][x] === null) continue;  // Skip null values, equivalent to Python's None
                    nextRows[y][x + xStart] = diamond[y][x];
                }
            }
        }

        // Print the row and then remove it:
        console.log(nextRows[0].join(''));
        nextRows.shift();

        // Pause for a bit before printing the next row:
        await new Promise(resolve => setTimeout(resolve, DELAY));
    }
})();
