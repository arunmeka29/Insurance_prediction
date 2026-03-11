# 1.load processed data from processed folder
# 2.create model and tarin data
# 3.save model in artifacts folder
from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd

x_train_scaled=pd.read_csv(r"C:\Users\Arunv\Desktop\Projects\Insurance_prediction\data\processed\x_train_scaled.csv")
x_test_scaled=pd.read_csv(r"C:\Users\Arunv\Desktop\Projects\Insurance_prediction\data\processed\x_test_scaled.csv")
y_train=pd.read_csv(r"C:\Users\Arunv\Desktop\Projects\Insurance_prediction\data\processed\y_train.csv")
y_test=pd.read_csv(r"C:\Users\Arunv\Desktop\Projects\Insurance_prediction\data\processed\y_test.csv")




model=LinearRegression()
model.fit(x_train_scaled,y_train)

with open(r"C:\Users\Arunv\Desktop\Projects\Insurance_prediction\artifacts\model.pkl","wb") as f:
    pickle.dump(model,f)
    
    
