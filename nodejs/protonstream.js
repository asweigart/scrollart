
// Constants for settings:
const DELAY = 10;  // Pause after each row in milliseconds.
const WIDTH = 200;  // Number of columns in output.
const NUM_STREAMS = 5;  // Number of streams on the screen.
const MAX_DISTANCE = NUM_STREAMS * 4;  // How many spaces streams must be within each other.
const MOVE_CHANCE = 0.75;  // How often a stream tries to move left or right, rather than continue straight.

const EMPTY_CHAR = ' ';
const STREAM_CHARS = 'oO@';

let streams = Array(NUM_STREAMS).fill(Math.floor(WIDTH / 2));


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async function main() {
    while (true) {
        let columns = Array(WIDTH).fill(EMPTY_CHAR);

        streams.forEach((stream, i) => {
            if (Math.random() < MOVE_CHANCE) {
                // Move stream:
                if (Math.random() < 0.5) { // Adjusting for bias
                    if (stream > 0 && streams.every(other => Math.abs((stream - 1) - other) <= MAX_DISTANCE)) {
                        // Move stream left:
                        streams[i] -= 1;
                    }
                } else {
                    if (stream < WIDTH - 1 && streams.every(other => Math.abs((stream + 1) - other) <= MAX_DISTANCE)) {
                        // Move stream right:
                        streams[i] += 1;
                    }
                }
            }

            columns[stream] = STREAM_CHARS[i % STREAM_CHARS.length];
        });

        /*
        // Eh, sparks just don't make it look that good.
        // Add sparks:
        if (Math.random() < SPARK_CHANCE) {
            // Find range where sparks can appear:
            const leftmostSparkColumn = Math.max(0, Math.min(...streams) - SPARK_RANGE);
            const rightmostSparkColumn = Math.min(WIDTH - 1, Math.max(...streams) + SPARK_RANGE);

            // Add sparks:
            Array.from({length: randomNumSparks()}, () => Math.floor(Math.random() * (rightmostSparkColumn - leftmostSparkColumn + 1) + leftmostSparkColumn))
                 .forEach(x => {
                     if (!STREAM_CHARS.includes(columns[x])) {  // Don't overlap a stream with a spark
                         columns[x] = SPARK_CHARS[Math.floor(Math.random() * SPARK_CHARS.length)];
                     }
                 });
        }
        */

        console.log(columns.join(''));
        await sleep(DELAY);
    }
})();
