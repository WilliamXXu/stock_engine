'''import yfinance as yf
import time
s=time.clock()
x=yf.download(tickers='K',period='10m',interval='1m')
diff1=time.clock()-s
print(diff1)



s=time.clock()
x=yf.download(tickers='K GIS MRK MKL C AAPL MSFT TSM BTI LMT BAM STAG COLD IYR KT TLK CHT ADM HTHT',period='10m',interval='1m')
diff1=time.clock()-s
print(diff1)
'''
a={1:2,3:4}
for x in a:
	print(x)

print(a.keys())