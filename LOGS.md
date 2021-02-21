feb14
a very interesting question:
https://stats.stackexchange.com/questions/269008/research-on-heterogeneous-neural-networks

these are related to autoencoders
[1] Learning in the Machine: Recirculation is Random Backpropagation P. Baldi and P. Sadowski August 11, 2018
[2] https://arxiv.org/abs/1904.02619

Learning about backprop (there are questions)
(( to be continued ))

feb15
https://arxiv.org/pdf/1911.11423.pdf

todo: simply refer to the models that are used by Talon:
single headed rnn;
flashlight project (models from FAcebook)

- accoustic model vs language model
- flashlight does not work under windows or on ARM.
- encoder / decoder RNN (see Goodfellow)

Hinton G., https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/38131.pdf, speech recognition, acoustic modeing.

http://www.voxforge.org/home/docs/faq/faq/what-is-an-acoustic-model good explanation

feb20:
- A general note: Speech Recognition and NLP are different things. Both use Deep Learning
these days. But watch this lecture for a better overview of Speech Recognition. Dragon was one of the first models used in the wild.

- https://www.youtube.com/watch?v=RBgfLvAOrss&list=PLPXcFKg4niEmdw2N_ntdRN9rYxHt-kvMc&index=2
[1] https://sci-hub.se/https://ieeexplore.ieee.org/document/1162650 paper on Dragon
Need HMMs to understand these. Reading Goodfellow for that.
Need the prob. theory for that.
[2] Ширяев
[3] Гитхман, Скороход: глава 4.
[4] М.В. КАРТАШОВ. Марковские цепи.
https://math.stackexchange.com/questions/3197490/advantage-of-using-hidden-markov-model-over-markov-chain
suggests the following
[5] https://www.cs.umb.edu/~rvetro/vetroBioComp/HMM/Rabiner1986%20An%20Introduction%20to%20Hidden%20Markov%20Models.pdf

feb21:
+ Read more about Markov models from [5]
+ Read more about HMMs in Speech Recognition from deeplearningbook (it is actually only used in speech recognition among all the applications)
- New resources:
 - https://habr.com/en/company/yandex/blog/198556/
 - How are phonemes|frames|acoustic model|utterances related? https://web.stanford.edu/~jurafsky/goldwater10.pdf, https://cmusphinx.github.io/wiki/tutorialconcepts/ (this appears in search results on multiple occasions)
- Read Hinton's et al. paper that is mentioned as a reference in Deeplearningbook and here https://habr.com/en/company/yandex/blog/198556/ . https://ieeexplore.ieee.org/document/6296526
- . Mohri, M., Pereira, F., & Riley, M. (2008). Speech recognition with weighted finite-state transducers. In Springer Handbook of Speech Processing (pp. 559-584). Springer Berlin Heidelberg.
- (book) Jurafsky D., Martin J.H. (2008) Speech and language processing, 2nd edition. Prentice Hall. Great book, chapter 26 is what I needed. (and 25)

- https://www.cs.toronto.edu/~graves/icml_2006.pdf CTC (we are using ctc, too).
we use encoder-decoder and ctc.
- Kaldi? language models from there?
- https://research.google/pubs/pub32892/
- https://ieeexplore.ieee.org/document/1454428 along with the paper about Dragon

- https://www.youtube.com/watch?v=RBgfLvAOrss&list=PLPXcFKg4niEmdw2N_ntdRN9rYxHt-kvMc&index=2 the video
