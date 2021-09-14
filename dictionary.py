import argparse

parser = argparse.ArgumentParser(description="このプログラムの説明")
parser.add_argument("--fn", default=None, help="file name")
parser.add_argument("--id", default=None, help="id name")
parser.parse_args()


def readwords(fn,input_id):
    
    f = open(fn, "r", encoding="utf-8")
    wordlist = f.readlines()
    for id,word in enumerate(wordlist,1):
        if not input_id: 
            word = word.rstrip("\n")
            print(str(id)+":"+word)
        else:
            if id == int(input_id):
                print(str(id)+":"+word)

    f.close()


if __name__ == "__main__":
    args = parser.parse_args()
    fn = args.fn
    input_id = args.id
    
    
    readwords(fn,input_id)