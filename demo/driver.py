import subprocess
import re

cp = subprocess.run(['clang', '-fsyntax-only', '-Xclang', '-ast-dump', 'main.cpp'], capture_output=True)

chunks = str(cp.stdout.decode('utf-8')).split('\n')

result = "(defun highlight()(interactive)"

for i in chunks:
    if str.__contains__(i, "CXXRecordDecl") and str.__contains__(i, "definition"):#i.contains("CXXRecordDecl"):
        S = re.search("<.*>", i)
        [from_, to_] = re.search(":.*:.*,[^\>]*", i).group().split(',')
        from_ = from_[1:]
        from_line = re.search("[^:]*", from_).group()
        from_col = from_[len(from_line) + 1:]
        print (from_line, from_col)
        
        # find positions for ELisp expression
        offset_in_chars = 0

        f = open('main.cpp', 'r')
        lines = f.readlines()
        for (idx, line) in enumerate(lines):
            print (idx, line)
            if idx + 1 == from_line:
                break
            else:
                offset_in_chars += len(line)

        # print('offset {}'.format(offset_in_chars))
        result += '(overlay-put (make-overlay 7 41) \'face \'highlight)(overlay-put (make-overlay 50 65) \'face \'highlight)'
        
        # result += '(overlay-put (make-overlay 1 2) \'face \'highlight)'.format(int(offset_in_chars) + int(from_col))
        
result += ')'

with open('decoded', 'w') as f:
    f.write(result)
