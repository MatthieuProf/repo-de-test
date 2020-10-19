ballX = 0
ballY = 0
ballSpeedX = 0.3
ballSpeedY = 0.1

ballSpeed = 0.1
ballAngle = PI/5

ballRadius = 5

racketWidth = 100
racketHeight = 10
racketX = 0
racketY = 0

lastFrameTime = 0
deltaTime = 0

#ici on definit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    #on dit qu'on va faire référence à la variable global
    global ballX, ballY, racketX, racketY, racketWidth
    global lastFrameTime
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #on definit la taille de la fenêtre
    size(400, 400)
    #vide la fenêtre
    clear()
    #on change le frameRate de l'application
    frameRate(30)
    ballX = width/2
    ballY = height/2
    
    racketX = mouseX - (racketWidth/2)
    racketY = height - 50
    
    lastFrameTime = millis()
    
def draw():
    global deltaTime, lastFrameTime
    
    clear()
    
    deltaTime = millis() - lastFrameTime
    lastFrameTime = millis()
    
    drawRacket()
    drawBall()
    
    
    
def drawRacket():
    global racketX, racketY, racketWidth, racketHeight
    fill(255)
    #draw a rectangle in coords
    # x : mouseX minus half of width
    # y : height of the window minus 20
    # width : 50
    # height : 10
    racketX = mouseX - (racketWidth/2)
    rect(racketX, racketY, racketWidth, racketHeight)
    
def drawBall():
    global ballX, ballY, ballSpeedX, ballSpeedY, ballRadius, ballAngle, ballSpeed
    global racketX, racketY, racketWidth, racketHeight
    global deltaTime
    
    #idem a ce qu'il y a au dessus
    ballX += cos(ballAngle) * ballSpeed * deltaTime
    ballY -= sin(ballAngle) * ballSpeed * deltaTime
    
    #haut et bas   
    if(ballY-ballRadius < 0):
        ballAngle = -ballAngle
        ballY = ballRadius
    elif(ballY+ballRadius > height):
        ballAngle = -ballAngle
        ballY = height-ballRadius
    
    #droite et gauche
    if(ballX+ballRadius > width):
        ballAngle = PI - ballAngle
        ballX = width-ballRadius
    elif(ballX-ballRadius < 0):
        ballAngle = PI - ballAngle
        ballX = ballRadius
    
    if(racketY < ballY+ballRadius < racketY+racketHeight and ballSpeedY > 0):
        if(racketX < ballX < racketX + racketWidth):
            ballSpeedY *= -1
            ballY = racketY-ballRadius
    
    
    #draw circle
    circle(ballX, ballY, 2*ballRadius);
    
 
    
       
          
             
                
                   
                      
                         
                            
        
