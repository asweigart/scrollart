// To get ts types, run: npm i --save-dev @types/readline

namespace DiagonalMaze {
    let width: number = 120;
    const DELAY: number = 150;

    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nDiagonal Maze by Al Sweigart al@inventwithpython.com");
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
            let line: string = '';
            for (let i: number = 0; i < width; i++) {
                if (Math.random() < 0.5) {
                    line += String.fromCharCode(9585);
                } else {
                    line += String.fromCharCode(9586);
                }
            }
            console.log(line);
            await sleep(DELAY);
        }
    }

    main();
}