#1.Load Training and testing data
#2.scale the traning data
#3.save scaled data in processed folder
import pickle
from sklearn.preprocessing import StandardScaler
from data_preprocessing import load_split_data
import pandas as pd

x_train,x_test,y_train,y_test=load_split_data()
scaler=StandardScaler()

x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)

pd.DataFrame(x_train_scaled).to_csv(r"C:\Users\Arunv\Desktop\Projects\Insurance_prediction\data\processed\x_train_scaled.csv",index=False)
pd.DataFrame(x_test_scaled).to_csv(r"C:\Users\Arunv\Desktop\Projects\Insurance_prediction\data\processed\x_test_scaled.csv",index=False)
pd.DataFrame(y_train).to_csv(r"C:\Users\Arunv\Desktop\Projects\Insurance_prediction\data\processed\y_train.csv",index=False)
pd.DataFrame(y_test).to_csv(r"C:\Users\Arunv\Desktop\Projects\Insurance_prediction\data\processed\y_test.csv",index=False)

with open(r"C:\Users\Arunv\Desktop\Projects\Insurance_prediction\artifacts\scaler.pkl","wb") as f:
    pickle.dump(scaler,f)
