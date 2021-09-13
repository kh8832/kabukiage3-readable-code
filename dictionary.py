import argparse

parser = argparse.ArgumentParser(description='このプログラムの説明')
parser.add_argument('--fn', default=None, help='file name')
parser.parse_args()


# 仕様1
def spec1():
    print("上手")

# 仕様3
def spec3(fn):
    f = open(fn, "r", encoding="utf-8")
    data = f.readline()
    print(data)
    f.close()


if __name__ == "__main__":
    args = parser.parse_args()
    fn = args.fn
    
    if fn is None:
        spec1()
    else:
        spec3(fn)