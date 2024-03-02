// To get ts types, run: npm i --save-dev @types/readline

namespace Ducklings {
    let width: number = 120

    const DELAY: number = 60;
    const DENSITY: number = 0.10;

    const DUCKLING_WIDTH: number = 5;

    type Direction = 'LEFT' | 'RIGHT';
    type Eyes = 'BEADY' | 'WIDE' | 'HAPPY' | 'ALOOF';
    type Body = 'CHUBBY' | 'VERY_CHUBBY';
    type Bill = 'OPEN' | 'CLOSED';
    type Wing = 'OUT' | 'DOWN' | 'UP';
    type NextBodyPart = 'HEAD' | 'BODY' | 'FEET' | 'DONE';

    class Duckling {
        direction: Direction;
        eyes: Eyes;
        bill: Bill;
        body: Body;
        wing: Wing;       
        nextBodypart: NextBodyPart; 

        constructor() {
            this.direction = (['LEFT', 'RIGHT'] as const)[Math.floor(Math.random() * 2)];
            this.bill = (['CLOSED', 'OPEN'] as const)[Math.floor(Math.random() * 2)];
            this.body = (['CHUBBY', 'VERY_CHUBBY'] as const)[Math.floor(Math.random() * 2)];
            this.wing = (['DOWN', 'OUT', 'UP'] as const)[Math.floor(Math.random() * 3)];

            if (this.body == 'CHUBBY') {
                // Chubby ducklings can only have beady eyes.
                this.eyes = 'BEADY';
            } else {
                this.eyes = (['ALOOF', 'HAPPY', 'WIDE'] as const)[Math.floor(Math.random() * 3)];
            }

            this.nextBodypart = 'HEAD';
        };

        getHeadStr(): string {
            let headStr: string = '';
            if (this.direction === 'LEFT') {
                // Get the bill:
                if (this.bill === 'OPEN') {
                    headStr += '>';
                } else if (this.bill === 'CLOSED') {
                    headStr += '=';
                }

                // Get the eyes:
                if (this.eyes === 'BEADY' && this.body === 'CHUBBY') {
                    headStr += '"';
                } else if (this.eyes === 'BEADY' && this.body === 'VERY_CHUBBY') {
                    headStr += '" ';
                } else if (this.eyes === 'WIDE') {
                    headStr += "''";
                } else if (this.eyes === 'HAPPY') {
                    headStr += '^^';
                } else if (this.eyes == 'ALOOF') {
                    headStr += '``';
                }

                headStr += ') '; //  Back of the left-facing head.
            } else if (this.direction === 'RIGHT') {
                headStr += ' (';  // Back of the right-facing head.

                // Get the eyes:
                if (this.eyes === 'BEADY' && this.body === 'CHUBBY') {
                    headStr += '"';
                } else if (this.eyes === 'BEADY' && this.body === 'VERY_CHUBBY') {
                    headStr += ' "';
                } else if (this.eyes === 'WIDE') {
                    headStr += "''";
                } else if (this.eyes === 'HAPPY') {
                    headStr += '^^';
                } else if (this.eyes == 'ALOOF') {
                    headStr += '``';
                }

                // Get the bill:
                if (this.bill === 'OPEN') {
                    headStr += '<';
                } else if (this.bill === 'CLOSED') {
                    headStr += '=';
                }
            }

            if (this.body === 'CHUBBY') {
                // Get an extra space so chubby ducklings are the same width as very chubby ducklings.
                headStr += ' ';
            }

            return headStr;
        }

        getBodyStr(): string {
            let bodyStr: string = '(';
            if (this.direction === 'LEFT') {
                // Get the interior body space:
                if (this.body === 'CHUBBY') {
                    bodyStr += ' ';
                } else if (this.body === 'VERY_CHUBBY') {
                    bodyStr += '  ';
                }

                // Get the wing:
                if (this.wing === 'OUT') {
                    bodyStr += '>';
                } else if (this.wing === 'UP') {
                    bodyStr += '^';
                } else if (this.wing === 'DOWN') {
                    bodyStr += 'v';
                }
            } else if (this.direction === 'RIGHT') {
                // Get the wing:
                if (this.wing === 'OUT') {
                    bodyStr += '<';
                } else if (this.wing === 'UP') {
                    bodyStr += '^';
                } else if (this.wing === 'DOWN') {
                    bodyStr += 'v';
                }
                
                // Get the interior body space:
                if (this.body === 'CHUBBY') {
                    bodyStr += ' ';
                } else if (this.body === 'VERY_CHUBBY') {
                    bodyStr += '  ';
                }
            }

            bodyStr += ')';

            if (this.body === 'CHUBBY') {
                // Get an extra space so chubby ducklings are the same width as very chubby ducklings.
                bodyStr += ' ';
            }

            return bodyStr;
        }

        getFeetStr(): string {
            if (this.body === 'CHUBBY') {
                return ' ^^  ';
            } else if (this.body === 'VERY_CHUBBY') {
                return ' ^ ^ ';
            } else {
                return '';
            }
        }

        getNextBodyPart() {
            if (this.nextBodypart === 'HEAD') {
                this.nextBodypart = 'BODY';
                return this.getHeadStr();
            } else if (this.nextBodypart === 'BODY') {
                this.nextBodypart = 'FEET';
                return this.getBodyStr();
            } else if (this.nextBodypart === 'FEET') {
                this.nextBodypart = 'DONE';
                return this.getFeetStr();
            }
        }
    }
    
    async function sleep(milliseconds: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, milliseconds));
    }

    process.on('SIGINT', function() {
        console.log("\nDucklings by Al Sweigart al@inventwithpython.com");
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
        let width = getTerminalWidth();
        let ducklingLanes: Array<Duckling | null> = Array.from({length: (Math.floor(width / DUCKLING_WIDTH))}, () => null);

        while (true) {
            let line: string = '';
            for (let laneNum: number = 0; laneNum < ducklingLanes.length; laneNum++) {
                let ducklingObj: Duckling | null = ducklingLanes[laneNum];
                if (ducklingLanes[laneNum] === null && Math.random() < DENSITY) {
                    // Place a new duckling in this lane:
                    ducklingObj = new Duckling();
                    ducklingLanes[laneNum] = ducklingObj;
                }

                if (ducklingObj !== null) {
                    line += ducklingObj.getNextBodyPart();
                    // Delete the duckling if we've finished drawing it:
                    if (ducklingObj.nextBodypart == 'DONE') {
                        ducklingLanes[laneNum] = null;
                    }
                } else {
                    // Draw five spaces since there is no duckling in this lane:
                    line += ' '.repeat(DUCKLING_WIDTH);
                }
            }
            console.log(line);
            await sleep(DELAY);
        }
    }

    main();
}