from flask import Flask,jsonify,request

app = Flask(__name__)
pizzaDB = [
    {'name': 'tonno','ingredienten':["kaas, tomaat, tonijn"],"vorm":"rond"},
    {'name': 'salami','ingredienten':["kaas, tomaat, salami"],"vorm":"rond"},
    {'name': 'hawaii','ingredienten':["kaas, tomaat, ananas,ham"],"vorm":"vierkant"}
]

@app.route("/",methods=['GET'])
def getPizza():
    return jsonify({'pizzaDB':pizzaDB})

@app.route("/<string:name>",methods=['GET'])
def getOnePizza(name):
    resultPizza = []
    print(name)
    for pizza in pizzaDB:
        if pizza['name']== name:
            resultPizza.append(pizza)
    return jsonify ({'pizzaDB':resultPizza})
if __name__ == '__main__':
    app.run()