from flask import Flask
app=Flask(__name__)
@app.route('/max')
def max_value():
    a=max([23,7,65,90])
    return str(a)+''+'is the max number'
if __name__=='__main__':
    app.run(debug=True)
    