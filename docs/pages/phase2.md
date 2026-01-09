---
title: Phase 2 contexte de lecture
layout: home
nav_order: 3
permalink: phase2.html
---

# La campagne "Contexte de lecture"

## L'interface

Les clefs, armures et métriques constituent le *contexte 
de lecture et d'interprétation* des objets musicaux 
(notes, silences et accords). Il sont initialisés 
sur la première mesure, et peuvent changer en 
cours de partition. L'interface surligne tous ces changements, 
en jaune si l'OMR estime  que la reconnaissance est correcte, 
en rouge sinon. 

L'utilisateur peut vérifier la
reconnaissance grâce à l'interface ci-dessous qui met en vis-à-vis
l'image et sa reconnaissance.


{% include image.html
file="collab-phase2.png" alt="Interface de la phase 2"  %} 


## Vérifications et actions

On demande à l'utilisateur de vérifier tous les éléments qui conditionnent l'interprétation  des notes. 

Ces éléments sont

 - Armures (en cas de niveau de confiance assez faible)
 - Clefs (en cas de niveau de confiance assez faible)
 - Métrique (en cas de doute sur la durée de la mesure)

Dans cette phase, nous vérifions les clefs, les armures et la métrique. Vous devez contrôler la correspondance entre l'image et la partition pour chacun de ces éléments, en ne considérant que ce qui est surligné. 

Tous les éléments surlignés peuvent être **édités** en cliquant sur leur représentation sur la partition à droite. Une interface vous permet de corriger l'élément si nécessaire, puis de valider la correction avec "OK". Tous les éléments validés après correction deviennent verts. 

Les éléments en rouge sont considérés comme suspects et doivent être édités et validés avec "OK" ; les éléments en jaune sont en principe corrects. Vous pouvez les contrôler visuellement et les éditer seulement si c'est nécessaire.

Le système recalcule la transcription au fur et à mesure des corrections. Validez chaque page après correction, jusqu’à la dernière: tous les éléments rouges doivent normalement être alors passés au vert.

