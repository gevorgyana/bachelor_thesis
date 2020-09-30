### Solution

Build a languge that recognizes arithmetic expressions.

### Dataset

Download a sample dataset from
[here](download.tensorflow.org/data/speech_commands_v0.01.tar.gz)
and inflate it into `data/` directory.

This dataset contains simple words like 'cat', 'dog', etc., spoken by
native speakers. We can construct a grammar from this simple set of
words. The dataset contains more words, but we choose only the following
subset.

Group | Words
:---  | :---
Digits | zero one two three four five six seven eight nine
Animals | cat dog bird
Control commands | off/on, up/down, stop/go, yes/no, left, right

Everything else is discarded.

### Convolutional network
Motivation: table 9.1 in [2] is showing 2 options for processing
audio data:
- audio waveform
- audio that has been processed with FT.

### Grammar

```
EOF = 'stop'
G = A | A + A
A is [0-9]+
```