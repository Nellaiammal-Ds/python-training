import matplotlib.pyplot as mat
x=[3,4,5,6,7]
y=[8,6,5,4,2]
mat.xlim(1,10)           #set the limit of the x axis
mat.ylim(1,10)           #set the limit of the y axis
mat.xticks([3,4,5])
mat.yticks([5,6,7])    #to see the output of xlim and ylim comment the xtricts and ytrics code
mat.plot(x,y)
mat.show()