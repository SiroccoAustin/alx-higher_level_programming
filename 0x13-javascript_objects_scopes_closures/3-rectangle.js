#!/usr/bin/node

class Rectangle{
	constructor (w, h){
		if ((w > 0) && (h > 0)){
			this.width = w;
			this.height = h;
		}
	}
	print(){
		let number = 0;
		while (number < this.height){
			let y = 0;
			while (y < this.width){
				process.stdout.write("X");
				y += 1;
			}
			console.log();
			number += 1;
		}
	}
};

module.exports = Rectangle;
