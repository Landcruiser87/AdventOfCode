import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from utils import support
from utils.loc import linecount
from dataclasses import dataclass
from collections import deque
from utils.support import logger, console, log_time

#Set day/year global variables
DAY:int = 5 #datetime.now().day
YEAR:int = 2020 #datetime.now().year

@dataclass
class Seat():
    input     :str   = ""
    seatId    :int   = None
    seatRow   :int   = None
    seatCol   :int   = None
    totalCols :range = range(0, 8)
    totalSeats:range = range(0, 128)
    def decode(self):
        directions = deque(self.input)
        while directions:
            direct = directions.popleft()
            match direct:
                case "B":
                    self.totalSeats = self.range_divide(1, self.totalSeats)
                case "F":
                    self.totalSeats = self.range_divide(-1, self.totalSeats)
                case "L":
                    self.totalCols = self.range_divide(-1, self.totalCols)
                case "R":
                    self.totalCols = self.range_divide(1, self.totalCols)
        self.seatId = self.seatRow * 8 + self.seatCol

    def range_divide(self, highlow:int, rangeOb:range):
        midpoint = len(rangeOb) // 2
        if highlow == -1:
            if (len(self.totalSeats) == 2) & (self.seatRow == None):
                self.seatRow = rangeOb.start
                return self.totalSeats
            elif (len(self.totalCols) == 2) & (self.seatCol == None):
                self.seatCol = rangeOb.start
                return self.totalCols
            else:
                return range(rangeOb.start, rangeOb[midpoint])
        elif highlow == 1:
            if (len(self.totalSeats) == 2) & (self.seatRow == None):
                self.seatRow = rangeOb.stop - 1
                return self.totalSeats
            elif (len(self.totalCols) == 2) & (self.seatCol == None):
                self.seatCol = rangeOb.stop - 1
                return self.totalCols
            else:
               return range(rangeOb[midpoint], rangeOb.stop)
        else:
            raise ValueError("I think you broke it hoser")
        
def problemSolver(dataset:list, part:int)->int:
    seatIds = []
    for seat in dataset:
        ticket = Seat(seat)
        ticket.decode()
        seatIds.append(ticket.seatId)
    if part == 1:
        return max(seatIds)
    elif part == 2:
        for i in seatIds:
            if i + 1 not in seatIds:
                return i + 1

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow call J.... G.... WENTWORTH. 
    support._877_cache_now() 
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1, False, "li")
    testdata = "FBFBBFFRLR\nBFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL".splitlines()
    console.log(f"{tellstory}")
    logger.info("testdata table")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemSolver(testdata, 1)
    #Assert testcase
    assert testcase == 820, f"Test case A failed returned:{testcase}"
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
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2, False, "li")
    testdata = "FBFBBFFRLR\nBFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL".splitlines()
    console.log(f"{tellstory}")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemSolver(testdata, 1) #No second test case here so reusing the first
    #Assert testcase
    assert testcase == 820, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problemSolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)
    # Solve part A
    resultA = part_A()
    fails = [887]
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
