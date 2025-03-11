from surmount.base_class import Strategy, TargetAllocation
from surmount.data import Asset

class TradingStrategy(Strategy):
    def __init__(self):
        # Define beta component
        self.beta_asset = Asset('SPY')  # SPY ETF as a proxy for S&P 500
        # Define alpha components
        self.alpha_assets = [
            Asset('MarketNeutral_HedgeFund'),
            Asset('ManagedFutures_Fund'),
            Asset('GlobalMacro_Fund')
        ]
        # Set initial allocations
        self.beta_allocation = 0.0  # Minimal capital for futures
        self.alpha_allocation = 1.0 / len(self.alpha_assets)

    @property
    def interval(self):
        return '1day'

    @property
    def assets(self):
        return [self.beta_asset.symbol] + [asset.symbol for asset in self.alpha_assets]

    def run(self, data):
        # Maintain beta exposure
        allocation = {self.beta_asset.symbol: self.beta_allocation}
        # Allocate equally among alpha strategies
        for asset in self.alpha_assets:
            allocation[asset.symbol] = self.alpha_allocation
        return TargetAllocation(allocation)