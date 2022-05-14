from dataclasses import dataclass


@dataclass
class Transaction:
    txn_id: str
    member_id: str
    ticker: str
    #txn_date: datetime.strptime(txn_date, format_data='%Y-%m-&d')
    txn_date: str
    txn_time: str
    txn_type: str
    quantity: float
    percentage_fee: float