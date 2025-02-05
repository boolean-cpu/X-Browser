
const GAME_SATATE={
	PAUSED:0,
	RUNNING:1,
	MENU:3,
	GAME_OVER:4,
	NEW_LEVEL:5
	
	
}

const level1=[
	[0,1,1,0,0,0,0,1,1,0],
	[1,1,1,1,1,1,1,1,1,1]
	
	];
	const level2=[
	[0,1,1,0,0,0,0,1,1,0],
	[1,1,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1,1]
			
	];
	
	const level3=[
	[1,1,1,0,0,0,0,1,1,1],
	[0,1,1,1,1,1,1,1,1,0],
	[1,1,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1,1]		
	];

	const level4=[
	[1,1,1,1,1,1,1,1,1,1],
	[0,1,1,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1,1,0],
	[1,1,1,1,1,1,1,1,1,1]		
	];

	const level5=[
	[0,1,1,1,1,1,1,1,1,0],
	[1,1,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1,1]		
	];
	
class Paddle{
	constructor(game){
		this.gamewidth=game.gamewidth;
		this.width=150;
		this.height=20;
		this.maxspeed=7;
		this.speed=0;
		this.position={
			x:game.gamewidth/2-this.width/2,
			y:game.gameheight-this.height-10
	}}
		draw(ctx){
			
			ctx.fillRect(this.position.x,this.position.y,this.width,this.height)
			ctx.fillStyle="blue";
	}
	moveRight(){
		
		this.speed= this.maxspeed;
	}
	moveLeft(){
		this.speed= -this.maxspeed;
	}
	stop(){
		this.speed=0;
	}
	update(deltatime){
		
		this.position.x=this.position.x+this.speed;
		if(this.position.x<0){ this.position.x=0;}
		if(this.position.x+this.width>this.gamewidth){ this.position.x=this.gamewidth-this.width};
	}
	
	}

class Handler{
	constructor(paddle,game){
    document.addEventListener("keydown",event=>{
		
   switch(event.keyCode){
case 37:
paddle.moveLeft();
break;
case 39:

paddle.moveRight();
break;
case 27:
game.tooglePause();
break;
case 32:
game.start();
break;

	}
	
	
	
	
	});
   
  document.addEventListener("keyup",event=>{
		
   switch(event.keyCode){
case 37:
 if(paddle.speed<0){
 paddle.stop();}
break;
case 39:
if(paddle.speed>0){
paddle.stop();}
break;



	} ;
  
})
}
} 
class Ball{

constructor(game){
	this.game=game;
this.img=document.getElementById("img_ball");

this.gameheight=game.gameheight;
this.gamewidth=game.gamewidth;
this.size=20;	
this.lives=3;
this.reset();	
}
reset(){
	this.position={
	x:10,
y:400}
this.speed={
	x:5,
	y:-5
}
}

draw(ctx){
ctx.drawImage(this.img,this.position.x,this.position.y,this.size,this.size)

}
update(deltatime){
	if(this.lives==0){
		game.gamestate=GAME_SATATE.GAME_OVER;
	}
this.position.x=this.position.x+this.speed.x;
this.position.y=this.position.y+this.speed.y;
if(this.position.x<0 || this.position.x+this.size>this.gamewidth){
this.speed.x=-this.speed.x;
}
if(this.position.y<0){
this.speed.y=-this.speed.y;
}
if( this.position.y+this.size>this.gameheight){
	this.lives--;
	this.reset();
	
}
if(detection(this,this.game.paddle)){
	this.speed.y=-this.speed.y;
	this.position.y=this.game.paddle.position.y-this.size;
	
} 
}



}


class Brick{

constructor(game,position){
	this.game=game;
this.img=document.getElementById("img_brick");
this.position=position;

this.width=80;
this.height=24;	
this.markdeletion=false;
	
}

update(){
	if(detection(this.game.ball,this)){
		this.game.ball.speed.y=-this.game.ball.speed.y;
		this.markdeletion= true;
	}
	
}

draw(ctx){
ctx.drawImage(this.img,this.position.x,this.position.y,this.width,this.height)

}


	}










class Game{
	constructor(gamewidth,gameheight){
		this.gameheight=gameheight;
		this.gamewidth=gamewidth;
		this.paddle = new Paddle(this);
this.ball= new Ball(this);	
new Handler(this.paddle,this);
this.gamestate=GAME_SATATE.MENU;
this.bricks=[];
this.gameObjects=[];
this.counter=0;
this.levels=[level1,level2,level3,level4,level5];
	
		
	}
start(){
	if(this.gamestate!=GAME_SATATE.MENU && this.gamestate!=GAME_SATATE.NEW_LEVEL){return}
this.gamestate=GAME_SATATE.RUNNING;	

this.bricks=levelsOb(this,this.levels[this.counter]);
this.gameObjects=[this.paddle,this.ball]
this.ball.reset();


}

update(deltatime){
	if(this.gamestate===GAME_SATATE.PAUSED || this.gamestate===GAME_SATATE.MENU || 
	this.gamestate===GAME_SATATE.GAME_OVER){return}
	[...this.gameObjects,...this.bricks].forEach((object)=>{object.update(deltatime)});
this.bricks=this.bricks.filter(brick=> !brick.markdeletion );

if(this.bricks.length===0){
	this.counter++;
	this.gamestate=GAME_SATATE.NEW_LEVEL;
	this.start();
	
	
}


}

draw(ctx){
[...this.gameObjects,...this.bricks].forEach((object)=>{object.draw(ctx)});	
if(this.gamestate==GAME_SATATE.PAUSED){

ctx.rect(0,0,this.gamewidth,this.gameheight);
ctx.fillStyle="rgba(0,0,0,0.5)";
ctx.fill()
ctx.font="40px Arial"

ctx.fillStyle="blue";
ctx.textAlign="center";
ctx.fillText("PAUSED",this.gamewidth/2,this.gameheight/2);	
	
	
}

if(this.gamestate==GAME_SATATE.MENU){

ctx.rect(0,0,this.gamewidth,this.gameheight);
ctx.fillStyle="black";
ctx.fill()
ctx.font="40px Arial"

ctx.fillStyle="navy";
ctx.textAlign="center";
ctx.fillText("Press space to start",this.gamewidth/2,this.gameheight/2);	
	
	
}
if(this.gamestate==GAME_SATATE.GAME_OVER){

ctx.rect(0,0,this.gamewidth,this.gameheight);
ctx.fillStyle="black";
ctx.fill()
ctx.font="40px Arial"

ctx.fillStyle="red";
ctx.textAlign="center";
ctx.fillText("GAME OVER",this.gamewidth/2,this.gameheight/2);	
	
	
}







	
}
tooglePause(){
	if(this.gamestate==GAME_SATATE.PAUSED){
		this.gamestate=GAME_SATATE.RUNNING;
	}else{
		this.gamestate=GAME_SATATE.PAUSED;
	}
	
}

	
	
}
   
	
	
	
	
	
	function levelsOb(game,level){
		let bricks=[];
		level.forEach((rows,rowindex)=>{
			rows.forEach((brick,brickindex)=>{
				if(brick===1){
				let position={
					x:80*brickindex,
					y:75+24*rowindex
				}
				bricks.push(new Brick(game,position));}
				
			})
			
		})
		return bricks;
	}
		
	
	
	function detection(ball,gameObject){
let topOfBall=ball.position.y;		
let topOfObject= gameObject.position.y;
let bottomOfBall =   ball.position.y + ball.size;
let objectLeft=gameObject.position.x;
let objectRight=gameObject.position.x+gameObject.width;

let objectBottom= gameObject.position.y+gameObject.height;

if(bottomOfBall >=topOfObject
&& topOfBall <=objectBottom 
&& ball.position.x>=objectLeft 
&& ball.position.x+ball.size <=objectRight){	
		return true;
		
		
	}
	else{return false;}}
	
	
	
	
	
	

var canvas=document.getElementById("canvas");
const GAME_WIDTH=800;
const GAME_HEIGHT=600;
var ctx=canvas.getContext('2d');
ctx.clearRect(0,0,800,600);

var game=new Game(GAME_WIDTH,GAME_HEIGHT);

var LastTime=0;
function gameloop(timestamp){
var deltatime=timestamp-LastTime;
LastTime=timestamp;
ctx.clearRect(0,0,GAME_WIDTH,GAME_HEIGHT);
game.draw(ctx);
game.update(deltatime);
requestAnimationFrame(gameloop);

}
requestAnimationFrame(gameloop);
	