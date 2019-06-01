# ftr_classifier
This is a natural language classifier, which uses key-word methods to classify future-referring sentences in terms of whether they utilize the present tense, future tense, or express epistemic modality.


### installation
`pip install ftr-classifier` 

### usage
`from ftr_classifier import ftr`

`ftr` has three main functions, `prepare()`, `process()` and `apply_dominance()`. They are designed to take a `pandas` dataframe with column containing text data in `str` format, and another column contained information about the languages of the text data, currently limited to either `english`, `dutch`, or `german`. The default column names are `response` for the column containing natural language strings, and `textLang` for the column indexing language. But these can be altered according to the users data by passing key word arguments to either `prepare` or `score`. Natural langauge responses should have been generated using the experimental methods described in `Robertson et al (TKTK)`.  Finally, `process_dataframe()` calls `prepare`, `process` and `apply_dominance` in sequence and returns a dataframe scoared according to the descriptions in `Robertson et al (TKTK)`.

