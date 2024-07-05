from __init__ import create_app, initialize_data

app = create_app()
initialize_data()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)
