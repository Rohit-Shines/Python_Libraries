import pandas as pd

# defines which version of pandas it is
print(pd.__version__) # 1.4.4

# Listing out data in csv order
list1={'cars':["honda","toyota","suzuki"],'models':[2,3,4]}
print(pd.DataFrame(list1))

###########  Series is like a column in a table #################
a = ["apple", 7, 2]; print(pd.Series(a))

##### Labels ######
print(pd.Series(a)[0]) # a -># this will give output by inserting similar like index values


### Creating index values ###
myvar = pd.DataFrame(list1,index=["a","b","c"])
print(myvar)

###calling the data with index number ####
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar["x"])


##### Making vertical to horizontal data with specific row ####
data = { "calories": [420, 380, 390], "duration": [50, 40, 45]}
a=pd.DataFrame(data); print(a)
print(a.loc[0])
