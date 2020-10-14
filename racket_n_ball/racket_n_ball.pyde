ballX = 0
ballY = 0
ballSpeedX = 5
ballSpeedY = 2
ballRadius = 5

racketWidth = 50
racketHeight = 10
racketX = 0
racketY = 0

#ici on definit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    #on dit qu'on va faire référence à la variable global
    global ballX, ballY, racketX, racketY, racketWidth
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #on definit la taille de la fenêtre
    size(400, 400)
    #vide la fenêtre
    clear()
    #on change le frameRate de l'application
    frameRate(60)
    ballX = width/2
    ballY = height/2
    
    racketX = mouseX - (racketWidth/2)
    racketY = height - 50
    
def draw():
    clear()
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
    global ballX, ballY, ballSpeedX, ballSpeedY, ballRadius
    global racketX, racketY, racketWidth, racketHeight
    
    #ballX = ballX + ballSpeedX
    #ballY = ballY + ballSpeedY
    #idem a ce qu'il y a au dessus
    ballX += ballSpeedX
    ballY += ballSpeedY
    
    #haut et bas   
    if(ballY-ballRadius < 0):
        ballSpeedY *= -1
        ballY = ballRadius
    elif(ballY+ballRadius > height):
        ballSpeedY *= -1
        ballY = height-ballRadius
    
    #droite et gauche
    if(ballX+ballRadius > width):
        ballSpeedX *= -1
        ballX = width-ballRadius
    elif(ballX-ballRadius < 0):
        ballSpeedX *= -1
        ballX = ballRadius
    
    if(racketY < ballY+ballRadius < racketY+racketHeight and ballSpeedY > 0):
        if(racketX < ballX < racketX + racketWidth):
            ballSpeedY *= -1
            ballY = racketY-ballRadius
    
    
    #draw circle
    circle(ballX, ballY, 2*ballRadius);
    
 
    
       
          
             
                
                   
                      
                         
                            
        
