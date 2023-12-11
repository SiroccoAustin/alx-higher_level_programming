#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0], 10);

let iter = 0;

if (x === undefined || isNaN(x)){
	console.log("Missing size");
}
else{
	while (iter < x){
		let y = 0;
		while (y < x){
			process.stdout.write("X");
			y += 1;
		}
		console.log();
		iter += 1;
	}
}
