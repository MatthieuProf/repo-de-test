#ceci est un commentaire, il ne sera pas exécuté par la machine

#ici on definit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #on definit la taille de la fenêtre
    size(400, 400)
    #vide la fenêtre
    clear()
    #on change le frameRate de l'application
    frameRate(60)
    
def draw():
    #clear()
    fill(255)
    #dessine une elipse avec les paramètres suivant x, y, largeur de l'ellipse, hauteur de l'ellipse
    #on récupère les coordonnées de la souris avec mouseX et mouseY
    #ellipse(mouseX, mouseY, 80, 80)
    ellipse(width/2 + cos(millis() * 0.0005) * 100, height/2 + cos(millis() * 0.002) * 100, 40, 40)
