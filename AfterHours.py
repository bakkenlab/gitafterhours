from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import commits

after_hours_app = Flask(__name__)
after_hours_api = Api(after_hours_app)


@after_hours_app.route('/api/v1/commits/<date_from>/<date_to>', methods=['GET'])
def get_commits(date_from, date_to):
    dates = commits.get_commits_in_range(int(date_from), int(date_to))
    return jsonify({'dates': dates})


if __name__ == '__main__':
    after_hours_app.run(port='5002')
