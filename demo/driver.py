import subprocess
import re

cp = subprocess.run(['clang', '-fsyntax-only', '-Xclang', '-ast-dump', 'main.cpp'], capture_output=True)

chunks = str(cp.stdout.decode('utf-8')).split('\n')

for i in chunks:
    if str.__contains__(i, "CXXRecordDecl") and str.__contains__(i, "definition"):#i.contains("CXXRecordDecl"):
        S = re.search("<.*>", i)
        [from_, to_] = re.search(":.*:.*,[^\>]*", i).group().split(',')
        from_ = from_[1:]
        from_line = re.search("[^:]*", from_).group()
        from_col = from_[len(from_line) + 1:]
        print (from_line, from_col)
        # Emacs Lisp command
        #print ()
