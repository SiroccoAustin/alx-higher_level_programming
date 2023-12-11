#!/usr/bin/node

const args = process.argv.slice(2);

const x = parseInt(args[0], 10);
let iter = 0;

if (args[0] == undefined || isNaN(args[0])){
	console.log("Missing number of occurrences");
}
else{
	while (iter < x){
		console.log("C is fun");
		iter += 1;
	}
}
