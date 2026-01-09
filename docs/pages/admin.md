---
title: Administrateurs
layout: home
nav_order: 1
permalink: admin.html
---

# Administration du site, vue d'ensemble

Le système collaboratif de CollabScore est basé
sur Callico, une plate-forme d'annotation Open Source
proposée par la société Teklia. Il existe une
[documentation Callico](https://doc.callico.eu/) 
et ce qui suit ne concerne donc que ce qui est spécifique 
à CollabScore à savoir:

 - l'import des documents à annoter se 
   fait depuis [Neuma](https://neuma.huma-num.fr) au lieu de ArkIndex
 - de même, après chaque campagne, les annotations sont retransmises
   à Neuma qui les prend en compte dans la production des partitions
   éditables.
 - enfin (et surtout), nous avons développé dans CollabScore des
   interfaces d'annotation spécifiques aux partitions musicales.

## Annotations et opérations d'édition

Les annotations produites par les interfaces CollabScore
contiennent des *opérations
d'édition* qui vont s'appliquer ensuite au moment de la regénération
des partitions afin de corriger, compléter ou
valider les choix effectués par l'OMR. Une opération d'édition
peut consister par exemple à demander le changement de hauteur d'une note,
le remplacement d'une clé, le nommage d'une partie, etc. 

Chaque campagne 
produit des opérations d'édition à appliquer aux partitions.
Après chaque campagne, il faut donc transmettre à Neuma les
opérations d'édition collectées afin qu'elles soient prises
en compte à la prochaine regénération des partitions. Ce sont
ces partitions corrigées à l'issue d'une phase qui
sont soumises à la phase suivante. Il existe en effet 
une dépendance entre les campagnes, qui explique
l'ordre dans lequel elles doivent se succéder. Il faut par exemple
avoir corrigé une clé ou une armure pour pouvoir correctement
vérifier les altérations des notes.
