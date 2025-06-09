TICKER_UNIVERSE = [
    # FAANG + MSFT
    "AAPL", "META", "AMZN", "NFLX", "GOOGL", "MSFT",

    # Dow 30
    "AXP","AAPL","AMGN","BA","CAT","CRM",
    "CSCO","CVX","DIS","DOW","GS","HD",
    "HON","IBM","INTC","JNJ","JPM","KO",
    "MCD","MMM","MRK","MSFT","NKE","PG",
    "TRV","UNH","V","VZ","WBA","WMT","RTX",  # RTX is newer Dow component

    # S&P 500 – Top 10 per sector (approx.)
    # Communication Services
    "T","VZ","CHTR","CMCSA","DIS","TMUS","NFLX","GOOGL","META","CHTR",
    # Consumer Discretionary
    "AMZN","HD","MCD","NKE","SBUX","LOW","TJX","GPC","YUM","BBY",
    # Consumer Staples
    "PG","KO","PEP","WMT","MDLZ","CL","COST","CVS","GIS","KMB",
    # Energy
    "XOM","CVX","COP","EOG","SLB","PSX","MPC","VLO","KMI","OKE",
    # Financials
    "JPM","BAC","WFC","C","GS","MS","AXP","PNC","BK","BLK",
    # Healthcare
    "JNJ","UNH","PFE","MRK","ABBV","TMO","BMY","LLY","DHR","GILD",
    # Industrials
    "HON","UPS","UNP","RTX","CAT","MMM","GE","LMT","FDX","BWA",
    # Information Technology
    "AAPL","MSFT","NVDA","ORCL","IBM","INTC","CSCO","ADBE","CRM","AVGO",
    # Materials
    "LIN","APD","ECL","SHW","MLM","FCX","NEM","PPG","LYB","CF",
    # Real Estate
    "SPG","PLD","AMT","CCI","EQIX","PSA","WELL","AVB","VTR","O",
    # Utilities
    "NEE","DUK","SO","AEP","EXC","D","SRE","ETR","XEL","ES"
]

tickers = ['AAPL', 'META', 'AMZN', 'NFLX', 'GOOGL', 'MSFT', 'AXP', 'AMGN', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 
'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT',
'RTX', 'T', 'CHTR', 'CMCSA', 'TMUS', 'SBUX', 'LOW', 'TJX', 'GPC', 'YUM', 'BBY', 'PEP', 'MDLZ', 'CL', 'COST', 'CVS', 
'GIS', 'KMB', 'XOM', 'COP', 'EOG', 'SLB', 'PSX', 'MPC', 'VLO', 'KMI', 'OKE', 'BAC', 'WFC', 'C', 'MS', 'PNC', 'BK', 'BLK', 
'PFE', 'ABBV', 'TMO', 'BMY', 'LLY', 'DHR', 'GILD', 'UPS', 'UNP', 'GE', 'LMT', 'FDX', 'BWA', 'NVDA', 'ORCL', 'ADBE', 'AVGO', 
'LIN', 'APD', 'ECL', 'SHW', 'MLM', 'FCX', 'NEM', 'PPG', 'LYB', 'CF', 'SPG', 'PLD', 'AMT', 'CCI', 'EQIX', 'PSA', 'WELL', 
'AVB', 'VTR', 'O', 'NEE', 'DUK', 'SO', 'AEP', 'EXC', 'D', 'SRE', 'ETR', 'XEL', 'ES']

print(len(tickers))