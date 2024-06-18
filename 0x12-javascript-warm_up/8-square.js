#!/usr/bin/node

const len = +process.argv[2];

if (isNaN(len)) {
  console.log('Missing size');
} else {
  let square = '';

  for (let i = 0; i < len; i++) {
    for (let k = 0; k < len; k++) {
      square = square + 'X';
    }

    if (i < len - 1) {
      square = square + '\n';
    }
  }

  console.log(square);
}
