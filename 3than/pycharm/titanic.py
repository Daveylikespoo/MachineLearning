import tflearn
import numpy as np

from tflearn.datasets import titanic
titanic.download_dataset('titanic_datasets.csv')

from tflearn.data_utils import load_csv
data, labels = load_csv ('titanic_datasets.csv', target_column=0,categorical_labels=True, n_classes=2, columns_to_ignore=[2,7])

print("the first row of data",data[0])
for p in data:
    if p[1]=="female":
        p[1]= 1
    else:
        p[1]=0


net = tflearn.input_data(shape=[None, 6]) #An input layer, with variable input size of examples with 6 features (the [None, 6])
net = tflearn.fully_connected(net, 32) #Two hidden layers with 32 nodes
net = tflearn.fully_connected(net, 32) #net tells the computer to add it to the line above
net = tflearn.fully_connected(net, 2, activation='softmax') #An output later of 2 nodes, and a "softmax" activation (more on activations later)
net = tflearn.regression(net) #find the pattern

model = tflearn.DNN(net)
model.fit(data, labels, n_epoch=100, batch_size=16, show_metric=True)

dicaprio = [3, 'jack dawson', 'make', 19,0,0,'n/a', 5.0000]
print("jack", model.predict([[3,19,0,0,5.5]])[0][0])
