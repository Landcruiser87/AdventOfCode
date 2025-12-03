import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time

#Set day/year global variables
DAY:int = 2 #datetime.now().day
YEAR:int = 2025 #datetime.now().year

def checkSplit(row:str):
    start, stop = row.split("-")
    invalidIDs = []
    baseRange = range(int(start), int(stop) + 1)
    for i in baseRange:
        stri = str(i)
        length = len(stri)
        midpoint = length // 2
        if stri[:midpoint] == stri[midpoint:]:
            invalidIDs.append(i)
            # logger.info(f"res found {i}")
        
    return invalidIDs

def checkRepeats(row:str):
    start, stop = row.split("-")
    invalidIDs = set()
    baseRange = range(int(start), int(stop) + 1)
    for rng in baseRange:
        strRng = str(rng)
        if strRng[0] == "0":
            continue
        if strRng in (strRng + strRng)[1:-1]:
            invalidIDs.add(strRng)            
            # logger.info(f"res {strRng}")

    return list(map(int, invalidIDs))

def invalid(data:list, part:int):
    invalids = []
    for row in data:
        if part == 1:
            repeats = checkSplit(row)
        elif part == 2:
            repeats = checkRepeats(row)        
        invalids.extend(repeats)

    return invalids

def problemSolver(dataset:list, part:int, test:bool=False)->int:
    #Test data comes in a little wierd
    if test:
        data = "".join(dataset).split(",")
    else:
        data = dataset[0].split(",")
    #Count the number of times the safe dial hits zero!
    invalids = invalid(data, part)
    return sum(invalids)

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow call J.... G.... WENTWORTH. 
    support._877_cache_now() 
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1, False, -1)
    console.log(f"{tellstory}")
    logger.info("testdata table")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemSolver(testdata, 1, True)
    #Assert testcase
    assert testcase == 1227775554, f"Test case A failed returned:{testcase}"
    logger.info(f"Test case passed for part A")
    #Solve puzzle with full dataset
    answerA = problemSolver(data, 1)
    return answerA

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    support._877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2, False, -1)
    console.log(f"{tellstory}")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemSolver(testdata, 2, True)
    #Assert testcase
    assert testcase == 4174379265, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problemSolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)
    # Solve part A
    resultA = part_A()
    fails = []
    if resultA in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultA}")
        exit()
    else:
        logger.info(f"part A possible solution: \n{resultA}\n")
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    resultB = part_B()
    fails = []
    if resultB in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultB}")
        exit()
    else:
        logger.info(f"part B possible solution: \n{resultB}\n")
    # support.submit_answer(DAY, YEAR, 2, resultB)

    #Recurse lines of code
    LOC = linecount(f'./{YEAR}/day{DAY}.py')
    logger.info(f"Lines of code: {LOC}")

    #Delete the cache after submission
    support._877_cache_now(".cache", True)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
# Main thing here is to count any number in a range that repeats itself.  This can be multiple length numbers depending on how huge the input gets.  
# Which knowing Eric, will probably be massive. 