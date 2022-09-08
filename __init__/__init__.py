from functools import wraps
import sentry_sdk
from flask import Flask, redirect, Response, request
from flasgger import Swagger
from flask_cors import CORS
from flask_cache import Cache
from ldap.module.ldapControl import ldapControl
from sentry_sdk.integrations.flask import FlaskIntegration
import sentry_sdk

sentry_sdk.init(
    "http://427e1f0c6efc4b2b9f3dd1997eaf27ba@sentry-test.devops.com/2",
    # 异常捕获百分比===100%
    traces_sample_rate=1.0
)


app = Flask(__name__, template_folder='../templates')
cache = Cache(app, config={"CACHE_TYPE": "simple"})

CORS(app, supports_credentials=True)


def requires_basic_auth(function):
    """Decorator to require HTTP Basic Auth for your endpoint."""

    def check_auth(username, password):
        return ldapControl(user=username, passwd=password).login()

    def authenticate():
        return Response(
            "Authentication required.", 401,
            {"WWW-Authenticate": "Basic realm='Login Required'"},
        )

    @wraps(function)
    def decorated(*args, **kwargs):
        auth = request.authorization
        print(auth)
        # print(check_auth(auth.username, auth.password))
        # check_result = check_auth(auth.username, auth.password)["rv"]
        check_result = "ok"
        # assert check_auth(auth.username, auth.password)["rv"] == "ok"
        if not auth or check_result == 'err':
            return authenticate()
        return function(*args, **kwargs)
    return decorated


swagger_config = {
    "headers": [],
    "specs": [{
        "endpoint": 'devops-api',
        "route": '/devops-api.json',
        "title": '猎上运维接口工程',
        "rule_filter": lambda rule: True,  # all in
        "model_filter": lambda tag: True,  # all in
        "description": "开发者：qiuye",
        "termsOfService": "/team"
    }],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "title": "猎上运维接口工程",

}

Swagger(app, decorators=[requires_basic_auth], config=swagger_config)


@app.route("/")
# @requires_basic_auth
def returnApidocs():
    return redirect("/apidocs")


@app.route("/team")
def returnTeam():
    return "猎上自动化工程"


@app.route("/health")
def health():
    return "ok"
# @app.after_request
# def add_header(response):
#     response.headers['Access-Control-Allow-Headers'] = 'Authentication, Content-Type'
#     return response
