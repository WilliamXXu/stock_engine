from engine import Engine
a=Engine()

trans={':LON':'.L',':HKG':'.HK',':BME':'.MC',':NYSE':'',':OTCMKTS':'',':ETR':'.DE'}
for x in a.stocks.keys():
	for y in trans.keys():
		if y in x:
			n=x.replace(y,trans[y])
			a.stocks[x].sym=n
			a.stocks[n]=a.stocks[x]
			del a.stocks[x]

a.save()