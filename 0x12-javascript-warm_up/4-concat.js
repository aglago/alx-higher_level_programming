#!/usr/bin/node

let arg = '';
const len = process.argv.length;

for (let i = 2; i < len; i++) {
  arg = arg + process.argv[i];

  if (i < len - 1) {
    arg = arg + ' ';
  }
}
console.log(arg);
