#!/usr/bin/node

exports.esrever = function (list) {
  const revArr = [];

  let index = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    revArr[i] = list[index];
    index++;
  }

  return revArr;
};
