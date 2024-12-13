def main():
    GIRL_FILE_NAME = "GirlNames.txt"
    BOY_FILE_NAME = "BoyNames.txt"
    GIRLS_NAMES_LIST = READ_GIRL_NAME_LIST(GIRL_FILE_NAME)
    BOYS_NAME_LIST = READ_BOY_NAME_LIST(BOY_FILE_NAME)
    ALL_NAMES_LIST = GIRLS_NAMES_LIST + BOYS_NAME_LIST
    INPUT_SEARCH = GET_SEARCH_NAMES()
    FOUND_NAMES = SEARCH_NAME_LIST(INPUT_SEARCH, ALL_NAMES_LIST)
    DISPLAY_RESULTS(INPUT_SEARCH, FOUND_NAMES)
def READ_GIRL_NAME_LIST(FILE_NAME):
    GIRLS_NAMES_FILE = open(FILE_NAME, "r")
    GIRL_NAMES_LIST = []
    GIRL_NAME = GIRLS_NAMES_FILE.readline()
    while GIRL_NAME != "":
        GIRL_NAME = GIRL_NAME.rstrip("\n")
        GIRL_NAMES_LIST.append(GIRL_NAME)
        GIRL_NAME = GIRLS_NAMES_FILE.readline()
    return GIRL_NAMES_LIST

def READ_BOY_NAME_LIST(FILE_NAME):
    BOYS_NAMES_FILE = open(FILE_NAME, "r")
    BOYS_NAMES_LIST = []
    BOY_NAME = BOYS_NAMES_FILE.readline()
    while BOY_NAME != "":
        BOY_NAME = BOY_NAME.rstrip("\n")
        BOYS_NAMES_LIST.append(BOY_NAME)
        BOY_NAME = BOYS_NAMES_FILE.readline()
    return BOYS_NAMES_LIST
def GET_SEARCH_NAMES():
    SEARCH_NAME = input(" Enter first name to search: ")
    INPUT_SEARCH = []
    while SEARCH_NAME != "end-now":
        INPUT_SEARCH.append(SEARCH_NAME)
        SEARCH_NAME = input("Enter next name or 'end-now' to see results: ")
    print()
    return INPUT_SEARCH
def SEARCH_NAME_LIST(INPUT_SEARCH, ALL_NAMES_LIST):
    FOUND_NAMES = []
    for INPUT_SEARCH in range(len(INPUT_SEARCH)):
        if INPUT_SEARCH[INPUT_SEARCH] in ALL_NAMES_LIST:
            FOUND_NAMES.append(INPUT_SEARCH[INPUT_SEARCH])
        return FOUND_NAMES
def DISPLAY_RESULTS(INPUT_SEARCH, FOUND_NAMES):
    for INPUT_SEARCH in range(len(INPUT_SEARCH)):
        if INPUT_SEARCH[INPUT_SEARCH] in FOUND_NAMES:
            print(INPUT_SEARCH[INPUT_SEARCH],\
                  "name is apart of the list")
        else:
            print(INPUT_SEARCH[INPUT_SEARCH],\
                  "name is not apart of the list")
main()
