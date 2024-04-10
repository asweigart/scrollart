// To get ts types, run: npm i --save-dev @types/readline

namespace StripedTriangles {
    let width: number = 120

    const DELAY: number = 60;
    let CHANGE_AMOUNT: number = 0.06;
    
    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nStriped Triangles by Al Sweigart al@inventwithpython.com");
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
        let density: number = 0.0;

        while (true) {
            width = getTerminalWidth();

            // The width of a pair of triangles is 8 characters:
            //   /\ \ \
            //  / /\ \
            // / / /\
            // 12345678
            let numTrianglePairs: number = Math.floor((width - 2) / 6);

            density += CHANGE_AMOUNT;
            if (density < 0 || density >= 1.0) {
                CHANGE_AMOUNT *= -1;
            }

            // Draw a row that starts with an upright triangle on the left side.
            let row1: string = '  ';
            let row2: string = ' ';
            let row3: string = '';
            for (let i = 0; i < numTrianglePairs; i++) {
                if (Math.random() < density) {
                    if (Math.random() < 0.5) {
                        row1 += '\\';
                        row2 += '\\ \\';
                        row3 += '\\ \\ \\';
                    } else {
                        row1 += '/';
                        row2 += '/ /';
                        row3 += '/ / /';
                    }
                } else {
                    row1 += ' ';
                    row2 += '   ';
                    row3 += '     ';
                }

                if (Math.random() < density) {
                    if (Math.random() < 0.5) {
                        row1 += '\\ \\ \\';
                        row2 += '\\ \\';
                        row3 += '\\';
                    } else {
                        row1 += '/ / /';
                        row2 += '/ /';
                        row3 += '/';
                    }
                } else {
                    row1 += '     ';
                    row2 += '   ';
                    row3 += ' ';
                }
            }
            console.log(row1);
            await sleep(DELAY);
            console.log(row2);
            await sleep(DELAY);
            console.log(row3);
            await sleep(DELAY);
            
            // Draw a row that starts with an upside down triangle on the left side.
            row1 = '';
            row2 = ' ';
            row3 = '  ';
            for (let i = 0; i < numTrianglePairs; i++) {
                if (Math.random() < density) {
                    if (Math.random() < 0.5) {
                        row1 += '\\ \\ \\';
                        row2 += '\\ \\';
                        row3 += '\\';
                    } else {
                        row1 += '/ / /';
                        row2 += '/ /';
                        row3 += '/';
                    }
                } else {
                    row1 += '     ';
                    row2 += '   ';
                    row3 += ' ';
                }

                if (Math.random() < density) {
                    if (Math.random() < 0.5) {
                        row1 += '\\';
                        row2 += '\\ \\';
                        row3 += '\\ \\ \\';
                    } else {
                        row1 += '/';
                        row2 += '/ /';
                        row3 += '/ / /';
                    }
                } else {
                    row1 += ' ';
                    row2 += '   ';
                    row3 += '     ';
                }
            }
            console.log(row1);
            await sleep(DELAY);
            console.log(row2);
            await sleep(DELAY); 
            console.log(row3);
            await sleep(DELAY);
        }
    }

    main();
}