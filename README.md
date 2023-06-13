# SteelEye
**Trade API Documentation**
This document provides an overview of the Trade API solution built using FastAPI. It explains the implemented endpoints, the data model, and the reasoning behind the approach taken.
Endpoints:

1.**Listing trades**:
•	Endpoint: GET /’trades’
•	Description: This endpoint fetches a list of trades.
•	Query Parameters:
	‘search’: Search query string to filter trades based on specific fields.
	‘asset_class’: Asset class of the trade.
	‘Start’: Minimum date for the tradeDateTime field.
	‘end’: Maximum date for the tradeDateTime field.
	‘min_price’: Minimum value for the tradeDetails.price field.
	‘max_price’: Maximum value for the tradeDetails.price field.
	‘trade_type’: BUY or SELL trade type.
	‘page’: Page number for pagination.
	‘limit’: Number of trades per page for pagination.
	‘sort’: Field to sort the trades by.

Response: A paginated list of trades based on the applied filters and pagination parameters.



2.**Single trade**:
Endpoint: GET /trades/{trade_id}
Description: This endpoint fetches a single trade by its ID.
Path Parameter: 
•	‘trade_id’: ID of the trade.
Response: The details of the requested trade.


3.**Searching trade**s:
Endpoint: GET /trades/search
Description: This endpoint allows users to search for trades using the provided query parameters.
Query Parameters:
	counterparty: Search for trades based on the counterparty field.
	instrumentId: Search for trades based on the instrumentId field.
	instrumentName: Search for trades based on the instrumentName field.
	trader: Search for trades based on the trader field.
Response: A list of trades matching the provided search criteria.

**Data Model**:
The Trade API uses a Pydantic data model to represent a single trade. The Trade model consists of the following fields:
•	asset_class: The asset class of the instrument traded.
•	counterparty: The counterparty the trade was executed with.
•	instrument_id: The ISIN/ID of the instrument traded.
•	instrument_name: The name of the instrument traded.
•	trade_date_time: The date and time the trade was executed.
•	trade_details: The details of the trade, including the buy/sell indicator, price, and quantity.
•	trade_id: The unique ID of the trade.
•	trader: The name of the trader.

**Reasoning and Approach**:

1.**FastAPI and Pydantic**:
•	FastAPI was chosen as the framework for building the Trade API due to its high performance, simplicity, and built-in support for asynchronous operations.
•	Pydantic was used for data validation and modeling the Trade schema. Its integration with FastAPI allows for automatic request and response validation.

2.**Mocked Database**:
•	Since the document mentions the requirement to mock the database, a simple list (trades_db) was used as a placeholder for the database.
•	In a real-world scenario, you would need to replace the mocked database with your actual database implementation (e.g., Elasticsearch).

3.**Filtering**:
•	The get_trades endpoint includes support for advanced filtering using the query parameters specified in the document.
•	Each query parameter is applied as a filter to the trades to narrow down the results.
•	Trades that match the filters are included in the final list of trades returned by the endpoint.

4.**Pagination**:
•	Pagination support was added to the get_trades endpoint to limit the number of trades returned and provide paginated results.
•	The page parameter indicates the desired page number, and the limit parameter controls the number of trades per page.
•	The start and end indices for slicing the list of trades are calculated based on the page and limit values.

5.**Sorting**:
•	The get_trades endpoint includes sorting functionality based on the sort parameter.
•	Trades can be sorted in ascending order by specifying the field name in the sort parameter.
•	To sort in descending order, the field name should be prefixed with a hyphen (e.g., sort=-trade_date_time).

6**Handling**:
•	Error handling and input validation are automatically handled by FastAPI and Pydantic.
•	If any invalid input is provided or any required parameter is missing, FastAPI will return an appropriate error response.

**Summary**:
The Trade API built using FastAPI provides endpoints for listing trades, fetching a single trade by ID, searching trades based on specific fields, and applying advanced filtering, pagination, and sorting. 
It utilizes FastAPI's capabilities, along with Pydantic for data modeling and validation. While a mocked database is used in the example, the code can be easily adapted to integrate with your actual database implementation.
