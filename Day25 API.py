from flask import  Flask , request , jsonify

app = Flask(__name__)

@app.route('/xyz', methods =['GET', 'POST'])
def test():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

@app.route('/abc/here', methods=['POST'])
def test1():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

@app.route('/abc/here/nope', methods = ['POST'])
def test2():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

@app.route('/abc/here/nope/nah', methods = ['POST'])
def test3():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

if __name__ == '__main__':
    app.run()


test(3,4)|
