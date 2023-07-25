import pandas as pd


def getExpectedReturn(df, price_col_name, annualised=True, annualise_method='sophisticated'):
    """
    Returns the expected return of a security given price data.
    """

    # Calculate returns of prices
    returns = df[price_col_name].pct_change(1)

    # Calculate the expected return using the mean method
    expected_return_daily = returns.mean()

    if annualised:
        if annualise_method == 'sophisticated':
            expected_return_annual = ((1 + expected_return_daily) ** 250) - 1
        elif annualise_method == 'crude':
            # Crude method
            expected_return_annual = expected_return_daily * 250

        return expected_return_annual

    else:
        return expected_return_daily