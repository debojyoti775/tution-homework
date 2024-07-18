from flask import Flask


app=Flask(__name__)
@app.route("/detail/<name>/<title>/<gender>")
def call(name,title,gender):
    if gender=="male":
        return"MR "+name+" "+title+" you are "+gender
    else:
        return"MRS "+name+" "+title+" you are "+gender
    


if __name__=='__main__':
    app.run(debug=True)