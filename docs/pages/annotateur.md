---
title: Annotateurs
layout: home
nav_order: 1
permalink: annotateur.html
---

# Présentation générale des tâches d'annotation


Chaque annotateur se voit attribuer des *tâches* 
à effectuer via des interfaces qui ont
en commun de présenter l'interprétation
de l'OMR et de permettre aux utilisateur d'effectuer
certaines corrections. Ces tâches s'effectuent
dans le cadre de *campagnes* déclenchées par les
administrateurs de CollabScore, et chaque campagne a lieu
dans le contexte d'un projet qui rassemble l'ensemble des documents
à annoter. 

## Projets, campagnes et tâches

Commençons par la notion de ¨*projet*. Un projet est un ensemble de
documents à annoter. Les administrateurs peuvent par exemple placer
dans un projet une partie des œuvres de Saint-Saëns (disons, les mélodies),
dans un autre projet une autre partie (disons, les œuvres pour piano), dans
un troisième des œuvres de Debussy ou de tout autre compositeur, etc.

Un annotateur est inscrit dans un ou plusieurs projets et la
liste des projets est la première page affichée après connexion,
comme le montre l'exemple de la figure ci-dessous.
 
{% include image.html
file="liste-projets.png" alt="La page montrant les projets auxquels vous participez"  %} 

Pour chaque projet, les administrateurs créent des *campagnes d'annotation* 
qui rassemblent des tâches distribuées aux annotateurs. Les tâches
au sein d'une même campagne sont homogènes, mais chaque campagne
correspond à un certain type d'annotation, par exemple la correction
des parties, des clés, ou des notes. Les types de campagnes 
de CollabScore sont détaillées ci-dessous. 

En général, une campagne d'un certain type
produira une tâche par œuvre, chaque tâche étant
affectée à un seul annotateur.  Il existe cependant
d'autres possibilités: un administrateur peut créer
plusieuts tâches pour une même œuvre, de manière à 
pouvoir synthétiser les corrections faites 
par chaque annotateur. 
La figure suivante 
mmontre, pour un projet donné, les campagnes et le bouton
d'accès à la liste des tâches.

{% include image.html
file="liste-campagnes.png" alt="La page montrant les campagnes"  %} 

Enfin, la liste des tâches montre les documents à annoter. En cliquant sur
le bouton "Annoter" d'une tâche on accède à l'interface spcéifique
à la campagne en cours.

{% include image.html
file="liste-taches.png" alt="La page la liste de tâches"  %} 

## Les campagnes d'annotation

Il existe essentiellement trois types de campagnes, correspondant
à des tâches qui sont conçues pour se succéder
dans un ordre strict. Chaque tâche s'effectue à une 
certaine granularité (tout le document, ou seulement une
page, etc.), et concerne une partie des éléments
de la notation musicale. 

## La campagne d'instrumentation

La première est intitulée **"Instrumentation"**. Elle permet 
de vérifier que les parties instrumentales ont bien été identifiées,
et de s'assurer que chaque portée est bien affectée à la
bonne partie. Il s'agit d'une condition préalable à la
bonne interprétation du contenu musical. 
**[Cette campagne est décrite en détail ici]({% link pages/phase1.md %})**.
 
 
## La campagne des contextes de lecture

La seconde campagne porte sur le **contexte de lecture**. le but
est de vérifier la bonne reconnaissance des clés, armures et métriques.
Toute erreur sur l'un de ces éléments a en effet un impact
sur l'interprétation des symboles musicaux (notes, silences, etc.).
 **[Cette campagne est décrite en détail ici]({% link pages/phase2.md %})**.
 

## La campagne des objets musicaux

Enfin, en supposant les parties bien identifiées et localisées sur les portées (phase 1), et 
les éléments d'interprétation corrects (phase 2), 
la campagne de phase 3, intitulée **Objets musicaux**
propose  à l'utilisateur de corriger 
les éléments locaux.

  - Durée, hauteur, altération des notes
  - Durée des silences
  - Eventuellement ajout ou suppression d'éléments

**[Cette campagne est décrite en détail ici]({% link pages/phase3.md %})**.
 