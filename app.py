from flasgger import Swagger
from config.config import app
from src.app.routes.auth_routes import auth_api
from src.app.routes.users_routes import user_api

app.config['SWAGGER'] = {
        'title': 'Flask Python API',
    }
swagger = Swagger(app)

app.register_blueprint(auth_api, url_prefix='/api')
app.register_blueprint(user_api, url_prefix='/api')

if __name__ == '__main__':
    ''' run application '''
    app.run(host='0.0.0.0', port=5000)