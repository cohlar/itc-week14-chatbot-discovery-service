from flask import Flask, request, abort, jsonify
import os


app = Flask(__name__)


endpoints = set()


@app.route('/api/discovery', methods=['POST'])
def add_endpoint():
    global endpoints
    if not request.get_json():
        abort(400, 'You are missing the payload, please send your enpoint url as a POST payload.')
    new_endpoint = request.get_json().get('endpoint')
    if not new_endpoint:
        abort(400, '''The payload needs to be a JSON in the format {'endpoint': 'your endpoint url'}''')
    endpoints.add(new_endpoint)
    return jsonify({'message': f'Enpoint {new_endpoint} has been successfully added to the discovery server'}), 200


@app.route('/api/discovery', methods=['GET'])
def get_endpoints():
    global endpoints
    return jsonify({'endpoints': list(endpoints)}), 200


@app.route('/api/discovery', methods=['POST'])
def remove_endpoint():
    global endpoints
    if not request.get_json():
        abort(400, 'You are missing the payload, please send your enpoint url as a POST payload.')
    endpoint_to_delete = request.get_json().get('endpoint')
    if not endpoint_to_delete:
        abort(400, '''The payload needs to be a JSON in the format {'endpoint': 'your endpoint url'}''')
    endpoints.discard(endpoint_to_delete)
    return jsonify({'message': f'Enpoint {endpoint_to_delete} has been successfully removed from the discovery server'}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)