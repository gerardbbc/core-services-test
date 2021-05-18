import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

articles = [
            {
                "name": "news_article_1",
                "id": "0",
                "components": [{
                    "name": "logo",
                    "location": "/path/to/logo"
                }]
            },
            {
                "name": "news_article_2",
                "id": "1",
                "components": [{
                    "name": "logo",
                    "location": "/path/to/logo"
                }]
            },
            {
                "name": "news_article_3",
                "id": "2",
                "components": [{
                    "name": "logo",
                    "location": "/path/to/logo"
                }]
            },
            {
                "name": "news_article_4",
                "id": "3",
                "components": [{
                    "name": "logo",
                    "location": "/path/to/logo"
                }]
            }
        ]      

id_count = 4

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    global id_count
    if request.method == "GET":
        if 'id' in request.args:
            for article in articles:
                if article.get('id') == request.args.get('id'):
                    return jsonify(article)    
            return "Error - article not found"
        else:
            return jsonify(articles)
    
    elif request.method == "POST":
        articles.append({
            "name": "news_article_" + str(id_count + 1),
                "id": str(id_count),
                "components": [{
                    "name": "logo",
                    "location": "/path/to/logo"
                }]
        })
        id_count += 1
        return jsonify(articles)

app.run()
