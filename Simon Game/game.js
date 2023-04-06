var buttonColours=["red", "blue", "green", "yellow"]
var gamePattern=[]
var userClickedPattern=[]

var started=false
var level= 0

$(document).keypress(function(event) {
	if(!started){
		$("#level-title").text("Level "+level)
		nextSequence()
		started =true
	}	
});

$('.btn').click(function() {
	var userChosenColour =$(this).attr('id'); //"this" stores the value returned by $('.btn')
	// here "this.attr('id')" is giving values like yellow green red blue 
	// console.log(userChosenColour)

	userClickedPattern.push(userChosenColour)
	playSound(userChosenColour);
	animatePress(userChosenColour);
	checkAnswer(userClickedPattern.length-1);
});



function playSound(name) {
	var audio= new Audio("sounds/"+name+".mp3")
	audio.play()
}

function animatePress(currentColour){
	$("."+currentColour).addClass('pressed')
	setTimeout(function(){
		$("."+currentColour).removeClass("pressed")
	}, 100)
	//we can use "#" instead of "." as both class name and id are same here
}

function checkAnswer (currentLevel) {
	// console.log(currentLevel)
	// console.log("gamePattern ",gamePattern)
	// console.log("userClickedPattern ",userClickedPattern)

	// console.log('gamePattern[currentLevel] ',gamePattern[currentLevel])
	// console.log('userClickedPattern[currentLevel] ',userClickedPattern[currentLevel])
	// console.log('gamePattern.length ',gamePattern.length)
	// console.log('userClickedPattern.length ',userClickedPattern.length)

	//currentLevel is same as index

	if (gamePattern[currentLevel]===userClickedPattern[currentLevel])
	{
		if (gamePattern.length===userClickedPattern.length)
		{
			setTimeout(function () {
				nextSequence() // repeating 
			}
				,1000)
		}
	}
	else{
		playSound("wrong")

		$("body").addClass("game-over")
		setTimeout(function(){
			$("body").removeClass("game-over")
		},200)

		$("#level-title").text("Game Over, Press Any Key to Restart");

		startOver()
	}	
}

function startOver(){
	gamePattern=[]
	// userClickedPattern=[]

	started=false
	level= 0
}

function nextSequence(){
	userClickedPattern = [];

	
	$("#level-title").text("Level "+level)
	level++

	var randomNumber=Math.floor(Math.random() * 4)
	var randomChosenColour=buttonColours[randomNumber]
	gamePattern.push(randomChosenColour)

	$("#"+randomChosenColour).fadeIn(100).fadeOut(100).fadeIn(100)
	playSound(randomChosenColour);
	// animatePress(randomChosenColour)	

}