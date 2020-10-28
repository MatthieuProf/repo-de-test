# Algo python

## Télécharger et installer Processing, et le mettre en mode python :
https://processing.org/

### Notions de bases
Par défaut deux fonctions principales sont appelées par Processing :
- la fonction ```setup()``` qui s'exécute au démarrage du programme
- la fonction ```draw()``` qui s'exécute en boucle à chaque frame

Processing donne accès à une API comprenant un certain nombre de fonctions et de variables utiles pour créer un petit programme graphique :
https://py.processing.org/reference/

Par exemple on peut accéder à la postion de la souris grâce aux variables ```mouseX``` et ```mouseY```, ou encore la taille de l'écran avec ```width``` et ```height```
On peut aussi facilement dessiner un cercle grâce à la fonction ```circle()``` : https://py.processing.org/reference/circle.html

### Définition et utilisation d'une fonction
Un fonction permet de regrouper des instructions afin d'organiser notre programme et de le faire étape par étape

Pour créer un fonction en python on utilise la syntaxe suivante :
```
def foo():
  #instructions de la fonction
```
Pour appeler une fonction en python on utilise la syntaxe suivante :
```
foo()
```

### Définition et utilisation d'une variable
Les variables permettent de stocker des informations comme un nombre dans la mémoire du programme.

Pour créer une variable en python il suffit de la nommer :
```
mavar = 12
```
Pour utiliser une variable il suffit de l'appeler par son nom :
```
calcul = mavar + 10
```
ici la variable ```calcul``` sera égale à la variable ```mavar``` + 10

Attention une variable qui est crée dans une fonction ne sera accessible que dans cette même fonction, pour créer une variable globale il faut la créer en dehors des fonctions, de préférence en début de programme. Pour y accéder dans une fonction il faut penser à utiliser le mot-clé ```global``` 
```
mavar = 10
def foo():
  global mavar
```

### Condition
L'utilisation des conditions permet d'exécuter une serie d'instruction uniquement si la condition est respectée. On utilise la syntaxe suivante.
```
if(condition):
  #faire les instructions
```
Nous avons accès à un certains nombre de comparateur pour faire des instructions, par exemple :

``` if(a < b): ``` si a est inférieur à b 

``` if(a > b): ``` si a est supérieur à b 

``` if(a <= b): ``` si a est inférieur ou égal à b 

``` if(a >= b): ``` si a est supérieur ou égal à b 

``` if(a < b and c > d): ``` si a est inférieur à b et si c est supérieur à d

``` if(a < b or c > d): ``` si a est inférieur à b ou si c est supérieur à d

``` if(a == b): ``` si a est égal à b

``` if(a != b): ``` si a est différent de b 

### Github
L'utilisation de github nécessite l'usage de trois commandes :

``` commit``` Permet de créer une version du code et commenter cette version sur le repo.

``` pull ``` Permet de récupérer le code sur le repo.

``` push ``` Permet d'envoyer les commit locaux (qui ne sont pas encore sur le repo) sur le repo.

### Delta time
Lorsqu'on déplace un objet en modifiant ces coordonnées dans la fonction ```draw()``` cela peut poser un problème en cas de chute de fps. En effet la fonction ```draw()``` est appelée en général 30 fois par seconde, mais ce nombre peut chuter si le processeur ralenti. Cela aura pour conséquence de ralentir le déplacement de l'objet.
Pour ne plus être dépendant du framerate la solution est de calculer la vitesse en fonction du temps. Dans processing nous devont donc calculer le temps entre de frame que nous appelerons detlatime et rendre la vitesse fonction de ce detlatime.
Nous utiliserons pour cela la fonction ```millis()``` qui permet de connaitre le temps depuis lequel le programme est lancé.
```
deltatime = 0
lastframetime = 0

def setup():
  lastframetime = millis()
  
 def draw():
  deltatime = lastframetime - millis()
  lastframetime = millis()
```

### Boucle for
Lorsque l'on doit effectuer une instruction ou une série d'instruction plusieurs fois plutôt que copier/coller le code pour répéter l'opération nous utiliserons des itérations.
Une des méthodes d'itération est la boucle for.

```
for i in range(8):
  print(i)
```

Ici la boucle effectuera 8 itérations et i évoluera donc entre 0 et 7.

### Notion mathématique
La trigonométrie est une notion importante lorsque l'on développe des jeux vidéos : https://fr.wikipedia.org/wiki/Cercle_trigonom%C3%A9trique
