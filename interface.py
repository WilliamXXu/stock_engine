from engine import Engine
#换手率 波动率 做t rank by   division  level  我草泥马

cur_dict={'US':'USD','UK':'GBP','HK':'HKD','CN':'CNY','EU':'EUR','CH':'CHF'}


a=Engine()

while True:
	i=input('---------------------------------\nHow can I serve you, Commander?\n 0. view portofolio (updated price) \n 1. open a new position \n 2. deal with an existing position \n 3. Save changes 4.retrieve temporary data\n---------------------------------\n')

	if i=='0':
		a.update()
		repr(a)
		print('')

		from datetime import datetime
		now = datetime.now()
		input('updated at '+now.strftime("%d/%m/%Y %H:%M:%S")+'\nPress Enter to continue\n')

	if i=='1':
		division=input('Which market? (CN,US,UK,HK,EU,CH....)\n')
		currency=input('Which currency? (USD,GBP,HKD...) Press Enter if can be inferred\n')
		if not len(currency):
			currency=cur_dict[division]
		alis=input('Alis for this instrument?Press Enter if none\n')


	if i=='1' or i=='2':
		symbol=input('Instrument symbol? Google Finance format (eg. 000001:SHE)\n')
		quantity=input('How many shares you buy/sell?\n')
		cost=input('For how much you buy/sell it?\n')
		fee=input('Estimate the commission please\n')

	if i=='1':
		a.trade(symbol,quantity,cost,fee,currency,division,alis)
	if i=='2':
		a.trade(symbol,quantity,cost,fee)

	if i=='3':
		a.save()
	if i=='4':
		import os
		os.remove('data.pickle')
		os.rename('data_temp.pickle','data.pickle')
		a=Engine()



