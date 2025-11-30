import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time
from itertools import combinations
from collections import deque

#Set day/year global variables
DAY:int = 9 #datetime.now().day
YEAR:int = 2020 #datetime.now().year

def checkSums(window:list, target:int):
    sums = 0
    que = deque(combinations(window, 2))
    while que:
        x, y = que.popleft()
        if x + y == target:
            sums += 1

    if sums != 0:
        return True
    else:
        return False

def decode(data:list, preamble:int):
    idx = preamble
    post = data[preamble:]
    for row in post:
        if checkSums(data[idx - preamble:idx], row):
            idx += 1
        else:
            return row

def problemSolver(dataset:list, part:int, preamble:int)->int:
    data = list(map(int, dataset))
    if part == 1:
        first = decode(data, preamble)
        return first
    if part == 2:
        pass

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
    testcase = problemSolver(testdata, 1, 5)
    #Assert testcase
    assert testcase == 127, f"Test case A failed returned:{testcase}"
    logger.info(f"Test case passed for part A")
    #Solve puzzle with full dataset
    answerA = problemSolver(data, 1, 25)
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
    testcase = problemSolver(testdata, 2)
    #Assert testcase
    assert testcase == 8, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problemSolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)
    # Solve part A
    resultA = part_A()
    fails = [38]
    if resultA in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultA}")
        exit()
    else:
        logger.info(f"part A possible solution: \n{resultA}\n")
    support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    # resultB = part_B()
    # fails = [252]
    # if resultB in fails:
    #     logger.warning(f"Answer already submitted\nAnswer: {resultB}")
    #     exit()
    # else:
    #     logger.info(f"part B possible solution: \n{resultB}\n")
    # support.submit_answer(DAY, YEAR, 2, resultB)

    #Recurse lines of code
    LOC = linecount(f'./{YEAR}/day{DAY}.py')
    logger.info(f"Lines of code: {LOC}")

    #Delete the cache after submission
    # support._877_cache_now(".cache", True)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
