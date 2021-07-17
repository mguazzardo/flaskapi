from flask import Flask, jsonify, request
app = Flask(__name__)
#Me importo el objeto JSON mockeado.

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': "Producto no encontrado"})

@app.route('/products')
def getProducts():
    return jsonify({'products': products, 'message': 'Lista de productos'})


@app.route('/products', methods = ['POST'])
def addProducts():
    new_product = {
        "name":     request.json['name'],
        "price":    request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Producto agregado correctamente", "products": products })

@app.route('/products/<string:product_name>', methods = ['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name'],
        productsFound[0]['price'] = request.json['price'],
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Producto actualizado",
            "product": productsFound[0]
        })

    return jsonify({'message': "Producto no encontrado"})


@app.route('/products/<string:product_name>', methods = ['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({
            "message": "Producto Borrado",
            "product": products
        })

    return jsonify({'message': "Producto no encontrado"})





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
