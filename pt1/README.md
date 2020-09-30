### Solution

Build a languge that recognizes arithmetic expressions.

### Dataset

Download a sample dataset from
[here](download.tensorflow.org/data/speech_commands_v0.01.tar.gz)
and inflate it into `data/` directory.

This dataset contains simple words like 'cat', 'dog', etc., pronounced
by native speakers. We can construct a grammar from this set of
words. The dataset contains more words, but we choose only the following
subset.

Group | Words
:---  | :---
Digits | zero one two three four five six seven eight nine
Animals | cat dog bird
Control commands | off/on, up/down, stop/go, yes/no, left, right

Everything else is discarded.



### Approaches to building a model
Motivation: table 9.1 in [2] is showing 2 options for processing
audio data:
- audio waveform
- audio that has been processed with FT.

Maybe it makes sense to work with a waveform, but it clearly contains
less infomration than MFCCs, so use 2-D MFCCs instead.

The authors of [1] implemented 3 models, let's play with the simplest
one first.
- [x] Implement the simple model.
- [ ] Implement the convolutional networks they had & measure
performance

### Grammar

```
EOF = 'stop'
G = A | A + A | EOF
A = [0-9]+
```