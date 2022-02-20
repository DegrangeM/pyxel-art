# Pyxel-Art

Pyxel-Art est à la fois une bibliothèque permettant de créer des exercices corrigés de programmation où les élèves doivent suivre un programme python dessinant un pixel-art et à la fois une collection d'exercices basés sur cette bibliothèque. Ces exercices peuvent être utilisés pour des activités débranchées.

## La banque d'exercice
Vous pouvez retrouver l'ensemble des exercices de bases fournis ainsi que leur correction sur le [wiki](https://github.com/DegrangeM/pyxel-art/wiki/Solutions). Il y a au total 17 et ceux-ci sont disponibles dans les dossiers `exercices/sujets` et `exercices/corrections`. Deux fiches prêtes à l'emploi contenant ces exercices sont disponibles.

- [Fiche n°1](https://github.com/DegrangeM/pyxel-art/blob/master/pyxel-art.pdf) – Exercices 1 à 11 – ils portent sur l'utilisation des variables et des boucles de répétitions (remarque : les compteurs des boucles for ne sont volontairement pas exploitées)
- [Fiche n°2](https://github.com/DegrangeM/pyxel-art/blob/master/pyxel-art-2.pdf) – Exercice 12 à 17 – ils portent sur l'utilisaiton des boucles for généralisées (utilisation des compteurs)

## Le principe des exercices
La grille ci-dessous est données aux élèves :

<img src="https://user-images.githubusercontent.com/53106394/138447368-fda4e02f-c046-489f-a625-06a553f255e1.png" />

Ainsi qu'un programme Python :

<img src="https://user-images.githubusercontent.com/53106394/138447331-b49f9064-02b0-4fcd-9ef4-ace36e40d693.png" width="200" />

Les élèves doivent alors exécuter le programme dans leur tête et en déduire le pixel-art obtenu.

La bibliothèque permet de générer automatiquement une correction de l'exercice :

<img src="https://user-images.githubusercontent.com/53106394/138447375-97773530-6f5d-4645-9e03-13130189fe4b.png" />


## Organisation des fichiers

- À la racine se trouve un fichier `alien.pdf` à distribuer aux élèves. Ce fichier contient la grille de déplacement de l'alien ainsi que 20 cases réponses.

- Le dossier `exercices` contient les 20 exercices de bases

  - Le dossier `sujets` contient les programmes au format image

    - La ligne d'importation ainsi que la ligne de génération d'image sont automatiquement retirées lors de la génération de l'image

  - Le dossier `corrections` contient la correction des exercices
    
    - Le fichier `0.png` contient la grille de base avec l'alien 

  - Le dossier `libs` contient la librairie de base permettant de générer les corrections

  - Le dossier `tools` contient un fichier à exécuter pour générer les énoncés des programmes au format image

- Le dossier `ressources` contient les diverses ressources nécessaires au projet (images, polices, etc.)

- Le dossier `autres` contient divers fichiers en vrac

## Création d'exercices

Pour créer un exercice, il suffit de s'insiperer d'un des exercices de base fournis.

Exécuter le fichier permettra de générer la grille de correction.

Exécuter le programme dans le dossier tool permettra de générer le programme au format image.

## Exemples d'utilisation

- En cours pour introduire petit à petit les notions, en particulier quand les élèves n'ont pas encore accès à un ordinateur

- Pour générer des questions d'évaluations, et obtenir une correction qui pourra être envoyé aux élèves

- Utilisé avec des outils comme wooclap ou moodle

## License

Pyxel-Art est sous license MIT.
