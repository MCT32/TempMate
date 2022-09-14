import argparse
import pathlib
import os

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--target-dir", type=pathlib.Path, default=pathlib.Path().absolute(), help="The directory to be copied to.")
parser.add_argument("-s", "--source-dir", type=pathlib.Path, default=pathlib.Path(__file__).parent.absolute().joinpath("templates"), help="The directory containing the templates.")
parser.add_argument("template")

args = vars(parser.parse_args())

template = args["template"]
target_dir = args["target_dir"]
source_dir = args["source_dir"]

paths = {}

for (dir, subdir, file) in os.walk(str(source_dir)):
    names = dir.split(",")
    
    for name in names:
        paths[name] = dir

assert paths[template], "Directory not found"

path = source_dir.joinpath(paths[template])

if os.name == "nt":
    os.system("copy \"" + str(path) + "\" \"" + str(target_dir) + "\"")
elif os.name == "posix":
    os.system("cp \"" + str(path) + "\" \"" + str(target_dir) + "\"")
else:
    print("OS not currently supported.")