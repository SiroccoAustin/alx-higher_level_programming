#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0], 10);

function recursive(number){
	if (isNaN(number) || number <= 0){
		return 1;
	}
	return number * recursive(number - 1);
}

console.log(recursive(x));
