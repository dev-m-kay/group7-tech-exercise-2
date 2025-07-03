from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
# Cole was here
#Elijah change for pull request
#Elijah was also here

# Edwart was here
#Devon was also here
# new change for pull request
