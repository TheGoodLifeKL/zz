import sys

for line in sys.stdin:
    print(sys.argv[1] + ":" + line, end="")
