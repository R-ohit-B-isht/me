from flask import Flask ,request
import os
UPLOAD_FOLDER = './uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        # print(request.get_data())
        print( request.mimetype)
        file = request.data
        
        with open('./uploads/a.txt', 'w') as f:
            f.write(str(file))
        # file = request.files['file']
        # print(file.filename)
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