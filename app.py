from flask import Flask, jsonify, make_response
from math import sqrt
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
    fibonacci = ((1+sqrt(5))**x-(1-sqrt(5))**x)/(2**x*sqrt(5))
    return jsonify({'input':x, 'output':fibonacci})
    
    
@app.route('/md5/<string:string>', methods=['GET'])
def getMD5(string):
    m = (hashlib.md5(str(string).encode()).hexdigest())
    return jsonify({'input':string, 'output':m})

@app.errorhandler(404) #code from miguelgrinberg to handle 404 errors
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)




if __name__ == "__main__":
    app.run(host="0.0.0.0")
