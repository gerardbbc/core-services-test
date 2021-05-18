from flask import Flask, request, jsonify, make_response
from flask_expects_json import expects_json

app = Flask(__name__)
app.config["DEBUG"] = True

pages = [
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
    "required": ["id"]
}

@app.route('/pages', methods=['GET'])
def getAllPageConfigs():
    return make_response(jsonify(pages), 200)

@app.route('/pages/<id>', methods=['GET'])
def getPageConfig(id):
    for page in pages:
        if page.get('id') == id:
            return make_response(jsonify(page), 200)
    return make_response(jsonify({"error": "page config not found"}), 404)

@app.route('/pages', methods=['POST'])
@expects_json(schema)
def createPageConfig():
    req = request.get_json()
    if req in pages:
        return make_response(jsonify({"error": "page config already exists"}), 400)
    pages.append(req)
    return make_response({"message": "page config added"}, 201)

@app.route('/pages/<id>', methods=['PUT'])
@expects_json(schema)
def updatePageConfig(id):
    req = request.get_json()
    for index, page in enumerate(pages):
        if page.get('id') == id:
            pages[index] = req
            return make_response({"message": "page config updated"}, 200)
    pages.append(req)
    return make_response({"message": "page config added"}, 201)

@app.route('/pages/<id>', methods=['DELETE'])
def deletePageConfig(id):
    for index, page in enumerate(pages):
        if page.get('id') == id:
            pages.pop(index)
            return make_response({"message": "page config deleted"}, 200)
    return make_response({"error": "page config not found"}, 200)

app.run()
