import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time
from dataclasses import dataclass
from collections import deque, defaultdict

#Set day/year global variables
DAY:int = 10 #datetime.now().day
YEAR:int = 2020 #datetime.now().year

@dataclass
class TwoChainz():
    data:list = None
    max_jolts:int = None
    def chain_of_fools(self) -> int:
        one_jolts, three_jolts = 0, 0
        pairs = deque(self.data.copy())
        while len(pairs) > 1:
            resistor = pairs.popleft()
            min_dist = min(pairs)
            if min_dist - resistor == 1:
                one_jolts += 1
            elif min_dist - resistor == 3:
                three_jolts += 1
        #The last threejolt diff will always be 3 due to the adapter
        three_jolts += 1
        return one_jolts * three_jolts
    
    def path_finder(self) -> int:
        counts = defaultdict(int, {0: 1})
        for ada in self.data[1:]:
            counts[ada] = counts[ada - 3] + counts[ada - 2] + counts[ada - 1]

        return counts[self.data[-1]]
    
def problem_solver(dataset:list, part:int)->int:
    data = sorted(list(map(int, dataset)))
    data.insert(0, 0) #Add the wall charger
    chainz = TwoChainz(data=data)
    chainz.max_jolts = max(data) + 3

    if part == 1:
        total = chainz.chain_of_fools()
        return total
    
    if part == 2:
        total = chainz.path_finder()
        return total

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow call J.... G.... WENTWORTH. 
    support._877_cache_now() 
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1, False, -3)
    console.log(f"{tellstory}")
    logger.info("testdata table")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problem_solver(testdata, 1)
    #Assert testcase
    assert testcase == 220, f"Test case A failed returned:{testcase}"
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
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2, False, -3)
    console.log(f"{tellstory}")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problem_solver(testdata, 2)
    #Assert testcase
    assert testcase == 19208, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problem_solver(data, 2)
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
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    resultB = part_B()
    fails = [252]
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
