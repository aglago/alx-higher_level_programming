#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = [];

  for (let i = 2; i < process.argv.length; i++) {
    numbers.push(+process.argv[i]);
  }

  const firstMax = Math.max(...numbers);

  const firstMaxIndex = numbers.indexOf(firstMax);
  numbers.splice(firstMaxIndex, 1);

  const secondMax = Math.max(...numbers);
  console.log(secondMax);
}
