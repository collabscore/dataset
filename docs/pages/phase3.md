---
title: Phase 3 objets musicaux
layout: home
nav_order: 4
permalink: phase3.html
---

# La campagne "Objets musicaux"

## L'interface


En phase 3 nous considérons les objets musicaux suivants: 
notes, silences et accords. Comme dans la phase 2, 
les éléments en rouge sont considérés comme suspects et 
doivent être édités et validés avec "OK". Les autres éléments 
peuvent être édités, 
même s'ils ne sont pas surlignés. L'édition consiste 
à apporter des corrections à la durée (notes et silences), 
à la hauteur ou aux altérations (notes).

{% include image.html
file="UI_phase3.png" alt="Détail des fonctions de l'interface"  %} 

## Vérifications et actions

Le système de reconnaissance optique a identifié des éléments
 pour lesquels l'interprétation est incertaine ou semble incohérente. Ce sont ces éléments principalement que vous devez considérer pour proposer une correction. 
 Il se peut que l'erreur vienne en fait d'un élément placé dans l'environnement proche, et il vous est donc permis de les modifier également. Une fois la correction effectué, l'élément passe en vert : il vous est possible d'annuler cette édition grâce à la liste à droite. Vous
avez également la possibilité de laisser un commentaire si la correction s'avère impossible à effectuer.
