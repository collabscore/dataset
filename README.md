# The CollabScore dataset for Optical Music Recognition evaluation 

This repository contains the reference dataset produced by the [CollabScore](https://collabscore.cnam.fr) project to test and evaluate Optical Music Recognition. It combines a set of images of music scores, all accessible and transformable through an IIIF server, the corresponding list of score encodings in MEI, and a few useful tools to set up a testing environment dedicated to Optical Music Recognition systems.

## Dataset 

The dataset  consists of 26 scores by Camille Saint-Saëns, totaling 199 pages,
covering the main genres practiced by the composer 
with the exception of operas. For each score, the dataset provides 
  - images of the original edition, taken from the Gallica digital library, 
  - a reference encoding in MEI format, 
  - a set of annotations linking  images and regions in images, to the corresponding notation
    fragment in the reference score.

## Running an evaluation

We mostly rely on [MusicDiff](https://github.com/gregchapman-dev/musicdiff), a Python
package which compares the predicted scores with the reference ones (ground truth). 
The reference scores are stored  in a directory ``ground_truth``, in MEI format,
and predicted scores  obtained by the tested OMR 
must be placed in a parallel directory, with a consistent
naming. Note that is not necessary for the scores to be
in MEI format. 


### Single score comparison


### Mass comparison

Evaluating a set of predicted scores  consists essentially in running the 
mass comparison measurements already implemented in MusicDiff. 

## Documentation 

For details, please refere to the [documentation](https://collabscore.github.io/dataset).

## Licence

The dataset is made available under a [Creative Commons Attribution Non-Commercial Share-Alike 4.0 (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0) license.

## Citing

