# Erreurs de vérité terrain repérées dans le dataset

Liste des erreurs à corriger dans le dossier ground_truth, directement dans les fichiers MEI.
Mettre la mention *corrigé* une fois la corresction faite.

## C006_0

- mesure 5 : erreur de placement du "âme" sous le si *corrigé*
- mesure 12 : erreur de placement du "etouffe"  *corrigé*
- mesure 35 : on a 2 inserted rest : ils ne sont pas sur l'image d'origine ! *corrigé*
- mesure 34 : idem pour le inserted rest. *corrigé*


## R171_0

- mesures 22 et suivantes : les notes n'ont pas été bien placées dans la VT, il manque un silence invisible en début de mesure.  *corrigé* 

## C009_0
- mesures 1,2,3,4 : ce sont des mesures sur une portée invisible => doivent-elles contenir des silences ? *pb de conversion XML MEI*


## C013_0
- Mesure 7 : pas possible de coder à l'identique les accords à cheval sur 2 portées

## C024_0
- Le fichier semble incorrect. Je mets la version dont je disposais (AL) *corrigé*

## C035_0
- Des problèmes de répartitions de notes sur les voix


## C141_0
- La conversion XML -> MEI perd la position des notes sur la bonne portée, et ça nous coute cher !!

## C455_0
- Dans l'image, la clé de sol n'est pas octaviée. Il semble donc raisonnable d'attendre une clé non octaviée dans la VT, même si c'est une voix de tenor ! Mais difficile à corriger car cela a un impact sur toutes les notes qui ont été encodées un octave trop bas.*corrigé*