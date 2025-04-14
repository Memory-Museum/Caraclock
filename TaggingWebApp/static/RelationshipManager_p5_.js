// Implemented by Dr. Jones and belen

// DEFAULT CIRCLES = 4
// 1. to-do ASK USER FOR HOW MANY PEOPLE AND NAMES, generate  circles
// 2. user can drag circles around. background colors signal "closeness"
// 3. (currently in mouseReleased()) - calculate distances and print them out
// 4. modify Ball.prettyprint() to be appropriate json format
// 5. based on 


const circle_colors = [0, 30, 60, 120, 210, 270, 300, 350] //8 preset values for rainbow (HSB), can expand this

// Retrieve the names from localStorage
const storedNames = localStorage.getItem("familyNames");

// Parse the string into an array if it exists, or use an empty array if not
const names = storedNames ? storedNames.split(','): [];


let dragPoint; // temp for dragging balls around
let balls = [];

let num_circles = 5;
const dragRadius = 20;
let dragColor = 0;


function setup() {
  createCanvas(400, 400);
  colorMode(HSB);
  textAlign(CENTER, CENTER);
  
  //Create how many circles are needed
  for (let i =0; i < num_circles; i++){
    let tempBall = new Ball(random(width/2-50,width/2+50), random(height/2-50, height/2+50), dragRadius, circle_colors[i], names[i]);
    balls.push(tempBall);

  }
}

function draw() {
  background(220);
  //background circles
  {push();
  noStroke();
  fill(54,21,100);
  circle(width/2, height/2, width+(width/2));
  fill(131,21,100);
  circle(width/2, height/2, width/1.5);
  fill(284, 28, 100);
  circle(width/2, height/2, width/4);
  pop();
  }
  
  
  //DRAW ALL THE CIRCLES 
  for(let b of balls){
    b.show()
  }
    
}

function mousePressed(){
  //move backwards through the array, b/c order of drawing (top to bot)  
  for(let i = balls.length-1; i>=0; i--){
    //check if mouse is in any of the circles
    if(balls[i].mouseInCircle()){
      print("IN");
      dragPoint = balls.splice(i, 1)[0]; //take 1 item at index i out of the points array, save to dragPoint (javascript array)
      dragPoint.pos.x = mouseX;
      dragPoint.pos.y = mouseY;
      balls.push(dragPoint); //put current point back into points array, but now drawn on top and the new circle will follow the mouse
    }
  }
  print(balls);
}

function mouseReleased(){
  dragPoint.calculateDistances(balls);
  dragPoint.prettyPrint();
  dragPoint = null;
}

function mouseDragged(){
  //check if not null
  if(dragPoint){
    dragPoint.pos.x = mouseX;
    dragPoint.pos.y = mouseY;
  }
  
}

function keyPressed(){
  //activate calculate distance
}

class Ball{
  constructor(x, y, circleRadius, circleHue, name){
    this.pos = createVector(x, y);
    this.radius = circleRadius;
    this.innerHue = circleHue;
    this.name = name;
    this.distances = []; //save (name, distance)
  }
  
  show(){
    print("draw ", this);
    push();
    strokeWeight(5);
    fill(this.innerHue,100, 100);
    circle(this.pos.x, this.pos.y, this.radius *2);
    pop();//anywhere in the circle
    textAlign(CENTER, CENTER);
    textSize(21);
    text(this.name, this.pos.x, this.pos.y); 
  }
  
  mouseInCircle(){
    return dist(mouseX, mouseY, this.pos.x, this.pos.y) < this.radius
  }

  calculateDistances(otherBalls){
    for(let ob of otherBalls){
      if (ob.name != this.name){
        let tempName = ob.name;
        let distanceBetween = this.pos.dist(ob.pos);
        this.distances.push(createVector(tempName, distanceBetween));
      }
    }
  }
  
  prettyPrint(){
    print("Ball", this.name, "distance from: ");
    
    for(let d of this.distances){
      print("- ", d.x, d.y);
    }
  }
}
