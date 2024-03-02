// To get ts types, run: npm i --save-dev @types/readline

namespace TriGridScaffolding {
    let width: number = 120
    const DELAY: number = 60;
    let CHANGE_AMOUNT: number = 0.04;

    
    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nTri Grid Scaffolding by Al Sweigart al@inventwithpython.com");
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
        let density = 0.0;
        while (true) {
            width = getTerminalWidth();
            let triangleWidth: number = Math.floor((width - 2) / 4);
            let row1: string = '';
            let row2: string = '';

            density += CHANGE_AMOUNT;
            if (density < 0.0 || density >= 1.0) {
                CHANGE_AMOUNT *= -1;
            }
        
            for (let j = 0; j < 2; j++) {
                if (j === 0) {
                    // On j == 0, handle the two rows of begins-with-rightside-up-triangles:
                    //  /\  /\  /\
                    // /__\/__\/__\
                    row1 = '';
                    row2 = '';
                } else if (j == 1) {
                    // On j == 1, handle the two rows of begins-with-upside-down-triangles:
                    // \  /\  /
                    // _\/__\/_
                    row1 = '\\ ';
                    row2 = '_\\';
                }
                
                for (let i = 0; i < triangleWidth; i++) {
                    if (Math.random() < density) {
                        row1 += ' /';
                        row2 += '/';
                    } else {
                        row1 += '  ';
                        row2 += ' ';
                    }

                    if (Math.random() < density) {
                        row2 += '__';
                    } else {
                        row2 += '  ';
                    }

                    if (Math.random() < density) {
                        row1 += '\\ ';
                        row2 += '\\';
                    } else {
                        row1 += '  ';
                        row2 += ' ';
                    }
                }

                console.log(row1);
                await sleep(DELAY);
                console.log(row2);
                await sleep(DELAY);
            }
        }
    }

    main();
}