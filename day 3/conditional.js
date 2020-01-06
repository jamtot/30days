'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function checkWeirdness(number){
    var output = "Weird";
    if (!(number%2 || number > 5 && number < 21)){
        output = "Not "+output
    }
    return output
}

function main() {
    const N = parseInt(readLine(), 10);
    console.log(checkWeirdness(N))
}

