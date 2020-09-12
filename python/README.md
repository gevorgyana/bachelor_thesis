This is a Python solution. It is divided into:

- processing wav files to obtain a transcript of them

- processing the transcript to obtain a program, valid in Python

Curretnly experimenting with this dataset, which should be inflated inside
of data/ directory to reproduce the behaviour of the scripts.

# To recognize speech, we need the words that are in the alphabet of the
# language. We donwload a sample dataset from here:
# download.tensorflow.org/data/speech_commands_v0.01.tar.gz
# and inflate it into the data/ directory.
# This dataset contains simple words like 'cat', 'dog', etc., spoken by
# native speakers. We can construct a grammar from this simple set of
# words that would correspond to the grammar of Python, for example, or
# its small subset.


# define the grammar for the simple language, this language will recognize
# arithmetic expressions. We only have the following words in our
# alphabet:

# digits:
# zero one two three four five six seven eight nine
# other(animals):
# cat dog bird
# control commands
# off/on, up/down, stop/go, yes/no, left, right
# everything else is discarded
# EOF = 'stop'

# Say first we have only expressions of this form:
# G = A | A + A
# A is [0-9]+

# The first subtask is to recognize the operand. Then build a small
# parser to do something smart with these operands.

'''
create 10 models, each of them wil be trying to predict words of type
'zero', 'one', 'two', .., 'nine' - sequences of them!

then run each model on the same input the following matrix
x_0 = [(t011, t012), (t021, t022), ... ],
x_1 = [(t111, t112), (t121, t122), ... ],
...,
x_9 = [(t911, t912), (t921, t922), ... ],

then merge each of the cells and obtain a final vector y:
y = ((t, class), (t, class), (t, class))
'''