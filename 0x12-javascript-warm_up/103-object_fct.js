#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: incr
};
console.log(myObject);

function incr () {
  myObject.value++;
}

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
