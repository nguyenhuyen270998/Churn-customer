from flask import Flask, render_template
import pandas as pd
# import model 

app = Flask(__name__)

@app.route('/')
def home():
    results= pd.read_csv('duieugoc.csv')
    fieldnames= results.columns.values
    return render_template("index.html", fieldnames= fieldnames, results=results, len=len )

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def Register():
    return render_template("register.html")

@app.route('/statictis')
def statistic():
    results= pd.read_csv('dudoan_total.csv')
    fieldnames= results.columns.values

    muc1= pd.read_csv('muc_1.csv')
    muc1_count= len(muc1)
    muc2= pd.read_csv('muc_2.csv')
    muc2_count= len(muc2)
    muc3= pd.read_csv('muc_3.csv')
    muc3_count= len(muc3)

    values=[muc1_count,muc2_count,muc3_count]
    labels=['group 1','group 2','group 3']
    return render_template("charts.html", results= results, fieldnames=fieldnames , len=len, values=values, labels=labels)

@app.route('/statictis/muc1')
def statistic_1():
    results1= pd.read_csv('muc_1.csv')
    fieldnames1= results1.columns.values
    muc1_count= len(results1)
    muc2= pd.read_csv('muc_2.csv')
    muc2_count= len(muc2)
    muc3= pd.read_csv('muc_3.csv')
    muc3_count= len(muc3)

    values=[muc1_count,muc2_count,muc3_count]
    labels=['group 1','group 2','group 3']
    return render_template("charts_muc1.html", results1= results1, fieldnames1=fieldnames1 , len=len, values=values, labels=labels)

@app.route('/statictis/muc2')
def statistic_2():
    results2= pd.read_csv('muc_2.csv')
    fieldnames2= results2.columns.values
    muc1= pd.read_csv('muc_1.csv')
    muc1_count= len(muc1)
    muc2_count= len(results2)
    muc3= pd.read_csv('muc_3.csv')
    muc3_count= len(muc3) 

    values=[muc1_count,muc2_count,muc3_count]
    labels=['group 1','group 2','group 3']
    return render_template("charts_muc2.html", results2= results2, fieldnames2=fieldnames2, len=len, values=values, labels=labels)

@app.route('/statictis/muc3')
def statistic_3():
    results3= pd.read_csv('muc_3.csv')
    fieldnames3= results3.columns.values
    muc1= pd.read_csv('muc_1.csv')
    muc1_count= len(muc1)
    muc2= pd.read_csv('muc_2.csv')
    muc2_count= len(muc2)    
    muc3_count= len(results3)

    values=[muc1_count,muc2_count,muc3_count]
    labels=['group 1','group 2','group 3']
    return render_template("charts_muc3.html", results3= results3, fieldnames3=fieldnames3, len=len, values=values, labels=labels)




if __name__ == '__main__':
    app.run()