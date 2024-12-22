from datetime import date
import pandas as pd
import numpy as np


economic_indicators_to_be_removed = ['Real interest rate (%)', 'Deposit interest rate (%)', 'Lending interest rate (%)',
                                     'Interest rate spread (lending rate minus deposit rate, %)', 'Fossil fuel energy consumption (% of total)']

economic_indicators_2024 = {
    'Ghana': {
        "Inflation, consumer prices (annual %)": 19.53,
        'Official exchange rate (LCU per US$, period average)': 15.05,
        'Average precipitation in depth (mm per year)': 1187,
        'Unemployment rate': 4
    },
    "Cote d'Ivoire": {
        "Inflation, consumer prices (annual %)": 3.8,
        'Official exchange rate (LCU per US$, period average)': 600.395,
        'Average precipitation in depth (mm per year)': 1348,
        'Unemployment rate': 2.60
    },
    "Kenya": {
        "Inflation, consumer prices (annual %)": 4.3,
        'Official exchange rate (LCU per US$, period average)': 128.250,
        'Average precipitation in depth (mm per year)': 630,
        'Unemployment rate': 5.7
    }
}

def remove_economic_indicators(economic_indicators):
    economic_indicators_to_be_included = list(set(economic_indicators['Indicator'].unique()) - set(economic_indicators_to_be_removed))
    economic_indicators = economic_indicators[economic_indicators['Indicator'].isin(economic_indicators_to_be_included)]
    return economic_indicators

def add_2024_economic_indicators(economic_indicators):
    economic_indicators['YR2024'] = np.zeros(economic_indicators.shape[0])
    for country, info in economic_indicators_2024.items():
        for indicator, data in info.items():
            economic_indicators.loc[(economic_indicators['Country'] == country) & (economic_indicators['Indicator'] == indicator), 'YR2024'] = data
    return economic_indicators

def add_economic_indicators_row(row, economic_indicators):
    country = row.country_id
    disbursement_date = date.fromisoformat(row.disbursement_date)

    economic_indicators_dict = {f'{indicator}': economic_indicators.loc[(economic_indicators['Country'] == country) & (economic_indicators['Indicator'] == indicator), 'YR'+str(disbursement_date.year)].item()
                                for indicator in economic_indicators['Indicator'].unique()}
    return economic_indicators_dict


def add_economic_indicators(df, economic_indcators):
    new_df_list = []
    for row in df.itertuples():
        new_df_list.append(add_economic_indicators_row(row, economic_indcators))
    return pd.DataFrame(new_df_list)