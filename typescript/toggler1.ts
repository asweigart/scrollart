// To get ts types, run: npm i --save-dev @types/readline

namespace Toggler1 {
    let width: number = 120

    const DELAY: number = 50;
    const TRUE_CHAR: string = '@';
    const FALSE_CHAR: string = '.';
    const TOGGLER_DENSITY: number = 0.10;

    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nToggler 1 by Al Sweigart al@inventwithpython.com");
        process.exit();
    });

    /*function updateWidth(): void {
        if (process.stdout.isTTY) {
            width = process.stdout.columns - 1; // -1 is because Windows puts a newline when printing to the last column
        }
    }*/

    interface Toggler {
        position: number,
        movement: number
    }

    const MOVEMENTS: number[] = [1, -1];

    async function main(): Promise<void> {
        let columnChars: Array<boolean> = Array.from({length: width}, () => false);
        let togglers: Array<Toggler> = [];

        while (true) {
            if (Math.random() < TOGGLER_DENSITY) {
                // Add a new toggler:
                togglers.push({
                    position: Math.floor(Math.random() * width), 
                    movement: MOVEMENTS[Math.floor(Math.random() * MOVEMENTS.length)]
                });
            }

            // Remove out of bounds togglers:
            togglers = togglers.filter(toggler => toggler.position > 0 && toggler.position < width);

            // Move the togglers and toggle the column chars:
            for (let toggler of togglers) {
                // Toggle the column:
                columnChars[toggler.position] = !columnChars[toggler.position];

                // Move the toggler:
                toggler.position += toggler.movement;
            }

            // Print the columns:
            let line: string = '';
            for (let columnChar of columnChars) {
                if (columnChar) {
                    line += TRUE_CHAR;
                } else {
                    line += FALSE_CHAR;
                }
            }
            console.log(line);
            await sleep(DELAY);
        }
    }

    main();
}