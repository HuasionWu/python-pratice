import pandas as pd

b = ['小华', '小吴', '小陈']
c = ['18岁', '19岁', '20岁']
d = ['18cm', '17cm', '16cm']

df = pd.DataFrame({'你是谁' : b, '你几岁' : c, '你多高' : d})
df.to_csv("xsb.csv", index=False, sep=',')