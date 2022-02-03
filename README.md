# ftr_classifier
This branch of the `ftr-classifier` is designed to be used on naturally-occuring data, rather than experimental data like the `master` branch. The main difference is that the present tense category does not rely on word lists; it rather simply classes all statements which are not classified as any other category as present tense. 

The other main addiion is the ability to classify text data in terms of not only _how_ but _whether_ test data refer to the future. 

See the `README.md` to the `master` branch for documentation.

To install this branch, first install `spacy 2.2.1`, as for the master branch, then clone this branch with `git clone -b natural_ftr git@github.com:cbjrobertson/ftr_classifier.git`, then `cd ftr_classifier` and install from source with `python setup.py install`. This should install this branch to whichever environment `python` is in, and will give you access to the `ftr.estimate_ftr_ptr` function, which estimates _whether_ an item of text data refers to the future.

NB: running `git clone...` will be slow, the repo takes up approximately 1GB.


