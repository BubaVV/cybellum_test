import resources
from db import models
from globs import api, app, db

api.add_resource(resources.User, '/user', '/user/<int:id>')
api.add_resource(resources.Post, '/post', '/post/<int:id>')
api.add_resource(resources.Comment, '/comment/<int:post_id>')

@app.route('/flask')
def hello_world():
    return 'Hello from Flask!\n'

@app.route('/db')
def db_sample():
    user = db.get_or_404(models.User, '123')


    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)