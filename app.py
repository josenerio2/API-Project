from flask import Flask, jsonify

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
        'title': 'gfgf',
        'description': '', 
        'done': False
    },
    {
        'id': 'fibonacci',
        'title':'' ,
        'description': '', 
        'done': True
    },
    {
        'id': 'is-prime',
        'title':'' ,
        'description':'' , 
        'done': False
    },
    {
        'id': 'slack-alert',
        'title':'' ,
        'description':'' , 
        'done': False
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






if __name__ == "__main__":
    app.run(host="0.0.0.0")