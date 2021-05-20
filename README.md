# CovidPredictor
A Machine Learning  model implemented with python to predict Covid

## Dependencies
1.Keras  
2.Tensorflow  
3.Tkinter  
4.Numpy  

## Description
1.The app takes 8 inputs viz.  
2.Cough(true/false)  
3.Fever(true/false)  
4.Sore Throat(true/false)  
5.Shortness of breath(true/false)  
6.Headache(true/false)  
7.Age60 and above(true/false)  
8.Gender(Male/Female)  
9.Contact with Covid positive person(true/false/don't know)  

The ML model uses a Neural Network with 3 layers. The first layer contains 12 nodes, a hidden layer with 8 nodes and a output layer with one node.It also implements early stopping to prevent overfitting.

### Data
The ML model is trained with the help of data stored in **data.txt** .It is obtained from [covidpred](https://github.com/nshomron/covidpred.)

The model has an accuracy of almost 93%

## License
© Sanchayan Bhowal