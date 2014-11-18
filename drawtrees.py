import nltk
import sys
for line in sys.stdin:
    line = line.strip()
    tree = nltk.Tree(line)
    tree.draw()
