
import json
import urllib

import flask
import requests
from flask_cors import CORS
import logging

# TODO: change this according your needs
sentry_host = "sentry-test.devops.com"
known_project_ids = ["7"]

app = flask.Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/bugs", methods=["POST"])
def bugs():
    try:
        envelope = flask.request.data.decode("utf-8")
        piece = envelope.split("\n")[0]
        header = json.loads(piece)
        dsn = urllib.parse.urlparse(header.get("dsn"))

        if dsn.hostname != sentry_host:
            raise Exception(f"Invalid Sentry host: {dsn.hostname}")

        project_id = dsn.path.strip("/")
        if project_id not in known_project_ids:
            raise Exception(f"Invalid Project ID: {project_id}")

        url = f"http://{sentry_host}/api/{project_id}/envelope/"
        print(url)
        header = {
            "X-Sentry-Token":"62b9c1a613bf11eda0d8629da323c68d",
            "Referer": "http://sentry-web.devops.com/"
        }
        re = requests.post(url=url, data=envelope, headers=header)
        status = re.status_code
        print(status)
    except Exception as e:
        # handle exception in your preferred style,
        # e.g. by logging or forwarding to Sentry
        logging.exception(e)

    return {}

if __name__ == "__main__":
    # print("app starting...")
    app.run("0.0.0.0", port=5000, debug=True)