from flask import Flask ,request
import os

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        print(request.files.get('file'))
        # file = request.files.get('file')
        # if file:
        #     mimetype = file.content_type
        #     filename = werkzeug.secure_filename(file.filename)
        #     file.save(os.path.join(UPLOAD_FOLDER, filename)
        # else:
        #     print("hi")    
        
        return "post"
    else:
        return "get"
    
    
if __name__ == "__main__":
    app.run(debug=True)