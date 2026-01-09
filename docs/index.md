---
title: "Accueil"
keywords: Page accueil
permalink: index.html
summary: 
---

# Introduction au système collaboratif CollabScore

Ce site est un guide d'utilisation du [système collaboratif
associé au projet CollabScore](https://collabscore.cnam.fr). 
En bref, CollabScore a pour but
d'analyser des images de partitions musicales 
afin d'en produire une version *éditable*, autrement
dit dans un format qui permet la modification du contenu
et son utilisation dans divers contextes. Le format
produit par une analyse CollabScore est soit 
[MusicXML](https://www.musicxml.com/), soit 
[MEI](https://music-encoding.org/). Grâce à CollabScore,
des archives musicales conservées au format image 
peuvent redevenir exploitables avec des fonctionnalités
comme l'écoute synchronisée, l'extraction de parties séparées,
la transposition, etc.  **Pour en savoir plus sur 
les objectifs du projet, vous pouvez 
[consulter la page dédiée]({% link pages/collabscore.md %})**.

## Les données


Toutes les informations sur les œuvres musicales proviennent
d'une blbliothèque numérique, Neuma, 
gérée conjointement par le Conservatoire national des 
arts et métiers et l'IRéMus. Cette bibliothèque,
accessible en ligne à l'adresse 
[https://neuma.huma-num.fr](https://neuma.huma-num.fr), 
fournit notamment:
  - une organisation hiérarchique en collections et sous-collections ;
  - les représentations numériques d'une œuvre sous forme
    de partition dans
    différents formats: image, XML, MIDI, PDF, etc. ;
  - des annotations décrivant ces représentations et les associant ;
  - des services.


{% include image.html
file="neuma.png" alt="Neuma" caption="Aperçu de la bibliothèque numérique Neuma"  %} 

Le système de reconnaissance optique des contenus analyse les
représentations-image dans Neuma, et y insère le format
éditable (XML) obtenu. C'est en interrogeant Neuma
que le système collaboratif propose à ses utilisateurs
d'ajouter des informations de correction et de validation. C'est
aussi dans Neuma que l'on peut accéder au résultat final des processus
CollabScore, à savoir une partition éditable extraite d'une image
et améliorée par les corrections des annotateurs.

En tant qu'utilisateur des interfaces collaboratives, vous n'aurez probablement pas à interagir directement avec Neuma, **mais si vous voulez en savoir plus, vous pouvez 
[consulter la page dédiée]({% link pages/neuma.md %})**.

## La reconnaissance optique, ou OMR

CollabScore produit une partition éditable à partir
d'une image par *reconnaissance optique* des éléments
de la notation musicale, ou OMR pour
*optical music recognition*. Nous avons développé
notre propre système OMR, nommé DMOS. Il analyse l'image de
la partition pour en extraire des objets et reconstituer le contenu,
comme l'illustre l'image ci-dessous.

{% include image.html
file="omr_reco.png" alt="OMR" caption="Illustration du processus de reconnaissance optique"  %} 

Quoique il tente
de produire une reconnaissance la plus précise
possible, le résultat présente et présentera toujours des limites
et produira toujours des erreurs, ou du moins
des incertitudes. La phase de reconnaissance optique est
donc complétée par une phase de validation et de correction
collaborative qui propose à des annotateurs
d'intervenir pour valider ou corriger les
résultat de la reconnaissance OMR.

**Pour en savoir plus sur DMOS, vous pouvez 
[consulter la page dédiée]({% link pages/omr.md %})**.

## Callico, un système de correction collaborative

Quand l'OMR a produit une partition éditable par reconnaissance
optique d'une image, il reste à valider cette reconnaissance
et à la corriger éventuellement. CollabScore propose des
interfaces pour que les utilisateurs puissent accéder aux documents
analysés,  comparer l'image initiale et la partition éditable, et 
indiquer les corrections à effectuer. L'image ci-dessous montre
une de ces interfaces, avec la mise en vis-à-vis de l'image (à
gauche) et de son interprétation (à droite). 

{% include image.html
file="collab-phase2.png" alt="Interfaces collaboratives"  caption="Une des interfaces collaboratives" %} 

L'essentiel de la présente documentation est consacré à ces
interfaces collaboratives. Elles constituent un système collaboratif
que nous avons construit sur la base de [Callico]{https://teklia.com/our-solutions/callico/}, une plate-forme
logicielle distribuée par la société Teklia. Nous avons
avons largement adapté Callico aux spécificités de la 
musique notée. 

## Comment lire ce guide

Ce guide est destiné aussi bien aux administrateurs 
qui créent et 
gèrent des campagnes d'annotation qu'aux annotateurs 
qui accèdent à  des documents pour les annoter. 

 - les administrateurs [peuvent accéder à cette section du site]({% link pages/admin.md %});
 
 - les annotateurs [peuvent accéder à cette section du site]({% link pages/annotateur.md %}).

Il est recommandé de prendre connaissance de la documentation avant
de se lancer dans des corrections et validation. La compréhension
des principes généraux, et l'organisation de chaque interface en 
particulier, ne peuvent que faciliter la prise en main de nos outils.
Nous avons cherché à les rendre aussi  simples que possible,  mais
ils s'appuient sur des notions et des connaissances loin 
d'être triviales, à commencer par la notation musicale elle-même.
Bonne lecture !