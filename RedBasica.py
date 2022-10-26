import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

Datos=np.load("DatosExperimento1.npy")
print(Datos.shape)

X=Datos[:,0:8]
Y=Datos[:,9]

print(X.shape)
print(Y.shape)

Y=to_categorical(Y)
print(Y.shape)

model=keras.Sequential()
model.add(Dense(100,input_dim=(8)))
model.add(Dense(200))
model.add(Dense(Y.shape[1],activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy")
model.fit(X,Y, epochs=100)