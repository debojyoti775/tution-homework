from flask import Flask
import math
app=Flask(__name__)
@app.route('/fact/<int:a>')
def fact(a):
    facto=math.factorial(5)
    return str(facto)
if __name__=='__main__':
    app.run(debug=True)
