#!/usr/bin/env python3
#

'''
LOOP

use a quick/rough way to estimate how many years you need
if wannt to go double insterest

year \\approx 72 / insterest

for example, i = 5% one year iteration
72/5 = 14.4
about 14 year we could double the base
'''

import argparse

from basic_common import do_nothing, get_prt

prt = do_nothing


class CompoundInterestCalculator:
    """Calculate compound interest scenarios."""

    def __init__(self, rate: float, limit: float = 2.0):
        """Initialize calculator with rate and target limit.

        Args:
            rate: Interest rate as decimal (e.g., 0.05 for 5%)
            limit: Target multiple to reach (default: 2.0 for doubling)
        """
        assert rate > 0.0, "Rate must be positive"
        assert rate < 1.0, "Rate must be less than 100%"
        self.rate = rate
        self.limit = limit

    def simple_lump_sum_growth(self, show_first_n: int = 0, show_last_n: int = 1) -> int:
        """Calculate years for single investment to reach target via compound interest.

        Starts with $500, displays selected years, stops when reaching $1000 (2x).

        Args:
            show_first_n: Number of first years to display (default: 3)
            show_last_n: Number of last years to display (default: 2)

        Returns:
            Number of years needed
        """
        initial = 500
        target = 1000
        value = initial
        years = 0
        year_values = []  # Store (year, value) pairs

        prt(f'simple_lump_sum: Starting with ${initial:.2f}, target: ${target:.2f} (2x), rate: {self.rate*100:.2f}%')

        year_values.append((0, value))

        while value < target:
            years += 1
            value *= 1 + self.rate
            year_values.append((years, value))

        # Display selected years
        prt(f'Year 0: ${year_values[0][1]:.2f}')

        # Show first N years
        for i in range(1, min(show_first_n + 1, len(year_values))):
            prt(f'Year {year_values[i][0]}: ${year_values[i][1]:.2f}')

        # Show ellipsis if there are hidden years
        if len(year_values) > show_first_n + show_last_n + 1:
            prt('...')

        # Show last N years
        start_idx = max(show_first_n + 1, len(year_values) - show_last_n)
        for i in range(start_idx, len(year_values)):
            prt(f'Year {year_values[i][0]}: ${year_values[i][1]:.2f}')

        prt(f'Reached target in {years} years')
        return years

    def annuity_with_regular_deposits(self, monthly_deposit: float = 1.0) -> int:
        """Calculate months for regular monthly deposits to reach $1000.

        The balance starts at $0. Each month, it earns one month's interest
        and then receives the configured deposit.

        Args:
            monthly_deposit: Amount deposited each month (default: $1.00)

        Returns:
            Number of months needed
        """
        assert monthly_deposit > 0.0, "Monthly deposit must be positive"
        monthly_rate = self.rate / 12
        target = 1000.0
        months = 0
        balance = 0.0

        while balance < target:
            months += 1
            balance *= 1 + monthly_rate
            balance += monthly_deposit

        years = months / 12
        total_input = monthly_deposit * months
        ratio = total_input / balance
        prt(
            f'annuity_deposits: ${monthly_deposit:.2f}/month at '
            f'{self.rate*100:.2f}% annual rate reaches ${balance:.2f} '
            f'in {months} months ({years:.2f} years); '
            f'total input: ${total_input:.2f}; input/balance ratio: {ratio:.4f}x'
        )
        return months


def tryloop(r: float, _limit=2.0):
    ''' tryloop (deprecated - use CompoundInterestCalculator.simple_lump_sum_growth) '''
    calc = CompoundInterestCalculator(r, _limit)
    calc.simple_lump_sum_growth()


def loop2(r: float, _limit: float=2.0, monthly_deposit: float=1.0):
    ''' loop2 (deprecated - use CompoundInterestCalculator.annuity_with_regular_deposits) '''
    calc = CompoundInterestCalculator(r, _limit)
    return calc.annuity_with_regular_deposits(monthly_deposit)



def _run_scenario(
    title: str,
    question: str,
    method: str,
    runner_func,
    start_rate: float = 0.05,
    increment: float = 0.005,
    iterations: int = 5,
    limit: float = 2.0,
    target_description: str = 'Target multiple: 2.0x',
    runner_kwargs: dict | None = None
):
    """Run a compound interest scenario with configurable parameters.

    Args:
        title: Display title for the scenario
        question: Question being answered
        method: Method description
        runner_func: Function to call for each iteration (takes rate and limit)
        start_rate: Starting interest rate (default: 0.05)
        increment: Rate increment per iteration (default: 0.005)
        iterations: Number of iterations (default: 5)
        limit: Target multiple (default: 2.0)
        target_description: Text describing the scenario target
        runner_kwargs: Optional keyword arguments for runner_func
    """
    prt('=' * 70)
    prt(title)
    prt(f'Question: {question}')
    prt(f'Method: {method}')
    prt('=' * 70)
    r = start_rate
    prt(f'Starting rate: {r*100:.2f}%, Increment: {increment*100:.2f}%, {target_description}')
    prt()
    for _ in range(iterations):
        runner_func(r, limit, **(runner_kwargs or {}))
        r += increment
    prt('=' * 70)
    prt()


def main(use_print: bool = False):
    '''main'''
    global prt  # pylint: disable=global-statement
    prt = get_prt(use_print=use_print)

    # Run both scenarios with unified approach
    _run_scenario(
        title='Simple Compound Interest (Single Lump Sum)',
        question='How many years to double a single initial investment?',
        method='Starting with 1.0, compound it until reaching the limit',
        runner_func=tryloop,
        start_rate=0.05,
        increment=0.01,
        iterations=3,
        limit=2.0
    )
    month_input=1.0
    _run_scenario(
        title='Compound Interest with Regular Deposits (Annuity)',
        question=f'How many months for ${month_input} monthly deposits to grow from $0 to $1000?',
        method=f'Add ${month_input} each month and compound the balance monthly',
        runner_func=loop2,
        start_rate=0.05,
        increment=0.01,
        iterations=3,
        limit=2.0,
        target_description='Target balance: $1000.00',
        runner_kwargs={'monthly_deposit': month_input}
    )
    month_input=1.5
    _run_scenario(
        title='Compound Interest with Regular Deposits (Annuity)',
        question=f'How many months for ${month_input} monthly deposits to grow from $0 to $1000?',
        method=f'Add ${month_input} each month and compound the balance monthly',
        runner_func=loop2,
        start_rate=0.05,
        increment=0.01,
        iterations=3,
        limit=2.0,
        target_description='Target balance: $1000.00',
        runner_kwargs={'monthly_deposit': month_input}
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Estimate years needed to double investment')
    parser.add_argument('-p', '--print', action='store_true', help='use stdlib print only (no rich formatting)')
    args = parser.parse_args()

    main(use_print=args.print)
