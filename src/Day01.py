from pathlib import Path
import pandas as pd
import re

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        calibrations = f.read().split('\n')

    first_calibrations = [re.findall('\d', line) for line in calibrations]
    first_calibrations = [int(line[0] + line[-1]) for line in first_calibrations]
    print(f"The result of first star is {sum(first_calibrations)}")

    digits = ['one', '1', 'two', '2', 'three', '3', 'four', '4', 'five', '5', 'six', '6', 'seven', '7', 'eight', '8', 'nine', '9']
    digits_bckw = [s[::-1] for s in digits]
    pattern = '|'.join(digits)
    pattern_bckw = '|'.join(digits_bckw)
    
    second_calibrations = [int(
        str(digits.index(re.search(pattern, line)[0]) // 2 + 1)
        + str(digits_bckw.index(re.search(pattern_bckw, line[::-1])[0]) // 2 + 1)
        ) for line in calibrations]
    print(f"The result of second star is {sum(second_calibrations)}")