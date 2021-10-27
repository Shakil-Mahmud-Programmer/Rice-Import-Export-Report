import pandas as pd,matplotlib.pyplot as plt
im=pd.read_csv("file/data-import.csv")
ex=pd.read_csv("file/data-export.csv")

plt.style.use('seaborn')
fig,ax=plt.subplots(3)
fig.suptitle("Rice Import & Export Report\nby Shakil Mahmud",color='purple')
fig.tight_layout(pad=3)

ax[0].set_title('Rice Import',color='red',size=10)
ax[0].plot(im['Year'],im['Quantity'],color='red',marker='o',markersize=3,linewidth=0.5,label='Import')
ax[0].set_xlabel('Year',color='red',size=9)
ax[0].set_ylabel('Import (ton)',color='red',size=9)
ax[0].legend(loc='upper left')

ax[1].set_title('Rice Export',color='green',size='10')
ax[1].plot(ex['Year'],ex['Quantity'],color='green',marker='o',markersize=2,linewidth=0.5,label='Export')
ax[1].set_xlabel('Year',color='green',size=9)
ax[1].set_ylabel('Export (ton)',color='green',size=9)
ax[1].legend(loc='upper left')

ax[2].set_title('Import and Export',color='blue',size='10')
ax[2].plot(im['Year'],im['Quantity'],color='red',marker='o',markersize=2,linewidth=0.5,label='Import')
ax[2].plot(ex['Year'],ex['Quantity'],color='green',marker='o',markersize=2,linewidth=0.5,label='Export')
ax[2].set_xlabel('Year',color='blue',size=9)
ax[2].set_ylabel('Import & Export (ton)',color='blue',size=9)
ax[2].legend(loc='upper left')



plt.show()