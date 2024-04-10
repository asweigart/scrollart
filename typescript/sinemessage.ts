// To get ts types, run: npm i --save-dev @types/readline

namespace SineMessage {
    let width: number = 120
    const DELAY: number = 100;
    const MESSAGE: string = 'Hello, world!';
    const STEP_INCREASE: number = 0.004;

    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nSine Message by Al Sweigart al@inventwithpython.com");
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
        let step: number = 0.0;
        while (true) {
            width = getTerminalWidth();
            let multiplier: number = (width - MESSAGE.length) / 2;
            let padding: string = ' '.repeat(Math.floor((Math.sin(step * (180 / Math.PI)) + 1) * multiplier));
            console.log(padding + MESSAGE);
            step += STEP_INCREASE;
            await sleep(DELAY);
        }
    }

    main();
}