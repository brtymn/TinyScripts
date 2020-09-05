import matplotlib.pyplot as plt

## This part reads data from the file.
f=open("datafile","r")

lines=f.readlines()

l1=[]
l2=[]

## Append the read objects to separate lists.
for x in lines:
    l1.append(x.split(' ')[0])
    l2.append(x.split(' ')[1])

f.close()

## This part treats the first column of data as the x-axis and the second column as the y-axis.
x_axis_str = [i.replace('\n','') for i in l1] 
y_axis_str = [i.replace('\n','') for i in l2]

## The "readlines()" function reads objects as strings. Convert the strings to floats.
x_axis = [float(number1) for number1 in x_axis_str]
y_axis = [float(number2) for number2 in y_axis_str]

## This part initializes the plot.
plt.plot(x_axis, y_axis)

plt.xlabel('First Cloumn') 
plt.ylabel('Second Cloumn')

plt.show()
