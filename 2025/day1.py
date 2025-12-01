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
    dRange:list[int] = range(0, 100)

    def rotate(self, instruction:str):
        turn = instruction[0]
        amount = int(instruction.strip()[1:])
        start = self.dial
        match turn:
            case "L":
                self.dial -= amount
            case "R":
                self.dial += amount 

        while self.dial not in self.dRange:
            if self.dial > 99:
                self.dial -= 100
            elif self.dial < 0:
                self.dial += 100
            else:
                break
            crossed = self.crossCheck(start, amount, turn)
            if crossed:
                self.zeroCross += 1

        if self.dial == 0:
            self.zeroStop += 1
        # logger.info(f"current: {self.dial}")

    def crossCheck(self, start:int, amount:int, turn:str):
        if self.dial == 0:
            return False
        if turn == "L":
            if (start - amount) not in self.dRange:
                self.zeroCross += 1
                return True
        elif turn == "R":
            if (start + amount) not in self.dRange:
                self.zeroCross += 1
                return True
            
        return False
        # self.dial += self.dial // 100 - (self.dial - amount) // 100
        # self.dial += (self.dial - amount) // 100 - self.dial // 100

def problemSolver(dataset:list, part:int)->int:
    #Count the number of times the safe dial hits zero!
    if part == 1:
        safe = SafeCracker(instructions=dataset)
        for turn in safe.instructions:
            safe.rotate(turn)
        return safe.zeroStop
    
    if part == 2:
        safe = SafeCracker(instructions=dataset)
        for turn in safe.instructions:
            safe.rotate(turn)
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
    support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    resultB = part_B()
    fails = [2408, 5126, 5239]
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
    # support._877_cache_now(".cache", True)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
