// To get ts types, run: npm i --save-dev @types/readline

const DELAY: number = 20;

let change_amount: number = 0.005;
let density: number = 0.0;
let width: number = 80
let line: string = '';

async function sleep(milliseconds: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, milliseconds));
}

async function main() {
    while (true) {
        if (process.stdout.isTTY) {
            width = process.stdout.columns - 1; // -1 is for Windows
        }

        if (density < 0 || density > 1) {
            change_amount *= -1;
        }
        density += change_amount;

        line = '';
        for (let i = 0; i < width; i++) {
            if (Math.random() < density) {
                line += '*';
            } else {
                line += ' ';
            }
        }
        console.log(line);
        await sleep(DELAY);
    }
}

main();