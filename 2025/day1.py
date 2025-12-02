import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time
from dataclasses import dataclass

#Set day/year global variables
DAY:int = 1 #datetime.now().day
YEAR:int = 2025 #datetime.now().year

@dataclass
class SafeCracker():
    dial:int = 50
    zeroStop:int = 0
    zeroCross:int = 0
    instructions:str = None
    def rotate(self):
        for instruction in self.instructions:
            turn = instruction[0]
            amount = int(instruction.strip()[1:])
            match turn:
                case "L":
                    direction = -1
                case "R":
                    direction = 1
            #Crank it up~!
            for x in range(amount):
                self.dial = (self.dial + direction) % 100
                #Crossing zero conditions
                #need to catch the edge case where it both stops on zero and crosses zero on the last click
                if (self.dial == 0) & (x != (amount - 1)): # & (x != 0)
                    self.zeroCross += 1
            
            # Zero Stop condition
            if self.dial == 0:
                self.zeroStop += 1
            # logger.info(f"current: {self.dial}")

        # Tried just calculating how many total rotations, but 
        # Kept getting edge case errors on part B 
            # toZero = self.dial or 100
            # toZero = 100 - self.dial
        # self.dial = (self.dial + direction * amount) % 100
        # if amount > toZero:
        #     self.zeroCross += (amount - toZero) // 100 + 1
            
def problemSolver(dataset:list, part:int)->int:
    #Count the number of times the safe dial hits zero!
    if part == 1:
        safe = SafeCracker(instructions=dataset)
        safe.rotate()
        return safe.zeroStop
    
    if part == 2:
        safe = SafeCracker(instructions=dataset)
        safe.rotate() 
    return safe.zeroStop + safe.zeroCross
    
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
    assert testcase == 6, f"Test case B failed returned:{testcase}"
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
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    resultB = part_B()
    fails = [2408, 5126, 5239, 5328, 6586]
    if resultB in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultB}")
        exit()
    else:
        logger.info(f"part B possible solution: \n{resultB}\n")
    support.submit_answer(DAY, YEAR, 2, resultB)

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
