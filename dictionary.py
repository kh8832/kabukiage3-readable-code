import argparse

parser = argparse.ArgumentParser(description='このプログラムの説明')
parser.add_argument('--fn', default=None, help='file name')
parser.parse_args()


def readwords(fn):
    
    f = open(fn, "r", encoding="utf-8")
    wordlist = f.readlines()
    for word in wordlist:
        word = word.rstrip('\n')
        print (word)

    f.close()


if __name__ == "__main__":
    args = parser.parse_args()
    fn = args.fn
    
    readwords(fn)