import yfinance as yf
import time
import json

# Define a function to get the P/E ratio (PER) of a company
def get_pe_ratio(ticker):
    stock = yf.Ticker(ticker)
    pe_ratio = stock.info.get('trailingPE', 'N/A')
    return pe_ratio

# Define a function to capture the P/E ratios of the companies passed in the tickers parameter
def capture_pe_ratios(tickers):
    # Get the P/E ratio for each company
    pe_ratios = {ticker: get_pe_ratio(ticker) for ticker in tickers}
    
    # Convert the P/E ratios dictionary to a JSON string
    pe_ratios_json = json.dumps(pe_ratios)
    
    # Return the P/E ratios in JSON format
    return pe_ratios_json


def get_falling_stocks(tickers):
    import yfinance as yf
    falling_stocks = []
    
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="5d", auto_adjust=False, back_adjust=False, prepost=True)
            if hist.empty:
                print(f"No price data found for ticker '{ticker}' (period=5d)")
                continue  # paso si no hay datos
            
            if len(hist) < 5:
                continue  # paso si son menos de 5 dias de datos
            
            # Check if the stock has been falling for the last 4 days
            falling = all(hist['Close'].iloc[i] > hist['Close'].iloc[i + 1] for i in range(4))
            
            if falling:
                falling_stocks.append(ticker)
        except Exception as e:
            print(f"Failed to get ticker '{ticker}' reason: {e}")
            
    if len(falling_stocks) > 0:
        return falling_stocks
    else:
        return "No hay acciones que hayan caído por los últimos 5 días"

msft = yf.Ticker("MSFT")

aapl = yf.Ticker("APPL")

googl = yf.Ticker("GOOGL")

# - cash flow statement
#print(msft.cashflow)

# - balance sheet
#print(msft.balance_sheet)

# show analysts data
""" print(msft.analyst_price_targets)
print(msft.earnings_estimate)
print(msft.revenue_estimate)
print(msft.earnings_history) """
#print(msft.eps_trend)
""" print(msft.eps_revisions)
print(msft.growth_estimates)  """

spy = yf.Ticker('SPY')
data = spy.info

# show fund description
#print(data.description)

# show operational information
print(data.fund_overview)
data.fund_operations

# show holdings related information
data.asset_classes
data.top_holdings
data.equity_holdings
data.bond_holdings
data.bond_ratings
data.sector_weightings