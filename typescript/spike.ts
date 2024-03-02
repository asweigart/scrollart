// To get ts types, run: npm i --save-dev @types/readline

namespace Spike {
    let width: number = 120;
    const DELAY: number = 100;

    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nSpike by Al Sweigart al@inventwithpython.com");
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
        while (true) {
            for (let i = 1; i * i < width; i++) {
                width = getTerminalWidth();
                console.log('-'.repeat(i * i));
                await sleep(DELAY);
            }

            for (let i = Math.floor(Math.sqrt(width)) - 1; i > 1; i--) {
                console.log('-'.repeat(i * i));
                await sleep(DELAY);
            }
        }
    }

    main();
}