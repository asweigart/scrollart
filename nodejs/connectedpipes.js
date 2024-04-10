
// Constants for settings:
const DELAY = 200;  // Pause after each row in milliseconds.
const WIDTH = 200;

// This setting changes the behavior to create the "long vertical style" if greater than 0.0:
const VERTICAL_STYLE_FACTOR = 1.0;  // Set between 0.0 and 1.0

// Constants for printed characters:
const UP_DOWN_CHAR = String.fromCharCode(9474);  // Character 9474 is '│'
const LEFT_RIGHT_CHAR = String.fromCharCode(9472);  // Character 9472 is '─'
const DOWN_RIGHT_CHAR = String.fromCharCode(9484);  // Character 9484 is '┌'
const DOWN_LEFT_CHAR = String.fromCharCode(9488);  // Character 9488 is '┐'
const UP_RIGHT_CHAR = String.fromCharCode(9492);  // Character 9492 is '└'
const UP_LEFT_CHAR = String.fromCharCode(9496);  // Character 9496 is '┘'
const UP_DOWN_RIGHT_CHAR = String.fromCharCode(9500);  // Character 9500 is '├'
const UP_DOWN_LEFT_CHAR = String.fromCharCode(9508);  // Character 9508 is '┤'
const DOWN_LEFT_RIGHT_CHAR = String.fromCharCode(9516);  // Character 9516 is '┬'
const UP_LEFT_RIGHT_CHAR = String.fromCharCode(9524);  // Character 9524 is '┴'
const CROSS_CHAR = String.fromCharCode(9532);  // Character 9532 is '┼'
const EMPTY = ' ';

// The previous printed row; initialize to up-left-right characters:
let prevRow = Array(WIDTH).fill(UP_LEFT_RIGHT_CHAR);


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Main loop
(async function main() {
    while (true) {

        let row = [];  // Character strings to print in this row.
        for (let i = 0; i < WIDTH; i++) {
            let prevChar = prevRow[i];
            let leftConnect, upConnect, downConnect, rightConnect;

            // Figure out if we need to connect the left side:
            leftConnect = i > 0 && "─┌└├┬┴┼".includes(row[i - 1]);

            // Figure out if we need to connect the up side:
            upConnect = "│┌┐├┤┬┼".includes(prevChar);

            // The downward and right side connection can be either:
            downConnect = Math.random() < 0.5;

            if (i == WIDTH - 1) {
                if (!upConnect && !downConnect && leftConnect && !rightConnect) {
                    // Make this a left-down pipe:
                    downConnect = true;
                } else if (!upConnect && downConnect && !leftConnect && !rightConnect) {
                    // Make this an empty space:
                    downConnect = false;
                } else if (upConnect && !downConnect && !leftConnect && !rightConnect) {
                    // Make this an up-down pipe:
                    downConnect = true;
                }
            } else {
                rightConnect = Math.random() < 0.5;
            }

            // Override rightConnect value if VERTICAL_STYLE_FACTOR is greater than 0.0:
            if (Math.random() < VERTICAL_STYLE_FACTOR) {
                rightConnect = false;
            }

            let char;
            // Get the character to print based on the connections to the four other sides:
            if (upConnect && downConnect && leftConnect && rightConnect) char = CROSS_CHAR;
            else if (upConnect && downConnect && leftConnect) char = UP_DOWN_LEFT_CHAR;
            else if (upConnect && downConnect && rightConnect) char = UP_DOWN_RIGHT_CHAR;
            else if (upConnect && downConnect) char = UP_DOWN_CHAR;
            else if (upConnect && leftConnect && rightConnect) char = UP_LEFT_RIGHT_CHAR;
            else if (upConnect && leftConnect) char = UP_LEFT_CHAR;
            else if (upConnect && rightConnect) char = UP_RIGHT_CHAR;
            else if (upConnect) char = Math.random() < 0.5 ? UP_DOWN_CHAR : UP_RIGHT_CHAR;  // Randomly end or continue the line upwards
            else if (downConnect && leftConnect && rightConnect) char = DOWN_LEFT_RIGHT_CHAR;
            else if (downConnect && leftConnect) char = DOWN_LEFT_CHAR;
            else if (downConnect && rightConnect) char = DOWN_RIGHT_CHAR;
            else if (downConnect) char = DOWN_RIGHT_CHAR;  // Force the line to go down and to the right
            else if (leftConnect && rightConnect) char = LEFT_RIGHT_CHAR;
            else if (leftConnect) char = Math.random() < 0.5 ? LEFT_RIGHT_CHAR : DOWN_LEFT_CHAR;  // Randomly end or bend the line leftwards
            else if (rightConnect) char = DOWN_RIGHT_CHAR;  // Force the line to go down and to the right
            else char = EMPTY;

            row.push(char);
        }

        console.log(row.join(''));
        prevRow = row;
        await sleep(DELAY);
    }
})();

