#coding: utf-8

'''
provide prepare_valus for years

for exampe, given year=2024, radius(context)=2
will retrun a list: [2022,2023,2024,2025,2026]
'''

from datetime import date

def get_thisyear() -> int:
    ''' get this year '''
    return date.today().year

def get_year_color(yy: int, target_year: int) -> str:
    ''' return the color from the input year '''
    this_year = get_thisyear()
    ret_color = "white"
    if yy == this_year:
        if yy == target_year:
            ret_color = "red"
        else:
            ret_color = "green"
    elif yy==target_year:
        ret_color = "yellow"
    return ret_color

def prepare_values(year: int, after: int=0, before: int=0, radius: int=0) -> list[int]:
    ''' prepare values '''
    year = year if year is not None else get_thisyear()
    after = after if after is not None else 0
    before = before if before is not None else 0
    radius = radius if radius is not None else 0
    if after<0 or before<0 or radius<0:
        raise ValueError("value MUST be greater than 0")
    if radius!=0:
        if after!=0 or before!=0:
            print(f"CONFLICT: context({radius}) vs after({after})/before({before})")
            print("The value of context will override after and/or before")
        after, before = radius, radius
    upper = year + after
    lower = year - before
    if lower>upper:
        lower,upper = upper,lower
    vals = []
    for y in range(lower,upper+1):
        vals.append(y)
    return vals

if __name__ == "__main__":
    print("provides functions only")
    print("DO NOT run this script...")
