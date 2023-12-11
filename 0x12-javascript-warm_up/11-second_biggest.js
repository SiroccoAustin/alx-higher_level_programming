#!/usr/bin/node

const args = process.argv.slice(2);

const myArray = [];

let iter = 0;

while (iter < args.length){
	const parseValue = parseInt(args[iter], 10);
	if (!isNaN(parseValue)){

		myArray.push(parseValue);
	}
	iter += 1;
}
const sortedArray = myArray.sort((a, b) => b - a);

if (myArray.length <= 1){
	console.log(0);
}
else{
	const secondLargest = sortedArray[1];
	console.log(secondLargest);
}
