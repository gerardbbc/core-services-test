from flask import Flask, request, jsonify, make_response
from flask_expects_json import expects_json

app = Flask(__name__)
app.config["DEBUG"] = True

pageConfigs = [
            {
                "name": "news_article_1",
                "id": "uk-1",
                "components": [{
                    "name": "logo",
                    "location": "/path/to/logo"
                }]
            },
            {
                "name": "news_article_2",
                "id": "uk-2",
                "components": [{
                    "name": "logo",
                    "location": "/path/to/logo"
                }]
            },
            {
                "name": "news_article_3",
                "id": "uk-3",
                "components": [{
                    "name": "logo",
                    "location": "/path/to/logo"
                }]
            },
            {
                "name": "news_article_4",
                "id": "uk-4",
                "components": [{
                    "name": "logo",
                    "location": "/path/to/logo"
                }]
            }
        ]      

schema = {
    "type": "object",
    "properties": {
        "name": { "type": "string" },
        "id": { "type": "string" },
        "components": { "type": "array"}
    },
    "required": ["id", "name", "components"]
}

@app.route('/page-configs', methods=['GET'])
def getAllPageConfigs():
    return make_response(jsonify(pageConfigs), 200)

@app.route('/page-configs/<id>', methods=['GET'])
def getPageConfig(id):
    for config in pageConfigs:
        if config.get('id') == id:
            return make_response(jsonify(config), 200)
    return make_response(jsonify({"error": "page config not found"}), 404)

@app.route('/page-configs', methods=['POST'])
@expects_json(schema)
def createPageConfig():
    req = request.get_json()
    if req in pageConfigs:
        return make_response(jsonify({"error": "page config already exists"}), 400)
    pageConfigs.append(req)
    return make_response({"message": "page config added"}, 201)

@app.route('/page-configs/<id>', methods=['PUT'])
@expects_json(schema)
def updatePageConfig(id):
    req = request.get_json()
    for index, config in enumerate(pageConfigs):
        if config.get('id') == id:
            pageConfigs[index] = req
            return make_response({"message": "page config updated"}, 200)
    pageConfigs.append(req)
    return make_response({"message": "page config added"}, 201)

@app.route('/page-configs/<id>', methods=['DELETE'])
def deletePageConfig(id):
    for index, page in enumerate(pageConfigs):
        if page.get('id') == id:
            pageConfigs.pop(index)
            return make_response({"message": "page config deleted"}, 200)
    return make_response({"error": "page config not found"}, 200)

app.run()
