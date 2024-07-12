# train_model.py

import numpy as np
from alexnet import alexnet
import pickle as pkl
WIDTH = 160
HEIGHT = 120
# WIDTH = 800
# HEIGHT = 600
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'pygta5-car-fast-{}-{}-{}-epochs-300K-data.model'.format(LR, 'alexnetv2',EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

hm_data = 22



for i in range(EPOCHS):
    for i in range(1,hm_data+1):
       
        with open('training_data2.pkl', 'rb') as file:
            train_data = pkl.load(file)
       
      #  with open('training_data-{}.pkl'.format(i), 'rb') as file:
        #    train_data = pkl.load(file)
   
        train = train_data[:-100] #400
        test = train_data[-100:] #100
        #print(f"Type of train_data: {type(train_data)}")  # Check the data type
        #print(f"Type of train: {type(train)}")  # Check the type after splitting
        #print(f"Sample element in train: {train[0]}")

      #  print(f"Shape of train: {train.shape}")  # Check the training set shape
        #print(f"Shape of test: {test.shape}")   # Check the testing set shape

        

    
        print("Size of train_data:", len(train_data))

       # print(len(train))
       # print(len(test))                                                                                            [[x,y,z,w],[0,0,1]]
       # print(type(train_data))
        X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
       # print(X.shape)     
        #X = X[::3, :, :, :]
        print(X.shape)

        #(272, 160, 120, 1)
        #X = np.array([i[0] for i in train])  # Assuming image data is at index 0
       # X = X.reshape(-1, WIDTH, HEIGHT, 1)  # Reshape based on image dimensions
       # print(X[700])
        Y =[i[1] for i in train]
       # print(Y.shape)

        test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
        test_y = [i[1] for i in test]
       # print(X)
        print(X.shape)
      #  print(Y)
       # print(Y.shape)
        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
            snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

        model.save(MODEL_NAME)



# tensorboard --logdir=foo:C:/path/to/log





