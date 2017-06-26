'''
import httplib
conn = httplib.HTTPConnection("api.coinone.co.kr")
conn.request("HEAD","/orderbook")
res = conn.getresponse()
print res.getbody(res)
print res.status, res.reason
'''
import requests
import json

coins = []
xrp = requests.get("https://api.coinone.co.kr/orderbook?currency=xrp")
btc = requests.get("https://api.coinone.co.kr/orderbook")
eth = requests.get("https://api.coinone.co.kr/orderbook?currency=eth")
etc = requests.get("https://api.coinone.co.kr/orderbook?currency=etc")

coins.append(json.loads(xrp.text))
coins.append(json.loads(btc.text))
coins.append(json.loads(eth.text))
coins.append(json.loads(etc.text))
for c in coins :
	if c is not None :
		timestamp = c['timestamp']
		bid = c['bid']
		ask = c['ask']
		pb = int(bid[0]['price']) * float(bid[0]['qty'])
		pa = int(ask[0]['price']) * float(ask[0]['qty'])

		qty = float(bid[0]['qty']) + float(ask[0]['qty'])

		#print pb
		#print pa
		print (pb + pa)/qty
		print timestamp
		print "_____"

