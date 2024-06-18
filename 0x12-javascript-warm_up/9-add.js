#!/usr/bin/node

const firstNum = +process.argv[2];
const secondNum = +process.argv[3];

function add(a, b) {
  console.log(a + b);
}

add (firstNum, secondNum);
