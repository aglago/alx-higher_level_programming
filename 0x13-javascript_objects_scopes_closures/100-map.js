#!/usr/bin/node

const list = require('./100-data').list;

const mapped = list.map((el, index) => {
  return el * index;
});

console.log(list);
console.log(mapped);
