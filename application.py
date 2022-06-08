from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hi this is my first change on the deployed project.'

if __name__ == '__main__':
    application.run()