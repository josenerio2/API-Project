from flask import Flask, jsonify
import hashlib
app = Flask(__name__)

tasks = [
    {
        'id': 'md5',
        'title': "md5",
        'description': 'hash algorithm', 
        'done': True
    },
    {
        'id': 'factorial',
        'title': 'factorial',
        'description': 'product of an integer and all the integers below it', 
        'done': True
    },
    {
        'id': 'fibonacci',
        'title':'fibonacci' ,
        'description': 'numbers', 
        'done': True
    },
    {
        'id': 'is-prime',
        'title':'is-prime' ,
        'description':'numbers that cant be formed by mult two smaller numbers' , 
        'done': True
    },
    {
        'id': 'slack-alert',
        'title':'slack-alert' ,
        'description':'notification on slack' , 
        'done': True
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/fibonacci/<int:x>', methods=['GET'])
def getFibonacci(x):
    x = int(x)
    if x == 0: 
        return 0
    elif x == 1: 
        return 1
    else: 
        return getFibonacci(x-1) + getFibonacci(x-2)

@app.route('/md5/<string:string>', methods=['GET'])
def getMD5(string):
    m = (hashlib.md5(str(string).encode()).hexdigest())
    return m

@app.route('/factorial/<int:x>', methods=['GET'])
def getFactorial(x):
    x = int(x)
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial



if __name__ == "__main__":
    app.run(host="0.0.0.0")