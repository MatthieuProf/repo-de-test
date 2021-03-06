ballX = 0
ballY = 0
lastBallX = 0
lastBallY = 0

ballSpeed = 0.2
ballSpeedX = 0
ballSpeedY = 0
ballAngle = PI/5

ballRadius = 5
ballAngleMax = PI/1.9

racketWidth = 100
racketHeight = 10
racketX = 0
racketY = 0

lastFrameTime = 0
deltaTime = 0

bricks = [1, 1, 1, 1, 1, 1, 1, 1]

#ici on definit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    #on dit qu'on va faire référence à la variable global
    global ballX, ballY, racketX, racketY, racketWidth
    global lastFrameTime
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #affiche le tableau bricks dans la console
    print(bricks)
    #affiche la valeur de bricks à l'index 0 
    print(bricks[0])
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
    global bricks
    
    clear()
    
    deltaTime = millis() - lastFrameTime
    lastFrameTime = millis()
    
    drawRacket()
    drawBall()
    
    for i in range(len(bricks)):
        if(bricks[i] > 0):
            drawBricks(i*50, 50, 50, 20, i)
    
    #print(bricks)
    
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
    global ballX, ballY, lastBallX, lastBallY, ballRadius, ballAngle, ballSpeed, ballSpeedX, ballSpeedY
    global racketX, racketY, racketWidth, racketHeight
    global deltaTime
    global ballAngleMax
    
    lastBallX = ballX
    lastBallY = ballY
    
    #idem a ce qu'il y a au dessus
    ballSpeedX = cos(ballAngle) * ballSpeed * deltaTime
    ballSpeedY = sin(ballAngle) * ballSpeed * deltaTime
    ballX += ballSpeedX
    ballY -= ballSpeedY
    
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
    
    if(racketY < ballY+ballRadius < racketY+racketHeight and ballSpeedY < 0):
        if(racketX < ballX < racketX + racketWidth):
            ratio = (ballX - racketX - racketWidth/2) / (racketWidth/2)
            ballAngle = PI/2 - ratio * ballAngleMax
            ballY = racketY-ballRadius
    
    
    #draw circle
    circle(ballX, ballY, 2*ballRadius);
    
    
#une fonction peut prendre des paramètres    
def drawBricks(bX, bY, bW, bH, index):
    
    global ballX, ballY, ballRadius, ballSpeedX, ballSpeedY, ballAngle
    global bricks
    
    rect(bX, bY, bW, bH)
    
    if(bX < ballX < bX+bW and bY < ballY < bY+bH):
        print("collision")
        
        aBall = (lastBallY-ballY) / (lastBallX-ballX)
        bBall = ballY - (aBall * ballX)
        
        yLeft = aBall*bX + bBall
        yRight = aBall*(bX+bW) + bBall
        '''
        xTop = (bY-bBall)/aBall
        xBottom = ((bY+bH)-bBall)/aBall
        
        
        fill(255, 0, 0)
        circle(xTop, bY, 10)
        circle(xBottom, bY+bH, 10)
        
        fill(0, 0, 255)
        circle(bX, yLeft, 10)
        circle(bX+bW, yRight, 10)
        '''
        
        if(bY < yLeft < bY+bH and lastBallX < bX < ballX):
            ballAngle = PI - ballAngle
            ballX = bX - ballRadius
            bricks[index] = 0
        elif(bY < yRight < bY+bH and ballX < bX+bW < lastBallX):
            ballAngle = PI - ballAngle
            ballX = bX+bW + ballRadius
            bricks[index] = 0
        elif(ballSpeedY < 0):
            ballAngle = -ballAngle
            ballY = bY-ballRadius
            bricks[index] = 0
        else:
            ballAngle = -ballAngle
            ballY = bY+bH+ballRadius
            bricks[index] = 0
        
        
    
    '''
    if(bX < ballX < bX+bW):
        if(bY < ballY+ballRadius < bY+bH and ballSpeedY < 0):
            ballAngle = -ballAngle
            ballY = bY-ballRadius
            bricks[index] = 0
        elif(bY < ballY-ballRadius < bY+bH and ballSpeedY > 0):
            ballAngle = -ballAngle
            ballY = bY+bH+ballRadius
            bricks[index] = 0
        
    elif(bY < ballY < bY+bH):
        if(bX < ballX+ballRadius < bX+bW and ballSpeedX > 0):
            ballAngle = PI - ballAngle
            ballX = bX - ballRadius
            bricks[index] = 0
        elif(bX < ballX-ballRadius < bX+bW and ballSpeedX < 0):
            ballAngle = PI - ballAngle
            ballX = bX + bW + ballRadius
            bricks[index] = 0
    '''
        
    
    
       
          
             
                
                   
                      
                         
                            
        
