#!/usr/bin/node

const SquareC = require("./5-square");

class Square extends SquareC{
	charPrint(c){
		if (c === undefined){
			c = "X";
		}
		let number = 0;
		while (number < this.height){
			let y = 0;
			while (y < this.width){
				process.stdout.write(c);
				y += 1;
			}
			console.log();
			number += 1;
		}
	}
};

module.exports = Square;
