from instrument import Instrument
import pickle
#换手率 做t

a=Instrument('K',100,20,'USD','UK','家乐氏')
print(type(a))
with open('data.pickle','wb') as f:
	pickle.dump(a,f,pickle.HIGHEST_PROTOCOL)

with open('data.pickle','rb') as g:
	t=pickle.load(g)

print(t.sym)
print(t.value)
print(t.zhongwen)
