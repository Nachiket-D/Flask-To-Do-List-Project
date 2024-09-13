from flask import Flask, jsonify, request, render_template, redirect, url_for, abort
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'


def read_json():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}


def write_json(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


@app.route('/')
def index():
    data = read_json()
    return render_template('index.html', items=data)


@app.route('/items/create', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST':
        data = read_json()
        new_id = max(map(int, data.keys()), default=0) + 1
        new_item = {
            'name': request.form['name'],
            'description': request.form['description']
        }
        data[str(new_id)] = new_item
        write_json(data)
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/items/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    data = read_json()
    if str(item_id) not in data:
        abort(404)

    if request.method == 'POST':
        updated_item = {
            'name': request.form['name'],
            'description': request.form['description']
        }
        data[str(item_id)] = updated_item
        write_json(data)
        return redirect(url_for('index'))

    item = data.get(str(item_id))
    return render_template('update.html', item_id=item_id, item=item)


@app.route('/items/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    data = read_json()
    if str(item_id) not in data:
        abort(404)
    
    data.pop(str(item_id))
    write_json(data)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
