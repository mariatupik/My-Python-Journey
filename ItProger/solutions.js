let sum = 0;
for (let i = 1; i < 1000; i++) {
  if (i % 3 == 0 || i % 5 == 0) {
    sum += i;
  }}
console.log("Сума чисел:", sum);

let x = new Array(
  new Array(20, 34, 2), 
  new Array(9, 12, 18), 
  new Array(3, 4, 5)
);
let min = x[0][0];

for (let i = 0; i < x.length; i++) {
    for (let j = 0; j < x[i].length; j++) {
        if (x[i][j] < min) {
            min = x[i][j];
        }}}
console.log("Мінімальний елемент масиву: " + min);