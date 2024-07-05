from flask import send_from_directory

from __init__ import create_app, initialize_data

app = create_app()
initialize_data()


@app.route('/swagger/<path:path>')
def send_swagger(path):
    return send_from_directory('swagger', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True)
