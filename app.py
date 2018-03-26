from flask import Flask

app = Flask(__name__)

tasks = [
    {
        'id': md5,
        'title': "md5",
        'description': 'hash algorithm', 
        'done': True
    },
    {
        'id': factorial,
        'title': ,
        'description': , 
        'done': False
    },
    {
        'id': fibonacci,
        'title': ,
        'description': , 
        'done': False
    },
    {
        'id': is-prime,
        'title': ,
        'description': , 
        'done': False
    },
    {
        'id': slack-alert,
        'title': ,
        'description': , 
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route





if __name__ == "__main__":
    app.run(host="0.0.0.0")