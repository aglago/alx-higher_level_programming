#!/usr/bin/node

const firstNum = +process.argv[2];

if (isNaN(firstNum)) {
  console.log('Not a number');
} else {
  console.log('My number:', firstNum);
}
