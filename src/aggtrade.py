import logging
from binance_d import SubscriptionClient
from binance_d.constant.test import *
from binance_d.model import *
from binance_d.exception.binanceapiexception import BinanceApiException

from binance_d.base.printobject import *

logger = logging.getLogger("binance-futures")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient()


def callback(data_type: 'SubscribeMessageType', event: 'any'):
    print('callback')
    if data_type == SubscribeMessageType.RESPONSE:
        print("Event ID: ", event)
    elif  data_type == SubscribeMessageType.PAYLOAD:
        PrintBasic.print_obj(event)
        #sub_client.unsubscribe_all()
    else:
        print("Unknown Data:")
    print()


def error(e: 'BinanceApiException'):
    print('error')
    print(e.error_code + e.error_message)

#sub_client.subscribe_symbol_bookticker_event("btcusd_210326", callback, error)
#sub_client.subscribe_book_depth_event("btcusd_210326", 10, callback, error, update_time=UpdateTime.FAST)

print('start')
sub_client.subscribe_aggregate_trade_event("btcusd_210326", callback, error)