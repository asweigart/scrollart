// Cube Wall scroll art, by Al Sweigart al@inventwithpython.com
// To get ts types, run: npm i --save-dev @types/readline

namespace CubeWall {
    const DELAY: number = 100;
    const DENSITY: number = 0.35;

    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nCube Wall by Al Sweigart al@inventwithpython.com");
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
            let width: number = getTerminalWidth();
            let segmentWidth: number = Math.floor(width / 18);

            let row1: string = '';
            let row2: string = '';
            let row3: string = '';
            let row4: string = '';
            let row5: string = '';
            let row6: string = '';

            let top1Shading: string = '';
            let top1ShadingBottom: string = '';
            let top2Shading: string = '';
            let top2ShadingBottom: string = '';
            let bottom1Shading: string = '';
            let bottom1ShadingBottom: string = '';
            let bottom2Shading: string = '';
            let bottom2ShadingBottom: string = '';
            let side1Shading: string = '';
            

            for (let i = 0; i < segmentWidth; i++) {
                if (Math.random() < DENSITY) {
                    top1Shading = '/////';
                    top1ShadingBottom = '_/_/_';
                } else {
                    top1Shading = '     ';
                    top1ShadingBottom = '_____';
                }

                if (Math.random() < DENSITY) {
                    top2Shading = '/////';
                    top2ShadingBottom = '_/_/_';
                } else {
                    top2Shading = '     ';
                    top2ShadingBottom = '_____';
                }

                if (Math.random() < DENSITY) {
                    bottom1Shading = '\\\\\\\\\\';
                    bottom1ShadingBottom = '_\\_\\_';
                } else {
                    bottom1Shading = '     ';
                    bottom1ShadingBottom = '_____';
                }

                if (Math.random() < DENSITY) {
                    bottom2Shading = '\\\\\\\\\\';
                    bottom2ShadingBottom = '_\\_\\_';
                } else {
                    bottom2Shading = '     ';
                    bottom2ShadingBottom = '_____';
                }

                if (Math.random() < DENSITY) {
                    if (Math.random() < 0.5) {
                        side1Shading = '\\\\';
                    } else {
                        side1Shading = '//';
                    }
                } else {
                    side1Shading = '  ';
                }

                row1 += `  /${top1Shading}/\\${bottom2Shading}\\  `;
                row2 += ` /${top1Shading}/${side1Shading}\\${bottom2Shading}\\ `;
                row3 += `/${top1ShadingBottom}/${side1Shading.repeat(2)}\\${bottom2ShadingBottom}\\`;
                row4 += `\\${bottom1Shading}\\${side1Shading.repeat(2)}/${top2Shading}/`;
                row5 += ` \\${bottom1Shading}\\${side1Shading}/${top2Shading}/ `;
                row6 += `  \\${bottom1ShadingBottom}\\/${top2ShadingBottom}/  `;
            }

            console.log(row1); await sleep(DELAY);
            console.log(row2); await sleep(DELAY);
            console.log(row3); await sleep(DELAY);
            console.log(row4); await sleep(DELAY);
            console.log(row5); await sleep(DELAY);
            console.log(row6); await sleep(DELAY);
        }
    }

    main();
}

/*

  ///////\\\\\\\    ///////\\\\\\\    ///////\\\\\\\    /     /\     \    /     /\     \    ///////\\\\\\\    ///////\     \    /     /\\\\\\\  
 ///////  \\\\\\\  ///////  \\\\\\\  ///////  \\\\\\\  /     /  \     \  /     /  \     \  ///////\\\\\\\\\  /////////\     \  /     /\\\\\\\\\ 
/_/_/_/    \_\_\_\/_/_/_/    \_\_\_\/_/_/_/    \_\_\_\/_____/    \_____\/_____/    \_____\/_/_/_/\\\\\_\_\_\/_/_/_/////\_____\/_____/\\\\\_\_\_\
\     \    ///////\     \    ///////\     \    /     /\\\\\\\    ///////\     \    /     /\     \\\\\///////\     \///////////\     \\\\\/     /
 \     \  ///////  \     \  ///////  \     \  /     /  \\\\\\\  ///////  \     \  /     /  \     \\\///////  \     \/////////  \     \\\/     / 
  \_____\/_/_/_/    \_____\/_/_/_/    \____
*/