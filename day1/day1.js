// import fs from 'node:fs';
const fs = require('node:fs');

console.log("Hello World")
const file = './sampleData.txt'

const openFile = (file) => {
    fs.readFile(file, 'utf8', (data, err) => {
        if (err) {
            console.error(err)
            return;
        } else {
            return data
        }
    })
}

var input = fs.readFile(file, (data, err) => {
    if (err) {
        console.error(err)
        return;
    }
})

console.log("Input: ", input)
// console.log(inputAsStr.split("   "))
