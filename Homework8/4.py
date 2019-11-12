import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("datasetP4.csv",header=None)
#print(df)

fig,ax=plt.subplots()
ax.scatter(df.iloc[:,0],df.iloc[:,1])

ax.grid(True)
fig.tight_layout()

#plt.show()
plt.savefig("graph.png")