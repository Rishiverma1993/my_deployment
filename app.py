from flask import Flask , render_template, request

import marks as m

app = Flask(__name__ , template_folder='template')

@app.route("/", methods = ["GET","POST"])

def world():
    if request.method == "POST":
        hrs = request.form["hrs"]
        marks_pred = m.marks_preduction(hrs)
        print(marks_pred)
        
        
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)