from flask import Flask, request, abort, jsonify


app = Flask(__name__)


endpoints = []


@app.route('/api/discovery', methods=['POST'])
def add_server():
    global endpoints
    if not request.get_json():
        abort(400, 'You are missing the payload, please send your enpoint url as a POST payload.')
    new_endpoint = request.get_json().get('endpoint')
    if not new_endpoint:
        abort(400, '''The payload needs to be a JSON in the format {'endpoint': 'your endpoint url'}''')
    endpoints.append(new_endpoint)
    return jsonify({'message': f'Enpoint {new_endpoint} has been successfully added to the database'}), 200


@app.route('/api/discovery', methods=['GET'])
def get_endpoints():
    global endpoints
    return jsonify({'endpoints': endpoints}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)