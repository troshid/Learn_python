from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (for example purposes)
users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    user = request.json
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = request.json
    users[user_id] = user
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.pop(user_id)
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
