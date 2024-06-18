#!/usr/bin/node

const firstArg = process.argv[2] ? process.argv[2] : undefined;
const format = ' is ';
const secondArg = process.argv[3] ? process.argv[3] : undefined;
const sentence = firstArg + format + secondArg;

console.log(sentence);
