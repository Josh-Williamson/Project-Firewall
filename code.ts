var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
const SW = canvas.width; 
const SH = canvas.height;
const TILE_W = 25; //tile pixel width
var bgcolor = "grey";

//soldier or enemy class
class Soldier{

	//soldier attributes
	constructor(pos,color,r,health,attack){
		this.pos = pos;
		this.color = color;
		this.r = r;
		this.health = health;
		this.attack = attack;
		
		//targets refrence points on the map
		this.targets = [];
		this.targets[0] = new Vector(startPos.x + pathData[0].x, startPos.y + pathData[0].y);
			
		//for multiple points
		for (let i = 1; i < pathData.length; i++){
			let prevTarget = this.targets[i-1];
			let path = pathData[i];
			
			let newTarget = new Vector(prevTarget.x + path.x, prevTarget.y + path.y);
			this.targets[i] = newTarget;		
		}	
		
		//traveling attributes
		this.currentTarget = this.targets[0];
		this.dir = new Vector(0,0);
		this.speed = 2.5;
		this.minTargetDist = 2;
	}
	
	//updates new current target as they reach targets
	update (){
		if(this.currentTarget == null) return;
	
		let dir = new Vector(this.currentTarget.x - this.pos.x, this.currentTarget.y - this.pos.y);
		let distance = (dir.x ** 2 + dir.y ** 2) ** (1/2);
		
		if(distance == 0) return;
		
		dir.x /= distance;
		dir.y /= distance;
		
		this.pos.x += dir.x * this.speed;
		this.pos.y += dir.y * this.speed;
		
		let xDist = Math.abs (this.pos.x - this.currentTarget.x);
		let yDist = Math.abs (this.pos.y - this.currentTarget.y);
		
		if (xDist <= this.minTargetDist && yDist <= this.minTargetDist){
		this.targets.splice(0,1);
		
			if(this.targets.length == 0) {
				this.currentTarget = null;
			}
			else{
				this.currentTarget = this.targets[0];
			}
		}
		
	}
	
	//renders enemy soldier circle
	render(){
		context.fillStyle = this.color;
		context.beginPath();
		context.arc(this.pos.x,this.pos.y,this.r,0,Math.PI** 2);
		context.fill();
	}
	
}



//vetor used to store x,y coord
class Vector{
	constructor(x,y){
	this.x = x;
	this.y = y;
	}
}

//starting path position
var startPos = new Vector(100,0);

//path coords (by pixel)
var pathData = [
	new Vector(0,200),
	new Vector(400,0),
	new Vector(0,-150),
	new Vector(150,0),
	new Vector(0, 250),
	new Vector(-600,0),
	new Vector(0,200),
	new Vector(700,0)
];

// soldier array
var soldiers = [];
const NUM_SOLDIERS = 10;

//soldier starting point
var soldierStart = new Vector(100,0);

//soldier loop
for (let i = 0; i < NUM_SOLDIERS; i++){
	let newSoldier = new Soldier(new Vector(soldierStart.x, soldierStart.y),"black",20,100,10);
	soldiers[soldiers.length] = newSoldier;
	soldierStart.y-=50;
}

//updates soldiers
function update () {
	soldiers.forEach(function(s){
		s.update()
	});
}

//renders path
function renderPath(){
	//gives path a starting point
	let drawPos = new Vector(startPos.x, startPos.y);
	
	//fills path color
	context.fillStyle = "white";
	
	//draws in each tile
	pathData.forEach(function(path){
		//up-down
		if (path.x == 0){
			let x = drawPos.x - TILE_W;
			let y = drawPos.y - TILE_W;
			let w = TILE_W * 2;
			let h = path.y + TILE_W * 2;
		
			context.fillRect(x,y,w,h);
		}
		//left right
		else{
			let x = drawPos.x - TILE_W;
			let y = drawPos.y - TILE_W;
			let w = path.x + TILE_W * 2;
			let h = TILE_W * 2;
			
			context.fillRect(x,y,w,h);
		}
		
		//updates start position when pathData updates
		drawPos.x += path.x;
		drawPos.y += path.y;
	});
}

//renders grid 
function renderGrid() {
	//line color
	context.fillStyle = "white";
	
	//draws up-down
	let x = 0;
	for (let i = 0; i < SW / TILE_W; i++){
		context.beginPath();
		context.moveTo(x,0);
		context.lineTo(x,SH);
		context.stroke();
	
		x += TILE_W;
	}
	
	//draws lines left-right
		let y = 0;
	for (let i = 0; i < SW / TILE_W; i++){
		context.beginPath();
		context.moveTo(0,y);
		context.lineTo(SW,y);
		context.stroke();
	
		y += TILE_W;
	}
}

//renders game window on browser
function render () {
	context.fillStyle = bgcolor;
	context.fillRect(0,0,SW,SH);
	
	renderPath();
	renderGrid();
	
	//renders enemy soldiers
	soldiers.forEach(function(s){
		s.render()
	});
}

function play () {
	update();
	render();

}
// 1000 pixels 60 fps
setInterval(play,1000/60);