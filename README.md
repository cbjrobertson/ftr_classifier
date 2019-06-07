# ftr_classifier
This is a natural language classifier, which uses key-word methods to classify future-referring sentences in terms of whether they utilize the present tense, future tense, or express epistemic modality.


## installation
It is recommended that ftr_classifier be used in a `conda` environment with `python 3.6` installed. Instructions on getting started with `conda` can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Once `conda` is installed, create an appropriate environment, with `conda create --name my_env_name python=3.6` , then activate the environment with `conda activate my_env_name` or `source activate my_env_name`. Then, to install `ftr_classifier` run:

`pip install ftr-classifier` 

## usage
`import ftr_classifier as ftr`

`ftr_classifier` has two main purposes. Firstly, it scores some dataframe  `pandas` dataframe, "`df`", with a column containing text data in `str` format, and another column containing information about the language of the text data, currently limited to  `english`, `dutch`, or `german`, in terms of how sentences in  `df['response']` refer to the future. Seconly, it provides counts of the lemmas/stems of the word lists it uses to classify responses.

The default column names are `response` for the column containing natural language strings, and `textLang` for the column indexing language. But these can be altered according to the user's data by passing key word arguments as in, `ftr.prepare(lang_col='new_textLang_col_name',text_col='new_response_col_name')` or `ftr.score(lang_col='new_textLang_col_name',text_col='new_response_col_name')`. Natural langauge responses should have been generated using the experimental methods described in `Robertson et al (TKTK)`. 


### classification

#### main classification functions
1)  `ftr.prepare()` processes `df['response']` using `spacy` natural language processing models, and returns `df` with `df['spacy_doc']`, the processed version of `df['response']`, and `df['final_sentence']`, which is just a `spacy` document of the last sentence in `df['response']`.
2) `ftr.score()` classifies  `df['final_sentence']` in terms of how it refers to the future (i.e. whether it uses the present tense, future tense, or some kind of expression exhibiting epistemic modal qualifcation). For explanation and justification of this classification scheme as regards English, Dutch, and German, see `Robertson et al. (TKTK)`. 
3) `ftr.apply_dominance()` applies a dominance relationship to the output of `ftr.score()`, as described in `Robertson et al. (TKTK)`. Any analyses on the results of this package should be performed on dominance-subjected results, i.e. the columns ending in `_dom`. If there is no `_dom` column for a particular category, e.g. `verb_poss`, then this category is the dominant category and can be used in analysis.

Finally, `ftr.lassify_df()` calls `ftr.prepare()`, `ftr.score()` and `ftr.apply_dominance()` in sequence and returns a dataframe scoared according to the descriptions in `Robertson et al (TKTK)`. This is the recommended apprach, as given in  the minimal examples.

#### resultant collumns
Calling  `ftr.lassify_df(df)` appends the following columns to `df`. Except for when a language does not have the word category of the column in question, columns are scored as `1` when a given feature is present and `0` when it is not. When a language does not have the word category in question, all values for that feature for that langauge are scored `-999`.

1) `response_clean` a python `list`, of the tokens in the final sentence in the strings in `df['response']`.
2) `present`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['present']` where `lang` == the language in `df['textLang']`, and is in `['english','dutch','german']`, i.e. whether it uses the present tense of the main verb in each response.
3) `future`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['future']` where `lang` == the language in `df['textLang']`, and is in `['english','dutch','german']`, i.e. whether it uses a future tense marker.
4) `verb_poss`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['verb_poss']` where `lang` == the language in `df['textLang']`, and is in `['english','dutch','german']`, i.e. whether the response uses a modal verb indicating uncertainty, e.g. _could_, _might_, or _may_, in English.
5) `verb_cert`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['verb_cert']` where `lang` == the language in `df['textLang']`, and is in `['english','dutch','german']`, i.e. whether the response uses a modal verb indicating certainty, i.e. _must_, in English.
6) `adv_adj_poss`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['adv_adj_poss']` where `lang` == the language in `df['textLang']`, and is in `['english','dutch','german']`, i.e. whether the response uses a modal adverb/adjective indicating uncertainty, e.g. _possibly_, _maybe_, or _probably_, in English.
7) `adv_adj_cert`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['adv_adj_cert']` where `lang` == the language in `df['textLang']`, and is in `['english','dutch','german']`, i.e. whether the response uses a modal adverb/adjective indicating certainty, e.g. _certain_, _definitely_, or _surely_, in English.
8) `mental_poss`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['mental_poss']` where `lang` == the language in `df['textLang']`, and is in `['english','dutch','german']`, i.e. whether the response uses an epistemic mental state predicate indicating uncertainty, e.g. _think_, or _believe_, in English.
9) `mental_cert`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['mental_cert']` where `lang` == the language in `df['textLang']`, and is in `['english','dutch','german']`, i.e. whether the response uses an epistemic mental state predicate indicating certainty, i.e. _know_, in English.
10) `particle_poss`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['particle_poss']` where `lang` == the language in `df['textLang']`, and is in `['dutch','german']`, i.e. whether the response uses an epistemic modal particle indicating uncertainty, i.e. _wel_ in Dutch, or _wohl_ in German (English does not have modal particles, so all `df['textLang'=='english','particle_poss']`  == `-999`, for `missing`).
11) `particle`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['particle']` where `lang` == the language in `df['textLang']`, and is in `['dutch','german']`, i.e. whether the response uses an epistemic modal particle apart from those indicating uncertainty, i.e. _toch_ in Dutch or _doch_ in German (English does not have modal particles, so all `df['textLang'=='english','particle']`  == `-999`, for `missing`).
12) `will_future`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['will_future']` where `lang` == the language in `df['textLang']`, and is in `['english','dutch','german']`, i.e. whether it uses a future tense marker _will_ (English), _zullen_ (Dutch), or _werden_ (German).*
13) `go_future`: indicates whether the reponse uses one of the words in `ftr.WORD_LISTS[lang]['go_future']` where `lang` == the language in `df['textLang']`, and is in `['english','dutch']`, i.e. whether it uses a form of the future tense marker _be going to_ (English), or _gaan_ (Dutch) (German does not have a future tense marker grammaticised from a motion verb, i.e. 'go', so all `df['textLang'=='german','go_future']`  == `-999`, for `missing`).*
14) `negated` a column indicating whether a negation is present in `df['response']`.
15) `present_dom`: indicates whether `df['present'] == 1` and not `df[['future','*_cert','*_poss']] == 1`, i.e. whether a response uses the present tense of the main verb and not also a future tense marker or an epistemic modal expression.
16) `future_dom`: indicates whether `df['future'] == 1` and not `df[['*_cert','*_poss']] == 1`, i.e. whether a response uses the a future tense marker and not also an epistemic modal expression. 
17) `will_future_dom`: indicates whether `df['will_future'] == 1` and not `df[['*_cert','*_poss']] == 1`, i.e. whether a response uses the a non-go-based future tense marker and not also an epistemic modal expression.
18) `will_future_dom`: indicates whether `df['will_future'] == 1` and not `df[['*_cert','*_poss']] == 1`, i.e. whether a response uses a future tense marker not based on 'go', and not also an epistemic modal expression.
19) `go_future_dom`: indicates whether `df['go_future'] == 1` and not `df[['*_cert','*_poss']] == 1`, i.e. whether a response uses a future tense marker based on 'go', and not also an epistemic modal expression. (`-999` for all German responses).
20) `lexi_poss`: `1` if `any` in `df[['adv_adj_poss',particle_poss','mental_poss']] == 1`, else `0`, i.e. whether a response uses an expression indicating epistemic uncertainty, which is not a modal verb.
21) `lexi_cert`: `1` if `any` in `df[['adv_adj_cert',particle_cert','mental_cert']] == 1`, else `0`, i.e. whether a response uses an expression indicating epistemic certainty, which is not a modal verb.

* Note that if either 'go_future' or 'will_future' == 1, then 'future' == 1, i.e. future is the set of morphemes in 'go_future' and 'will_future'.

### lemma counting
Additionally, `ftr_classifier` includes functionality to count word occuances according to the sementically relevant lemmas of the words used to classify sentences. The function for doing this is `ftr.count_lemmas()`. If already created, result of `ftr.prepare()` or `ftr.classify_df()` should be passed to  `ftr.count_lemmas()`, as in `ftr.count_lemmas(df=df_class)`, where `df_class == ftr.prepare(df) OR ftr.classify_df(df)`.  `ftr.count_lemmas()` returns a dataframe containing the following columns:

1) `language` -- the language defined in `df['textLang']`.
2) `feature` -- which classification feature the lemma is defined as being a part of, see above.
3) `lemma` the lemma of the word various inflections/derrivations counted derived from the same root. The custom lemmatizer is actually not strictly a lemmatiser, as words from different word classes (i.e. epistemic modal adverbs and adjectives) are "lemmatised" to the same root. It therefore sometimes behaves more like stemming sometimes, but stems back to the adjectival/nominal form rather than the non-dictionary root. This is an entirely arbitrary decision made for reasons of readability. The reasons for the hibrid lemmatising/stemming approach, is we are interested in `Robertson et al. (TKTK)` in semantic marking of a given root more so than the subtle differneces delineated by derrivations of similar roots. In German, whether the root is marked as either the indicative or subjunctive/konjunktiv II mood  is indicated with  `_IND` and `_SUBJ` appended to the end of the "lemma". 
4) `count` the count of the lemma within each language.
5) `num_responses` the number of responses within the language. This and the next column are included in case researcher wish to normalise counts, in the case they have differing number of responses in different languages.
6) `num_words` the sum of the number of words in df['final_sentence'] for each language.

### cleaning
Finally we provide a function which drops the  `spacy` docs automatically appended to the dataframe when `ftr.prepare()` or `ftr.classify_df()` are called. This is because these are memory intensive and sometimes cause display difficulties in the resultant dataframes in some common IDEs, e.g. `spyder`. Use is `clean_df = ftr.clean_spacy(df_class)`, where `df_class == ftr.prepare(df) OR ftr.classify_df(df)`.

### minimal examples
Minimal example scripts are located in `./minimal_examples/`. There is an `iPython` and base `python` version, which demonstrate the same function calls. Opening `minimal_example.ipynb` by clicking on it in `git` will show the interested reader examples of useage with printed results.
