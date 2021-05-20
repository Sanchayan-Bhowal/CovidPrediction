from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping,ModelCheckpoint

dataset =loadtxt("data.txt",delimiter=",")

n_train=139424

X = dataset[:,0:8]
Y = dataset[:,8]

trainX, testX = X[:n_train, :], X[n_train:, :]
trainy, testy = Y[:n_train], Y[n_train:]

# print(X[0])
# print(trainX[0],' ',testX[0])
# print(Y[0])
# print(trainy[0],' ',testy[0])
model = Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=200)
mc = ModelCheckpoint('best_model.h5', monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)

# fit the keras model on the dataset
# model.fit(X, Y, epochs=256, batch_size=14000)
model.fit(trainX, trainy, validation_data=(testX, testy), epochs=400, batch_size=14000, verbose=0, callbacks=[es, mc])
# # evaluate the keras model
# _, accuracy = model.evaluate(X, Y)
# print('Accuracy: %.2f' % (accuracy*100))