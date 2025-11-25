import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from utils.time_run import log_time
from utils.loc import linecount
from utils.support import logger, console
from utils import support
from itertools import combinations
from collections import deque

#Set day/year global variables
DAY:int = 1 #datetime.now().day
YEAR:int = 2020 #datetime.now().year

def data_load(filen:str)->list:
	with open(f'{DAY}{filen}.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [x.strip() if x != "" else "" for x in data]
	return arr

def problemsolver(data:list, part:int)->int:
    if part == 1:
        combos = deque(list(combinations(data, 2)))
        while combos:
            idx1, idx2 = combos.popleft()
            if int(idx1) + int(idx2) == 2020:
                return int(idx1) * int(idx2)
    elif part == 2:
        combos = deque(list(combinations(data, 3)))
        while combos:
            idx1, idx2, idx3 = combos.popleft()
            if int(idx1) + int(idx2) + int(idx3) == 2020:
                return int(idx1) * int(idx2) * int(idx3)

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow call J.... G.... WENTWORTH. 
    support._877_cache_now() 
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1)
    console.log(f"{tellstory}")
    logger.info("testdata table")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemsolver(testdata, 1)
    #Assert testcase
    assert testcase == 514579, f"Test case A failed returned:{testcase}"
    logger.info(f"Test case passed for part A")
    #Solve puzzle with full dataset
    answerA = problemsolver(data, 1)
    return answerA

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    support._877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2)
    console.log(f"{tellstory}")
    # [logger.info(row) for row in testdata]
    
    #Solve puzzle w/testcase
    testcase = problemsolver(testdata, 2)
    #Assert testcase
    assert testcase == 241861950, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problemsolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)
    #Solve part A
    resultA = part_A()
    fails = [8400518384267]
    if resultA in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultA}")
        exit()
    else:
        logger.info(f"part A possible solution: \n{resultA}\n")
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    resultB = part_B()
    fails = [8400518384267]
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
