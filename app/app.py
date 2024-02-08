import resources
from globs import api, app

api.add_resource(resources.User, '/user', '/user/<int:id>')
api.add_resource(resources.Post, '/post', '/post/<int:id>')
api.add_resource(resources.Comment, '/comment/<int:post_id>')
api.add_resource(resources.Login, '/login')


@app.route('/flask')
def hello_world():
    return 'Hello from Flask!\n'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
