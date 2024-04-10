// To get ts types, run: npm i --save-dev @types/readline

namespace Zigzag {
    let width: number = 120

    const DELAY: number = 20;
    const ZIG_NUM_CHARS: number = 8;
    const ZIG_CHAR: string = '*';

    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nZigzag by Al Sweigart al@inventwithpython.com");
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
        let indentSize: number = 0;

        while (true) {
            for (let i = 0; i < width - ZIG_NUM_CHARS; i++) {
                width = getTerminalWidth();
                console.log(' '.repeat(indentSize), ZIG_CHAR.repeat(ZIG_NUM_CHARS));
                indentSize += 1;
                await sleep(DELAY);
            }

            for (let i = 0; i < width - ZIG_NUM_CHARS; i++) {
                width = getTerminalWidth();
                console.log(' '.repeat(indentSize), ZIG_CHAR.repeat(ZIG_NUM_CHARS));
                indentSize -= 1;
                await sleep(DELAY);
            }
        }
    }

    main();
}