import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('productos.db')
cursor = conn.cursor()

# Crear la tabla de productos si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        precio REAL,
        imagen TEXT,
        enlace TEXT
    )
''')

# Borrar productos existentes para evitar duplicados
cursor.execute('DELETE FROM productos')

# Lista de productos con rutas locales de imágenes
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

# Insertar productos en la base de datos
cursor.executemany('''
    INSERT INTO productos (nombre, descripcion, precio, imagen, enlace)
    VALUES (?, ?, ?, ?, ?)
''', productos)

# Guardar y cerrar la conexión
conn.commit()
conn.close()

print("✅ Base de datos actualizada correctamente.")
