from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

app = FastAPI()


class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")
    price: float = Field(description="The price of the Trade.")
    quantity: int = Field(description="The amount of units traded.")


class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")
    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")
    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")
    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")
    trade_date_time: datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")
    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")
    trade_id: Optional[str] = Field(alias="tradeId", default=None, description="The unique ID of the trade")
    trader: str = Field(description="The name of the Trader")


# Mocked database
trades_db = []


@app.get("/trades", response_model=List[Trade])
def get_trades(
    search: Optional[str] = Query(None, description="Search query string"),
    asset_class: Optional[str] = Query(None, description="Asset class of the trade"),
    start: Optional[datetime] = Query(None, description="Minimum date for tradeDateTime field"),
    end: Optional[datetime] = Query(None, description="Maximum date for tradeDateTime field"),
    min_price: Optional[float] = Query(None, description="Minimum value for tradeDetails.price field"),
    max_price: Optional[float] = Query(None, description="Maximum value for tradeDetails.price field"),
    trade_type: Optional[str] = Query(None, description="BUY or SELL trade type"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Number of trades per page"),
    sort: Optional[str] = Query(None, description="Field to sort by")
) -> List[Trade]:
    filtered_trades = trades_db

    if search:
        filtered_trades = [trade for trade in filtered_trades if search.lower() in str(trade).lower()]

    if asset_class:
        filtered_trades = [trade for trade in filtered_trades if trade.asset_class == asset_class]

    if start:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_date_time >= start]

    if end:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_date_time <= end]

    if min_price:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.price >= min_price]

    if max_price:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.price <= max_price]

    if trade_type:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.buySellIndicator == trade_type]

    # Sorting
    if sort:
        reverse = False
        if sort.startswith("-"):
            reverse = True
            sort = sort[1:]
        filtered_trades = sorted(filtered_trades, key=lambda trade: getattr(trade, sort), reverse=reverse)

    # Pagination
    start_index = (page - 1) * limit
    end_index = start_index + limit
    paginated_trades = filtered_trades[start_index:end_index]

    return paginated_trades
