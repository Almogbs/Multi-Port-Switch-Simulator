import unittest
import os

test_cases = [
    # inputs, outputs
    ("1000 1 2 0.1 0.9 200 2 10 20 180", "180010 15050 164960 19507 4915 14592 1000.15 0.0389 0.009"),
    ("10000 2 2 0.5 0.5 0.5 0.5 3 3 1000000000000 1000000000000 4 4", "59884 29723 30161 0 0 0 10003.06 0.98 0.25"),
    ("10000 2 2 0.5 0.5 0.5 0.5 3 3 3 3 4 4", "53775 27034 26741 6128 3028 3100 10000.48 0.53 0.25"),
    ("10000 2 2 0.5 0.5 0.5 0.5 10 10 1 1 100 100", "198521 98849 99672 1815 907 908 9999.96 0.01 0.01"),
    ("10000 2 2 0.5 0.5 0.5 0.5 10 10 100 100 100 100", "199336 99758 99578 0 0 0 9999.94 0.01 0.01"),
    ("10000 2 2 0.5 0.5 0.5 0.5 10 10 100000 100000 100 100", "199792 100045 99747 0 0 0 10000.04 0.01 0.01"),
]

OUTPUT_PERCENT_ERR = 7

def get_err_msg(input: str, output: str, expected: str, errs: list) -> str:
    """
    Return the error message
    """
    out = output.split()
    exp = expected.split()

    ret = f"\nInput: {input}\n"
    ret += "Output: "
    for i in range(len(out)):
        if i in errs:
            ret += f" >{out[i]}< "
        else:
            ret += f"  {out[i]}  "
    ret += "\nExpect: "
    for i in range(len(exp)):
        if i in errs:
            ret += f" >{exp[i]}< "
        else:
            ret += f"  {exp[i]}  "

    return ret


def check_output(output: str, expected: str, percent_err: float) -> int:
    """
    Compare the output and the expected output
    """
    output = output.split()
    expected = expected.split()
    errs = []
    for i in range(len(output)):
        if abs(float(output[i]) - float(expected[i])) > (percent_err / 100) * float(expected[i]):
            errs.append(i)
    return errs


def simulate(input: str) -> str:
    """
    run simulator.py with the input
    """
    os.system(f"./simulator {input} > output.txt")
    with open("output.txt", "r") as f:
        return f.read().strip()

class Test(unittest.TestCase):
    def test_simulate(self):
        for i, (input, excepted) in enumerate(test_cases):
            with self.subTest(test=i):
                print(f"TEST{i + 1}...")
                output = simulate(input)
                errs = check_output(output, excepted, OUTPUT_PERCENT_ERR)                   
                self.assertEqual(errs, [],  get_err_msg(input, output, excepted, errs))

            
unittest.main(argv=[''], verbosity=2, exit=False)
