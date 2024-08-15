from flask import Flask

app=Flask(__name__) # It will be interacting with the server(WSGI Application)

@app.route('/') # Decorator
def welcome():
    return "Hello World , I am going to win "

@app.route('/memebers') 
def welco():
    return "Hello World dwqwerew fdsgrfdrgdf "






if __name__=="__main__": # Starting Of the program
    app.run(debug=True)  # DEbug will help it automatically save it, not need to restart

