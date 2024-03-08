// Math Func scroll art, by Al Sweigart al@inventwithpython.com
// To get ts types, run: npm i --save-dev @types/readline

namespace MathFunc {
    const DELAY: number = 100;
    //const FUNC = (x: number, y: number): boolean => ((x ^ y) % 5) !== 0;
    //const FUNC = (x: number, y: number): boolean => ((x & y) & (x ^ y) % 19) !== 0;
    //const FUNC = (x: number, y: number): boolean => ((x * 64) % y) !== 0;
    const FUNC = (x: number, y: number): boolean => ((x | y) % 7) !== 0;

    const TOP_BLOCK: string = String.fromCodePoint(9600);
    const BOTTOM_BLOCK: string = String.fromCodePoint(9604);
    const FULL_BLOCK: string = String.fromCodePoint(9608);
    const EMPTY_BLOCK: string = ' ';

    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nMath Func by Al Sweigart al@inventwithpython.com");
        process.exit();
    });

    function getTerminalWidth(): number {
        if (process.stdout.isTTY) {
            return process.stdout.columns - 1; // -1 is because Windows puts a newline when printing to the last column
        } else {
            return 80;
        }
    }

    async function main(): Promise<void> {
        let y: number = 0;
        while (true) {
            let width = getTerminalWidth() - 1;
            let line: string = '';
            for (let x = 0; x < width; x++) {
                let topBit: boolean = FUNC(x, y);
                let bottomBit: boolean = FUNC(x, y + 1);

                // Flipping the bits because I think they often look better this way:
                topBit = !topBit;
                bottomBit = !bottomBit;

                if (topBit && bottomBit) {
                    line += FULL_BLOCK;
                } else if (topBit && !bottomBit) {
                    line += TOP_BLOCK;
                } else if (!topBit && bottomBit) {
                    line += BOTTOM_BLOCK;
                } else {
                    line += ' ';
                }
            }
            console.log(line);
            y += 2;
            await sleep(DELAY);
        }
    }

    main();
}