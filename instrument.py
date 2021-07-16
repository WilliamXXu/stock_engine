class Instrument():

	def __init__(self,sym,quan,cost,currency,division,zhongwen=0):

		
		self.sym=sym
		self.currency=currency
		self.division=division
		self.quan=quan
		self.cost=cost
		self.value=self.fetch(sym)
		self.zhongwen=zhongwen

	def fetch(self,ticker):
		import yfinance as yf
		import math
		x=yf.download(tickers=ticker,period='10m',interval='1m')
		ind=0
		while ind<=9: 
			ind+=1
			y=x.iloc[-ind,:]
			y=float(y['Close'])
			if not math.isnan(y):
				return y
		raise ValueError('Yahoo Finance error')

	def conv(self,tar_currency):
		pair=self.currency+tar_currency+'=X'
		return self.value*self.fetch(pair)


class Portofolio():
	