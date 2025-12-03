import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time
from itertools import combinations
import numpy as np

#Set day/year global variables
DAY:int = 3 #datetime.now().day
YEAR:int = 2025 #datetime.now().year

def calc_joltages(banks:list, length:int)->list:
    res = []
    for row in banks:
        combo_nation = ("".join(pair) for pair in combinations(row, length))
        mapped = list(map(int, combo_nation))
        topj = np.argmax(mapped)
        res.append(mapped[topj])
    return res

def calc_big(banks:list, length:int)->list:
    results = []
    for row in banks:
        start_id = 0
        remaining = length
        temp = []
        for _ in range(length):
            end_id = len(row) - (remaining - 1)
            search = row[start_id:end_id]
            max_d = max(search)
            temp.append(max_d)
            rel_idx = search.index(max_d)
            start_id += rel_idx + 1
            remaining -= 1
        results.append("".join(temp))
    return list(map(int, results))

def problem_solver(dataset:list, part:int)->int:
    if part == 1:
        res = calc_joltages(dataset, 2)
    elif part == 2:
        res = calc_big(dataset, 12)
    return sum(res)

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
    testcase = problem_solver(testdata, 1)
    #Assert testcase
    assert testcase == 357, f"Test case A failed returned:{testcase}"
    logger.info(f"Test case passed for part A")
    #Solve puzzle with full dataset
    answerA = problem_solver(data, 1)
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
    testcase = problem_solver(testdata, 2)
    #Assert testcase
    assert testcase == 3121910778619, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problem_solver(data, 2)
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
#Here we have "banks" of batteries (each row) which we want to turn on and find the largest joltage possible.  
#Joltages are calculated by turning on two individual "digits" and multiplying htem.  We can't rearrange them either
#Ad up each rows joltage for the final joltage.  The key here seems to be that its not hte highest two "individual"
#numbers added together.  Its the highest possible combination of the two.  Hello itertools!
########################################################
#Part B Notes
#Well In usual Eric fashion he hits us with a memory error when trying to use combinations at the larger
#battery bank level.  Maaaaybe use hashmap?  Memoization?  Nahhh.  Lets create a slide window to move
#down the line. 
