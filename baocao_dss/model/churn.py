import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder#model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn import metrics
from sklearn.metrics import classification_report
scaler = StandardScaler() #chuan hoa du lieu dua ve chuan (0,1)
#xu ly du lieu

def fit():
    df = pd.read_csv('dulieu.csv')
    # print(df.head())
    lista = [ 'Class']
    df[lista] = df[lista].apply(lambda x:x.map({'Churned': 1, "Active": 0}))
    df_dummy = pd.get_dummies(df[['aug_user_type', 'sep_user_type', 'aug_fav_a','sep_fav_a']])
    df = pd.concat([df,df_dummy], axis=1)
    df=df.drop(columns=['aug_user_type', 'sep_user_type','aug_fav_a', 'sep_fav_a'])
    df=df.drop(columns=['aug_fav_a_ufone','sep_fav_a_ptcl','aug_fav_a_ptcl','sep_fav_a_telenor','aug_fav_a_telenor','aug_user_type_Other', 'sep_user_type_Other','aug_user_type_2G', 'sep_user_type_2G','aug_fav_a_0','aug_fav_a_mobilink','aug_fav_a_warid','sep_fav_a_warid','aug_fav_a_zong','sep_fav_a_zong' ])
    #chia tap train
    Y = df['Class']
    X = df.drop(["Class"],axis=1)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.7, test_size=0.3,random_state=28)
    X_train[["network_age","Aggregate_Total_Rev","Aggregate_SMS_Rev","Aggregate_Data_Rev","Aggregate_Data_Vol","Aggregate_OFFNET_REV"]]= scaler.fit_transform(X_train[["network_age","Aggregate_Total_Rev","Aggregate_SMS_Rev","Aggregate_Data_Rev","Aggregate_Data_Vol","Aggregate_OFFNET_REV"]])
    x_train_const=sm.add_constant(X_train)
    logit = sm.Logit(Y_train,x_train_const)
    result = logit.fit()
    # print (result.summary())
    #xac suat du doan 
    y_predicted_train = result.predict(x_train_const)
    # print(y_predicted_train.head())
    y_predicted_train_df = pd.DataFrame(index= Y_train.index, columns=('Churn','Churn_Probability'))
    y_predicted_train_df = pd.DataFrame({'Churn':Y_train.values, 'Churn_Probability':y_predicted_train})
    y_predicted_train_df.index.name = 'customerID'
    print(y_predicted_train_df.head())
    # Dự đoán khả năng churn trên tập train
    #Tạo cột 'predicted' nhận giá trị 1 nếu Churn_Prob > 0.5 nếu không nhận giá trị 0
    m_train=y_predicted_train_df
    m_train['Churn_Predict'] = m_train.Churn_Probability.map(lambda x: 1 if x >=0.5 else 0)
    print(m_train.head(10))
    #Test model
    X_test[["network_age","Aggregate_Total_Rev","Aggregate_SMS_Rev","Aggregate_Data_Rev","Aggregate_Data_Vol","Aggregate_OFFNET_REV"]]= scaler.fit_transform(X_test[["network_age","Aggregate_Total_Rev","Aggregate_SMS_Rev","Aggregate_Data_Rev","Aggregate_Data_Vol","Aggregate_OFFNET_REV"]])
    x_test_const=sm.add_constant(X_test)
    y_predicted_test = result.predict(x_test_const)
    print(y_predicted_test.head())
    y_predicted_test_df = pd.DataFrame(index= Y_test.index, columns=('Churn','Churn_Probability'))
    y_predicted_test_df = pd.DataFrame({'Churn':Y_test.values, 'Churn_Probability':y_predicted_test})
    y_predicted_test_df.index.name = 'customerID'
    print(y_predicted_test_df.head())
    # Dự đoán khả năng churn trên tập test
    #Tạo cột 'predicted' nhận giá trị 1 nếu Churn_Prob > 0.5 nếu không nhận giá trị 0
    m_test=y_predicted_test_df
    m_test['Churn_Predict'] = m_test.Churn_Probability.map(lambda x: 1 if x >=0.5 else 0)
    print(m_test.head())
    print(metrics.accuracy_score(y_predicted_test_df['Churn'],m_test['Churn_Predict']))
    #XU LY DU LIEU HIEN THI TREN WEB
    df1=pd.read_csv('dulieu.csv')
    x_1=df1.drop(["Class"],axis=1)
    print(x_1.head())
    #gộp theo hàng cái này t dùng để gộp cái dự đoán xs của tập train và test lại
    y_1=y_predicted_train_df.append(y_predicted_test_df)
    print('y1')
    print(y_1.head())
    #gộp theo cột giữ nguyên index, sau khi gộp lại giá trị y rồi thì kết nối cột y xs với x ban đầu 
    output_xs=x_1.merge(y_1,left_on=None, right_on=None, left_index=True, right_index=True)
    print(output_xs.head())
    #Cái này muốn hiển thị vào trang thống kê 
    du_doan=output_xs.drop(columns=['Churn','Churn_Predict'])
    print(du_doan.head())
    muc_1=du_doan[du_doan['Churn_Probability']<0.2]
    muc_2= du_doan[du_doan['Churn_Probability']>=0.2]
    muc_2= muc_2[muc_2['Churn_Probability']<0.5]
    muc_3= du_doan[du_doan['Churn_Probability']>=0.5]
    #Ngoài ra trang thống kê còn  hiển thị biểu đồ theo 3  mức  nếu  xs nằm trong [0,0.2) thì mức 1, [0.2,0.5) mức 2, xs>0=0.5 mức 3
    # Và Hiển thị danh sách khách hàng theo 3 mức như trên  bao gồm thông tin và xs rời đi tương ứng của khách hàng
    


def predict1():
    return muc_1

def predict2():
    return muc_2
def predict3():
    return muc_3