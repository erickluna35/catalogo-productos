from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Función para obtener productos desde la base de datos
def obtener_productos():
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

# Ruta principal
@app.route('/')
def inicio():
    productos = obtener_productos()
    return render_template('index.html', productos=productos)

# Iniciar el servidor
if __name__ == '__main__':
    print("Iniciando servidor Flask...")
    app.run(debug=True)
