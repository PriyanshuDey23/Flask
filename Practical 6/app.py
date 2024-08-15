from flask import Flask,render_template,Response
import cv2


app=Flask(__name__)
camera=cv2.VideoCapture(0) # Access the camera

def generated_frames():
    while True : # Read the frames continuously
        ## Read the Camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpeg',frame) # encoding
            frame=buffer.tobytes()
        
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Open cv documentation Page





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')  # I have to create html content , this html should continuously hit the url to take the streaming data in index, 
def video():          # Here we will provide all the frames that I am getting from the webcam, give it to index.tml
    return Response(generated_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')  # Func(generate frames) :- will be taking the frames from the webcam, pass to index

if __name__=="__main__":
    app.run(debug=True)