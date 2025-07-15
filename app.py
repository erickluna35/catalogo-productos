from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

# Ruta de la base de datos
DB_PATH = 'productos.db'

# Crear la base de datos si no existe
def inicializar_base_de_datos():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                precio REAL,
                imagen TEXT,
                enlace TEXT
            )
        ''')
        productos = [
            (
                'PC Gamer',
                'Computadora de alto rendimiento para videojuegos.',
                24999.99,
                'static/img/pc_gamer.jpg',
                'https://www.youtube.com/watch?v=u-sl4Kx2wsY'
            ),
            (
                'Mouse Gamer',
                'Mouse ergonómico con luces LED y alta precisión.',
                799.50,
                'static/img/mouse_gamer.jpg',
                'https://www.youtube.com/watch?v=H1KfN_uGBvs'
            ),
            (
                'Figura 3D de Zoro',
                'Figura coleccionable del personaje Zoro de One Piece.',
                1599.00,
                'static/img/zoro.jpg',
                'https://www.youtube.com/watch?v=3Ew8B10VwoQ'
            )
        ]
        cursor.executemany("INSERT INTO productos (nombre, descripcion, precio, imagen, enlace) VALUES (?, ?, ?, ?, ?)", productos)
        conn.commit()
        conn.close()
        print("✅ Base de datos creada correctamente.")

# Obtener productos desde la base de datos
def obtener_productos():
    conn = sqlite3.connect(DB_PATH)
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

# Ejecutar la aplicación (Railway necesita host=0.0.0.0 y PORT del entorno)
if __name__ == '__main__':
    inicializar_base_de_datos()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
