import re
from typing import Callable
from decimal import *

def generator_numbers(text: str):
    patern = r"\d+\.\d+"
    for el in re.findall(patern, text):
        yield Decimal(el)
        
     
def sum_profit(text: str, func: Callable):
    return Decimal(sum(func(text))).quantize(Decimal("0.00"))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,\
доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
