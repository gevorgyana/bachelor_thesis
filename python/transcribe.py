import librosa

# to recognize speech, we need the words that are in the alphabet of the
# language. We donwload a sample dataset from here:
# download.tensorflow.org/data/speech_commands_v0.01.tar.gz
# and inflate it into the data/ directory.
# This dataset simple words like 'cat', 'dog', etc., spoken by native
# speakers. We can construct a grammar from this simple set of words
# that would correspond to the grammar of Python, for example, or its
# small subset.
