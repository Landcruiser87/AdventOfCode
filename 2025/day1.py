import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time
from dataclasses import dataclass
from itertools import cycle

#Set day/year global variables
DAY:int = 1 #datetime.now().day
YEAR:int = 2025 #datetime.now().year

@dataclass
class SafeCracker():
    zeroC:int = 0
    dial:int = 50
    instructions:str = None
    dRange:list[int] = range(0, 99)
    def rotate(self, instruction:str):
        turn = instruction[0]
        amount = int(instruction[1:])
        if turn == "L":
            self.dial = self.dial - amount
        elif turn == "R":
            self.dial = self.dial + amount
        while True:
            if self.dial > 99:
                self.dial = self.dial - 100
            elif self.dial < 0:
                self.dial = 100 - abs(self.dial)
            if abs(self.dial) < 100:
                break

        if self.dial == 0:
            self.zeroC += 1
        # logger.info(f"current:{self.dial}")

def problemSolver(dataset:list, part:int)->int:
    safe = SafeCracker(instructions=dataset)
    #Count the number of times the safe dial hits zero!
    if part == 1:
        for turn in safe.instructions:
            safe.rotate(turn)
        return safe.zeroC
    
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
    testcase = problemSolver(testdata, 1)
    #Assert testcase
    assert testcase == 3, f"Test case A failed returned:{testcase}"
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
    testcase = problemSolver(testdata, 2)
    #Assert testcase
    assert testcase == 19208, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problemSolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)
    # Solve part A
    resultA = part_A()
    fails = [79]
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
