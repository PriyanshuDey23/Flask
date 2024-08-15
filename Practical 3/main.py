### Integrate HTML with Flask (Jinga 2)
### Https verb GET and POST 
# First Thing is , when we go home page , we will show an Html Page
# render_template :- Render An Html Page
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

# Home Page
@app.route('/')
def welcome():
    return render_template("index.html") # Call from Html File from template folder

# Success(using HTMl)
@app.route("/success/<int:score>")
def success(score):
    result= " "
    if score >= 50:
        result="PASS"
    else:
        result="FAIL"

    return render_template("result.html",result=result) 
# http://127.0.0.1:5000/success/90

# Fail
@app.route("/fail/<int:score>") 
def fail(score):
    return "The Person Has Failed and the marks is " + str(score)
# http://127.0.0.1:5000/fail/20


#Result Checker
#1 ->  Normal 
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
# Check for 2 times one is pass another is fail , to see the different result


### Result checker for html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        Science=float(request.form['Science']) # Name from html
        Maths=float(request.form['Maths'])
        C=float(request.form['C'])
        DataScience=float(request.form['DataScience'])
        total_score=(Science+Maths+C+DataScience)/4
    result= " "
    if total_score >= 50:
        result="success"
    else:
        result="fail"
    return redirect(url_for(result,score=total_score))




if __name__=='__main__':
    app.run(debug=True)