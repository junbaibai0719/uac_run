import subprocess
import sys

if __name__ == "__main__":
    if sys.argv.__len__() > 1:
        p = subprocess.Popen(sys.argv[1], stdout=sys.stdout, stderr=sys.stderr)
        out, err = p.communicate()