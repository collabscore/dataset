---
title: Les interfaces collaboratives
layout: home
nav_order: 5
permalink: callico.html
---

# Callico, notre plate-forme collaborative

CollabScore a développé des interfaces qui soumettent 
les résultats "bruts" du système d’OMR, contenant les 
indications des zones à contrôler, à une communauté 
d'utilisateurs pour les valider et les corriger très 
rapidement. En effet, au lieu que l’utilisateur relise 
l’ensemble de la partition produite pour y rechercher 
des erreurs, ce qui est particulièrement  
long et fastidieux, grâce aux interfaces de CollabScore 
et aux erreurs signalées par l’OMR, 
les utilisateurs se focalisent directement et uniquement 
sur ces erreurs signalées.  

Les campagnes collaboratives sont organisées en 
trois phases consacrées respectivement à 
*l'instrumentation*, à la vérification des 
*contextes de lecture* et enfin à la vérification
des *objets musicaux*. Chaque phase permet de corriger
des éléments dont la validité conditionne celle des éléments
à vérifier dans la phase suivante. Par exemple, en phase 2,
l'utilisateur doit vérifier les armures reconnues
par le système OMR. Ce n'est que quand ces armures
sont validées qu'il est possible de regarder les notes et 
accords pour vérifier leurs altérations. 


## L'instrumentation

Une partition est écrite pour une ou plusieurs parties 
instrumentales ou vocales. La reconnaissance optique 
a tenté de les déterminer mais cette phase 
permet à l'utilisateur de vérifier
l'affectation d'un instrument à chaque partie, son 
intitulé (s'il existe) et son abréviation éventuelle.
L'image ci-dessous montre l'interface proposée.


{% include image.html
file="collab-phase1.png" alt="Interface de la phase 1"  %} 

## Le contexte de lecture

Les clefs, armures et métriques constituent le *contexte 
de lecture et d'interprétation* des objets musicaux 
(notes, silences et accords). Il sont initialisés 
sur la première mesure, et peuvent changer en 
cours de partition. L'interface surligne tous ces changements, 
en jaune si l'OMR estime  que la reconnaissance est correcte, 
en rouge sinon. L'utilisateur peut vérifier la
reconnaissance grâce à l'interface ci-dessous, et corriger
si nécessaire.


{% include image.html
file="collab-phase2.png" alt="Interface de la phase 2"  %} 

## Les objets musicaux 

En phase 3 nous considérons les objets musicaux suivants: 
notes, silences et accords. Comme dans la phase 2, 
les éléments en rouge sont considérés comme suspects et 
doivent être édités et validés avec "OK". Les autres éléments 
peuvent être édités, 
même s'ils ne sont pas surlignés. L'édition consiste 
à apporter des corrections à la durée (notes et silences), 
à la hauteur ou aux altérations (notes).


{% include image.html
file="collab-phase3.png" alt="Interface de la phase 3"  %} 
