import os
from huepy import *
print(lightgreen("""
                  /////|
                 ///// |
                |~~~|  |
                |===|  |
                |r  |  |
                | n |  |
                |  f| /
                |===|/
                '---'
"""))
# print welcome massag
print(bold(green("      Welcome in rename script  " + red("(♥_♥)"))))
print(green("      ▬▬ι═══════ﺤ    -═══════ι▬▬"))
# back to first path
mycwd = os.getcwd()


def re_name(arg1):
    cont = 1
    os.chdir(arg1)

    # list all dir
    all = os.listdir()
    print(lightgreen(bold(all)))
    q = input(cyan(" Do you want to rename the files ?! >" +
                   red(" (y) or( n ) or (q) to  exit >>  "))).lower()
    try:
        print(0)
   
        if q == "y":
            newname = input(que(orange(" Enter new name > "))).strip()
            ex = ''
            for f in all:
                if os.path.isfile(f):
                    if not ex:
                        ex += input(que(orange("Enter files extension > "))
                                    ).strip(".")
                        os.rename(f, f"{newname}{cont}.{ex}")
                        cont += 1

                    elif ex:
                        os.rename(f, f"{newname}{cont}.{ex}")
                        cont += 1

                elif os.path.isdir(f):
                    os.rename(f, f"{newname}{cont}")
                    cont += 1

            print(good(yellow(" ============> ") +
                       green(" The files were renamed Goodbye " + yellow(" 【ツ】"))))
            pass
    # if no right dir rerun minf fn
        elif q == "n":
            os.chdir(mycwd)
            minf()
        elif q == "q":
            pass
        elif q != "q" or " y " or "n":
            print(yellow(" Enter an error, try again "))
            os.chdir(mycwd)
            minf()
            pass

    except:
           pass


def minf():

    while True:
        # to quit from prog
        pathto = input(que(orange("Enter path to Files to be renamed > ")))
        if pathto == "q":
            break
        # to run re_name fn
        elif os.path.exists(pathto):
            re_name(pathto)
            break
        # to check if path is exists
        elif not os.path.exists(pathto):
            print(info(green("path not exists ! Enter valid path  ") +
                       red("or") + green("   Enter q to exit >  ")))


minf()
