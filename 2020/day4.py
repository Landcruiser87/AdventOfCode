import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
import numpy as np
from itertools import groupby
from utils import support
from utils.loc import linecount
from dataclasses import dataclass
from utils.support import logger, console, log_time

#Set day/year global variables
DAY:int = 4 #datetime.now().day
YEAR:int = 2020 #datetime.now().year

PASS_DICT = {
    "byr" : "(Birth Year)",
    "iyr" : "(Issue Year)",
    "eyr" : "(Expiration Year)",
    "hgt" : "(Height)",
    "hcl" : "(Hair Color)",
    "ecl" : "(Eye Color)",
    "pid" : "(Passport ID)",
    "cid" : "(Country ID)",
}

def problemsolver(dataset:list, part:int)->int:
    datal = groupby(dataset, key=lambda x:x == "")
    data = [list(group) for is_empty, group in datal if not is_empty]
    for group in data:
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
    testcase = problemsolver(testdata, 1)
    #Assert testcase
    assert testcase == 2, f"Test case A failed returned:{testcase}"
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
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2, False, -3)
    console.log(f"{tellstory}")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemsolver(testdata, 2)
    #Assert testcase
    assert testcase == 336, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problemsolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)
    #Stack the data horizontally 100 times.
    # data =  [row * 100 for row in data]
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
