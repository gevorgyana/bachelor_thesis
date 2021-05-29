Task one: inference of ASCII-base number system,
positional with two fixed symbols.

English alphabet, pretrained Facebook model as per here: https://github.com/flashlight/flashlight/blob/master/flashlight/app/asr/tutorial/notebooks/InferenceAndAlignmentCTC.ipynb;

0. Install Flashlight and build it.
1. Download models from Flashlight.
2. Run inference with Flashlight (using its inference binaries).
3. You are done! Now you can take input from a file and turn it into text output with precise key strokes.
4. After that, you can use the routine using some external process, say a Python wrapper in the above tutorial.
So the whole pipeline is wrapped into a routine that can be called. Great.

Task two: 
1. Write Emacs Lisp code that is calling the routine.
It should be constantly watching for changes in a file and applying them.
Whenever it sees a file change, it means that the file is ready for execution. Literate execution.
Use reflexion mechanisms built into the language.

2. Then use the M-X interface to execute commands literally. You will get something similar to reflexion in
Python using eval(). Always type in literate commands. For demonstration purposes, show how LSP (Language
server protocol) can be made use of.