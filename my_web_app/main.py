from flask import Flask, render_template, request
from map_location_API import Main

app = Flask(__name__)


@app.route("/")
def kar():
    return render_template("form.html")


@app.route('/map')
def data():
    users_name = request.args.get("User_names")
    count = request.args.get("Count")
    try:
        count = int(count)
    except Exception:
        count = 5
        return render_template('fail_numbers.html')
    try:
        return Main(users_name, count).get_root().render()
    except Exception:
        return render_template('API_problems.html')
    # return render_template('Users_location_map.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080, host="127.0.0.1")
