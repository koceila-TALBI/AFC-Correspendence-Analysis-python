# AFC-Correspendence-Analysis-python
Un exemple d'Analyse Factoriel des Correspondences en python avec de brèves explications 

L’analyse factoielle des corréspondences est une méthode qui permet de ré-
duire un tableau de deux vairables qualitatives qui possède chacune plusieurs
modalités en un tableaux plus simple, si simple qu’ils peuvent être traduits
en graphiques.
Les étapes que nous allons suivre :

1. Diviser toutes les cellules par le nombre total afin de travailler sur de
proportions (matrice des proportion observée)
2. Calculer les sommes marginales, le résultat doit être un vecteur colonne
et un vecteur ligne
3. Faire un produit du vecteur colonnes par le vecteur lignes pour obtenir
la matrice d’indépendance
4. Matrice d’écart à l’indépendance
5. Décomposition en valeurs singulères (SVD)
6. Coordonnées des modalités dans les plans factoriels
