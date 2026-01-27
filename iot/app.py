from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect('home_automation.db')

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT fan, light, door FROM devices WHERE id = 1")
    devices = cursor.fetchone()
    conn.close()

    return render_template('index.html', devices=devices)

@app.route('/device/<name>/<state>')
def control_device(name, state):
    allowed_devices = ['fan', 'light', 'door']
    if name not in allowed_devices:
        return "Invalid device", 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE devices SET {name} = ? WHERE id = 1",
        (state,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

