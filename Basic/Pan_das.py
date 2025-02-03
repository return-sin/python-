import random
import pandas as pd
random.seed(3)
names = ['John', 'Jane', 'Jack', 'Jill', 'Joe']
ages = [random.randint(20, 35) for i in range(5)]
people = {'names': names, 'ages': ages}
df= pd.DataFrame.from_dict(people)
# print( df["ages"] )
# print( df["ages"][3] )
# print( df.loc[0] )
# print( df.loc[0]["names"] )  
# print( df[2:5] )
# print(df.head(5))
# print(df.tail(3))
headers = df.keys( )
print(headers)
print( df.shape )
print(df.describe( ))
df = df.sort_values("ages")
print(df[ df["ages"] > 21 ])