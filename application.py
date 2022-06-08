from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Second change from different computer.'

if __name__ == '__main__':
    application.run()