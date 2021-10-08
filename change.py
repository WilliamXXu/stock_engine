from engine import Engine
a=Engine()

trans={':LON':'.L',':HKG':'.HK',':BME':'.MC',':NYSE':'',':OTCMKTS':'',':ETR':'.DE'}
b=Engine()
for x in a.stocks.keys():
	for y in trans.keys():
		if y in x:
			n=x.replace(y,trans[y])
			b.stocks[x].sym=n
			b.stocks[n]=b.stocks[x]
			del b.stocks[x]

b.save()