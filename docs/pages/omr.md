---
title: Le système OMR
layout: home
nav_order: 4
permalink: omr.html
---

# La reconnaissance optique des partitions


Le système de reconnaissance de partitions musicales 
(<i>Optical Music Recognition</i> - OMR) du projet CollabScore 
s’appuie sur une combinaison d’Intelligences Artificielles 
à base d’apprentissage profond (*Deep Learning*) et 
de modélisation de la notation musicale. 

Le système analyse l’image de la partition et 
grâce à ses connaissances sur la notation musicale 
est capable de produire une représentation 
complète de la partition reconnue tout en vérifiant 
sa cohérence. Cela permet au système de détecter et  
signaler d’éventuelles erreurs de lecture qui peuvent 
se produire sur des partitions anciennes parfois 
mal imprimées (en rouge ci-dessous), afin que 
les utilisateurs puissent contrôler rapidement 
la partition produite.

## Caractéristiques et problèmes soulevés par l'OMR

La notation musicale encode une information extrêmement
complexe, et s'avère très difficile à interpréter 
correctement par reconnaissance automatique. 
Il existe des systèmes d’OMR commerciaux   intégrés aux logiciels 
d’édition musicale, mais ces solutions donnent des résultats 
jugés peu satisfaisants pour des partitions un tant soit 
peu complexes. Dans beaucoup de cas, le temps passé 
pour la correction des erreurs peut s'avérer plus long 
que l'écriture dela partition à partir de zéro.

CollabScore a développé un système OMR nommé DMOS 
qui s'est attaché à apporter une solution fiable 
à des situations pour lesquelles les systèmes 
actuels sont en échec. En voici un échantillon.</div>

### Identification des parties et voix<


La partition d'une musique polyphonique
contient plusieurs parties instrumentales,
et chaque instrument peut lui-même 
jouer en parallèle plusieurs voix. De 
plus un instrument peut occuper 1, 2 ou
même trois portées. L'identification
des parties et voix est souvent fautive
dans les systèmes existant.</p>		

{% include image.html
file="ex-voix-image.png" alt="Image d'une partition multi-voix"  %} 


DMOS effectue une analyse globale de
la partition pour identifier les parties,
applique des heuristiques pour reconnaître
les portées, et distingue avec précision les voix.
La colorisation des voix et parties en sortie 
permet la vérification de l'analyse effectuée.


{% include image.html
file="ex-voix-score.png" alt="Identification des voix"  %} 

### Voix sur plusieurs portées


Un instrument peut jouer simultanément voix, et une voix
peut s'étendre sur plusieurs portées comme le montre l'exemple
ci-dessous.


{% include image.html
file="ex-multivoice-image.png" alt="Voix sur plusieurs portées"  %} 


La reconnaissance optique doit pouvoir identifier les notes
et silences appartenant à une même voix, et produire
un codage de la partition qui représente fidèlement cette situation
					
					
{% include image.html
file="ex-multivoice-score.png" alt="Après reconnaissance"  %} 

### Liaisons


On trouve deux types liaisons dans
une partition : les liaisons de continuité
d'une même note ou accord, et les
liaisons d'articulation. Ces liaisons peuvent
dépasser les limites des mesures et même des pages.

{% include image.html
file="ex-liaisons-image.png" alt="Image d'une partition avec liaisons"  %} 

DMOS identifie
les différents types de liaison et traite dans la
version actuelle les liaisons de continuité. La reconnaissance
de la structure d'une partition permet la production
des liaisons multi-mesures ou multi-pages.


{% include image.html
file="ex-liaisons-score.png" alt="Après reconnaissance"  %} 

### Reconnaissance du texte


Dans les parties chantées, la notation musicale s'accompagne
d'un découpage syllabique des paroles. La correspondance 
texte-musique peut être complexe: parfois (mélisme) une même syllabe
est chantée sur plusieurs notes, parfois (même si plus rarement) 
c'est l'inverse. La notation musicale utilise un
 codage plus ou moins complexe pour représenter ces situations.

{% include image.html
file="ex-paroles-image.png" alt="Mélodie avec texte"  %} 


DMOS intègre une reconnaissance optique des
caractères qui a été adaptée pour reconstituer 
un texte à partir du codage trouvé dans l'image. 
La reconstitution fiable des textes est importante 
pour pouvoir reproduire la partition correctement
dans différents contextes. 



{% include image.html
file="ex-paroles-score.png" alt="Après reconnaissance"  %} 
