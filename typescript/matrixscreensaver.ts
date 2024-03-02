// To get ts types, run: npm i --save-dev @types/readline

namespace MatrixScreensaver {
    let width: number = 120
    const DELAY: number = 100;
    const DENSITY: number = 0.02;
    const MIN_STREAM_LENGTH: number = 6;
    const MAX_STREAM_LENGTH: number = 14;
    const STREAM_CHARS: Array<string> = ['0', '1'];

    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nMatrix Screensaver by Al Sweigart al@inventwithpython.com");
        process.exit();
    });

    async function main(): Promise<void> {
        let columns: Array<number> = Array.from({length: width}, () => 0);

        while (true) {
            let line: string = '';
            for (let i = 0; i < width; i++) {
                if (columns[i] === 0) {
                    if (Math.random() < DENSITY) {
                        // Restart the stream in this column:
                        columns[i] = Math.floor(Math.random() * (MAX_STREAM_LENGTH - MIN_STREAM_LENGTH)) + MIN_STREAM_LENGTH;
                    }
                }
                if (columns[i] > 0) {
                    // Add a random stream character for this column:
                    line += STREAM_CHARS[Math.floor(Math.random() * STREAM_CHARS.length)];
                    columns[i] -= 1;
                } else {
                    // Add empty space for this column:
                    line += ' ';
                }
            }
            console.log(line);
            await sleep(DELAY);
        }
    }

    main();
}