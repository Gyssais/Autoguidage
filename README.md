# Autoguidage

## Nouvel algo !

Conçu pour suivre des étoiles, et non plus un cercle.
* Sature l'image : tous les pixels sous un seuil -> noirs, au dessus -> blancs
* Ajoute un cercle blanc autour de chaque pixel blanc (pour que la détection de contours soit plus efficace) (ça marche pas à chaque fois, j'ai pas bien compris pourquoi)
* Détecte les contours de ces cercles blancs
* Calcul le centre de ces contours. On obtient ainsi la position des étoiles les plus lumineuses de l'image.
* Recommence le calcul avec une autre image (les mêmes étoiles, mais qui ont un peu bougé)
* Calcule la moyenne des écarts entre les étoiles des deux images
* On obtient de combien de pixels les étoiles se sont déplacées, sur les deux axes

## Ancien

Exemple d'utilisation de la librairie opencv en python. Le script permet de détetecter un cercle (j'avais pensé ça pour Mercure). On pourrait adapter ça à une étoile. Et à un flux video au lieu d'une photo.

Il faut juste installer opencv sur la Pi : c'est pas très compliqué, juste long (il faut recompiler la librairie)


