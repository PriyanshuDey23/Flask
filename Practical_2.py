### Building Url Dynamically
### VAriable Rules And URL Building
### we also want to build the separate pages for pass and fail
# redirect:-  It will redirect to some success or fail page
# url_for:- For url Dynamic
from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Hello Everyone"

@app.route("/success/<int:score>") # Here score is int,  # <score>- It will be treated as integer
def success(score):
    return "The Person Has Passed and the marks is " + str(score)
# http://127.0.0.1:5000/success/90

@app.route("/fail/<int:score>") 
def fail(score):
    return "The Person Has Failed and the marks is " + str(score)
# http://127.0.0.1:5000/fail/20

# Result Checker
# 1 ->  Normal 
@app.route("/result/<int:score>") # we will check the score
def result(score):
    
    if score < 50:
        return fail(score)
    else :
        return success(score)
    

# http://127.0.0.1:5000/result/50

# Url Dynamic
@app.route("/results/<int:marks>") # we will check the score
def results(marks):
    result= ""
    if marks < 50:
        result= 'fail'
    else :
        result= 'success'
    return redirect(url_for(result,score=marks))





if __name__=='__main__':
    app.run(debug=True)