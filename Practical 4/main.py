
# Jinja 2 Template
# First Thing :-  conditions,for loops  {%...%}
# Second Thing :- Expression to print output {{  }}
# Third Thing :- For comments {#...#}



from flask import Flask,redirect,url_for,render_template,request
import pandas as pd

app=Flask(__name__)

# Home Page
@app.route('/')
def welcome():
    return render_template("index.html") # Call from Html File from template folder



# Success(using HTMl) # Change in Success
@app.route("/success/<int:score>")
def success(score):
    
    res=" "
    if score >= 50:
        res="PASS"
    

    exp={'score':score,'res':res} # This is the dictionary  , I am printing in the form
    
    
    
    return render_template("result.html",result=exp)


# http://127.0.0.1:5000/success/90




# Fail
@app.route("/fail/<int:score>") 
def fail(score):
    if score < 50:
        res="FAIL"
    

    exp={'score':score,'res':res} # This is the dictionary  , I am printing in the form
    
    
    
    return render_template("result.html",result=exp)
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
        result="success" # calling the function
    else:
        result="fail"    # Calling the function
    return redirect(url_for(result,score=total_score))




if __name__=='__main__':
    app.run(debug=True)