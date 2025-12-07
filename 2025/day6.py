import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time
from dataclasses import dataclass
from functools import reduce
from operator import add, mul
from itertools import zip_longest, groupby

#Set day/year global variables
DAY:int = 6 #datetime.now().day
YEAR:int = 2025 #datetime.now().year

@dataclass
class CephMath:
    full      :list = None
    operations:list = None
    problems  :list = None
    def load_data(self, dataset:list, part:int):
        self.operations = dataset[-1]
        if part == 1:
            self.operations = self.operations.split()
            self.problems = [list(map(int, x.split())) for x in dataset[:-1]]
        elif part == 2:
            self.operations = self.operations.split()
            self.full = "\n".join(dataset[:-1])
            self.problems = ["".join(x) for x in zip_longest(*self.full.split("\n"), fillvalue=" ")]
            for idx, prob in enumerate(self.problems):
                if prob.isspace():
                    continue
                else:
                    self.problems[idx] = int(prob)
            self.problems = [list(g) for k, g in groupby(self.problems, key=lambda x: isinstance(x,str)) if not k]

    def do_maths(self, part:int) -> list:
        results, maths = [], 0
        for idx, operation in enumerate(self.operations):
            if part == 1:
                maths = [self.problems[x][idx] for x in range(len(self.problems))]
            else:
                maths = self.problems[idx]
            match operation:
                case "*":
                    results.append(reduce(mul, maths))
                case "+":
                    results.append(reduce(add, maths))
        return results

def problem_solver(dataset:list, part:int)->int:
    ceph = CephMath()
    if part == 1:
        ceph.load_data(dataset, part)
        problems = ceph.do_maths(part)
        return sum(problems)
   
    elif part == 2:
        ceph.load_data(dataset, part)
        problems = ceph.do_maths(part)
        return sum(problems)

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow call J.... G.... WENTWORTH. 
    support._877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1, False, -1, strip=True)
    console.log(f"{tellstory}")
    logger.info("testdata table")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problem_solver(testdata, 1)
    #Assert testcase
    assert testcase == 4277556, f"Test case A failed returned:{testcase}"
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
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2, False, -2, strip=False)
    console.log(f"{tellstory}")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problem_solver(testdata, 2)
    #Assert testcase
    assert testcase == 3263827, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problem_solver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR, strip=False)
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
# ehh really easy?
########################################################
#Part B Notes
# I guess just a flattened list of the combined ranges.  Which also seems too easy.  huh
# there it is!  MemoryError.  Need a better way to turn the range into a list.  I can't 
# store all these huge numbers...  
# Well first too i'm seeing I need to merge the ranges. s
# Not sure how to do that. 
    
#New game plan. 
#Range Merge 
#Alright.  soooo I think ... I need to do an startpoint check for the overlap. 
#3-5 -> 10-14 -> 16-20 -> 12-18 