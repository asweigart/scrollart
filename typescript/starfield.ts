// To get ts types, run: npm i --save-dev @types/readline

namespace Starfield {
    const DELAY: number = 20;
    const STAR_CHAR: string = '*';
    const EMPTY_CHAR: string = ' ';

    let change_amount: number = 0.005;
    let density: number = 0.0;
    let width: number = 120
    let line: string = '';

    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nStarfield by Al Sweigart al@inventwithpython.com");
        process.exit();
    });

    async function main(): Promise<void> {
        while (true) {
            if (process.stdout.isTTY) {
                width = process.stdout.columns - 1; // -1 is because Windows puts a newline when printing to the last column
            }

            if (density < 0 || density > 1) {
                change_amount *= -1;
            }
            density += change_amount;

            line = '';
            for (let i = 0; i < width; i++) {
                if (Math.random() < density) {
                    line += STAR_CHAR;
                } else {
                    line += EMPTY_CHAR;
                }
            }
            console.log(line);
            await sleep(DELAY);
        }
    }

    main();
}