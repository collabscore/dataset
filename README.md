# The CollabScore dataset for Optical Music Recognition evaluation 

This repository contains the reference dataset produced by the [CollabScore](https://collabscore.cnam.fr) project to test and evaluate Optical Music Recognition. It combines a set of images of music scores, all accessible and transformable through an IIIF server, the corresponding list of score encodings in MEI, and a few useful tools to set up a testing environment dedicated to Optical Music Recognition systems.

## Dataset 

The dataset  consists of 26 scores by Camille Saint-Saëns, totaling 199 pages,
covering the main genres practiced by the composer 
with the exception of operas. For each score, the dataset provides 
  - images of the original edition, taken from the Gallica digital library ;
  - a reference encoding in MEI format, 
  - a set of annotations linking  images and regions in images, to the corresponding notation
    fragment in the reference score.

Images are actually supplied as references to the [Gallica](https:/gallica.bnf.fr) digital library, embedded in IIIF manifests. The 
``iiif.py`` script lets extract useful contents. Reference scores can be found in the ``ground_truth`` folder. 

It is assumed that the OMR predicted files will be put in the ``predicted``folder.
For the sake of illustration, the ``predicted`` folder is initially fed with  the results
of the CollabScore OMR system. This lets you begin directly testing the comparison utility. Eventually,
you must replace the content of ``predicted`` with your own predicted scores. Be careful to respect 
the score file naming, as the comparison assume identical names in, respectively, ``predicted`` 
and ``ground_truth`` folders. 

## Viewing the content

We provide a tiny Node.js site which shows the list of scores and allows to display images (using the Mirador IIIF viewer)
or MEI files (using the Verovio viewer). You just need to install Node.js and run the commands.

```bash
npm install
npm start
```

This shoud start a Node.js server of http://127.0.0.1:8080. The main page shows a list of the
the scores, each associated to the respective link for images, refrence score and predicted score.

<img width="1141" height="867" alt="ListOpus" src="https://github.com/user-attachments/assets/9b8d8314-384b-4ee5-b4c8-eec4e8e6f38f" />

## Running an evaluation

We mostly rely on [MusicDiff](https://github.com/gregchapman-dev/musicdiff), a Python
package which compares the predicted scores with the reference ones (ground truth). 
The reference scores are stored  in a directory ``ground_truth``, in MEI format,
and predicted scores  obtained by the tested OMR  must be placed in a parallel directory, with a consistent
naming. Note that is not necessary for the scores to be in MEI format. 

### The compare.py script

The dataset comes with a ``compare.py`` script which can be use tu run comparisons between predicted and ground truth, either at
an individual or global level.

It is recommended to set up virtual Python 3.12+ environment and to install the required packages with ``pip install - requirements.txt``.  The script
is fully documented in the [documentation](https://collabscore.github.io/dataset).

### Single score comparison

The predicted score in folder ``predicted``must have the exact same filename as the reference score in ``ground_truth``. 
The script must be run with the ``-a single`` option, and take as input the name of the file(s) to compare. Example
for file ``C006_0.mei``.

```bash
python3 compare.py -a single -s C006_0
```

Results will be found in the ``results``folder:
  - ``C006_0_predicted_diff.pdf``, differences found in the predicted file
  - ``C006_0_ground_diff.pdf``, differences found in the reference file
  - detailed list of operations in ``C006_0_report.json``

### Mass comparison

Evaluating a set of predicted scores  consists essentially in running the 
mass comparison measurements already implemented in MusicDiff. 

## Documentation 

For details, please refere to the [documentation](https://collabscore.github.io/dataset).

## Licence

The dataset is made available under a [Creative Commons Attribution Non-Commercial Share-Alike 4.0 (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0) license.

## Citing

If you use this work in any research, please cite the relevant paper:

```
@inproceedings{rigauxEtAl26,
  title={The collabscore Dataset. Towards Robust and Generalized OMR Evaluation},
  author={Rigaux, Philippe and Coüasnon, Bertrand and  Guillotel-Nothmann, Christophe and  Guilloux, Fabien and Lemaitre, Aurélie},
  booktitle={XXX},
  pages={XXX},
  year={2026}
}
```


To cite MusicDiff, please refer to the following paper:

```
@inproceedings{foscarin2019diff,
  title={A diff procedure for music score files},
  author={Foscarin, Francesco and Jacquemard, Florent and Fournier-S’niehotta, Raphael},
  booktitle={6th International Conference on Digital Libraries for Musicology},
  pages={58--64},
  year={2019}
}
```
