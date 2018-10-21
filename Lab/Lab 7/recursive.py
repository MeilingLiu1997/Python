import os
import sys



def main():
    path = get_path()
    total = recursive(path)
    print("total file: ", total[0], "py file: ", total[1])




def get_path():
    path = sys.argv[1]
    return path


def add(tuple1, tuple2):
    c = (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
    return c

def recursive(path):
    result = (0,0)
    if os.path.isfile(path):
        basename = os.path.basename(path)
        if basename.startswith('.') == True:
            return (0,0)
        elif basename.endswith('.py') == True:
            return(1,1)
        else:
            return(1,0)
    else:
        files = os.listdir(path)
        for file in files:
            result = add(result,recursive(os.path.join(path,file)))
        return result

main()
