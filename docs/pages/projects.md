---
title: Projects
layout: home
nav_order: 3
permalink: projects.html
---

# Projects

###	Campagnes
C’est dans cette section qu’on va pouvoir planifier les différentes phases (campagnes) à corriger.<br>
Le tableau affiche l’ID de la campagne, le Nom de la campagne, le nom du Corpus (Projet), le Mode de correction pour la phase ainsi que le nom du Créateur de la phase.<br>
Dans notre cas, on utilisera en Mode : **Instrumentation**, **Reading Context** ou **Music Object**.<br>
Instrumentation pour la partie de reconnaissance des différentes parties instrumentales.<br>
Reading Context pour la partie de reconnaissance des armures, clefs et métrique.<br>
Music Object pour la partie de reconnaissance de hauteur des notes, altérations et durée des notes.<br>
Pour la création d’une campagne on aura besoin de remplir les champs suivants :
-	Nom (input text)
-	Créateur (select)
-	Projet (select)
-	Mode (select)
-	Etat (sélecteur)
-	Description (textarea)
-	Nombre de tâches à assigner par volontaire (select)
-	Nombre d’assignations autorisées pour les tâches disponibles (select)
-	Configuration (textarea)


###	Images
C’est dans cette section qu’on va faire les appels d’images (partitions) IIIF depuis la database Gallica.<br>
Le tableau affiche l’ID de l’image, son URL IIIF ainsi que ses dimensions (Largeur et Hauteur).<br>
Pour importer une nouvelle image on doit cliquer sur *(Ajouter Image +)* en haut à droite.<br>
On aura besoin de son URL IIIF et de ses dimensions :
-	URL IIIF (input URL)
-	Largeur (input number)
-	Hauteur (input number)


###	Projets
C’est dans cette section que la création du corpus (Projet) est faite.<br>
Le tableau affiche l’ID du projet, le nom du Projet, son statut (Public ou non), son Fournisseur et la Date de création.<br>
Pour créer un nouveau projet, on doit cliquer sur *(Ajouter Projet +)* en haut à droite.<br>
Il faudra sélectionner le Fournisseur qui servira pour le corpus ainsi que spécifier l’identifiant des objets à utiliser.<br>
Le Token d’invitation pour le projet est généré automatiquement à la création.<br>
On peut y ajouter les utilisateurs qui devront participer à ce corpus ainsi que spécifier leurs rôles.<br>
Pour la création du projet il faudra remplir les champs suivants :
-	Nom (input text)
-	Description (textarea)
-	Illustration (input file)
-	Public (checkbox)
-	Token d’invitation (input text)
-	Fournisseur (select)
-	Identifiant de l’objet chez le fournisseur (input text)
-	Informations supplémentaires venant du fournisseur (textarea)
-	Utilisateur (select)

### Types
C’est ici qu’on va déclarer les différents types qui serviront à classer les différents éléments dans des catégories.<br>
Le tableau affiche l’ID du type, le Nom du type, si c’est un dossier ou non, le Projet du type ainsi que son Fournisseur.<br>
Pour créer un nouveau Type, on doit cliquer sur *(Ajouter Type +)* en haut à droite.<br>
Pour créer un type, on aura besoin de lier le type à un Fournisseur et de lui attribuer un Identifiant Objet.<br>
Les différents champs à remplir pour la création d’un type sont les suivants :
-	Nom (input text)
-	Dossier (checkbox)
-	Couleur (input text)
-	Projet (select)
-	Fournisseur (select)
-	Identifiant de l’objet chez le fournisseur (input text)

### Eléments
C’est dans cette section qu’on va pouvoir lier tous les différents éléments rajoutés plus tôt ensemble.<br>
Le tableau affiche l’ID de l’élément, son Nom, son Type, le Projet qui lui est lié, son Fournisseur ainsi que son ID d’objet renvoyé par le Fournisseur.<br>
Pour créer un nouvel Elément, on doit cliquer sur *(Ajouter Elément +)* en haut à droite.<br>
Il n’y a pas besoin de spécifier un Parent quand on créé un élément du type Opus.<br>
Il faut spécifier un Parent quand l’élément qu’on créé appartient à un Opus et est de type ScorePage.<br>
Les différents champs à remplir pour la création d’un élément sont les suivants :
-	Nom (input text)
-	Type (select)
-	Projet (select)
-	Parent (select)
-	Image (select)
-	Polygone (textarea)
-	Fournisseur (select)
-	Identifiant de l’objet chez le fournisseur (input text)
-	Campagne (select)
