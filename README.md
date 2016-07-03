
# Gensim word2vec training example

Example of how to learn vector presentation of words in python using `Gensim`
on english wikipedia articles.

# Requirements
* Python 3.5 + pip
* Gensim 0.12.4

# Setup

Run following commands (estimated 10 hours)

```
./setup.sh
```

The shell script `setup.sh` will do the following
* Install required python libraries using `pip`
* Download the compressed [english wikipedia articles dump](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2)
and put them into `data/enwiki-latest-pages-articles.xml.bz2`
* Train the word2vec model using the `train.py` script.

This can ofc. also just be done manually.

# Results

Running the `test.py` script shows a few examples of the results of the
obtained word representation.

```
King - man + woman:

"queen"       - similarity: 0.678644
"princess"    - similarity: 0.587378
"monarch"     - similarity: 0.528285
"prince"      - similarity: 0.520583
"throne"      - similarity: 0.488901
"empress"     - similarity: 0.482006
"emperor"     - similarity: 0.461451
"regnant"     - similarity: 0.45579
"isabeau"     - similarity: 0.455715
"berengaria"  - similarity: 0.455293
```

```
Similarity between man and woman:
0.707675308594
```
