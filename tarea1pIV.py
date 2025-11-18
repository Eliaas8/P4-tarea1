import sqlite3

conn = sqlite3.connect('tarea1.db')
conn.execute("PRAGMA foreign_keys = ON;")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clase TEXT NOT NULL CHECK(clase IN ('Guerrero','Mago','Arquero','Clérigo','Asesino','Paladín')),
    nivel_experiencia INTEGER NOT NULL CHECK(nivel_experiencia >= 1)
);
""")

c.execute("""
CREATE TABLE IF NOT EXISTS misiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nivel_dificultad TEXT NOT NULL CHECK(nivel_dificultad IN ('Fácil','Media','Difícil','Épica')),
    localizacion TEXT NOT NULL,
    recompensa INTEGER NOT NULL CHECK(recompensa >= 0)
);
""")

c.execute("""
CREATE TABLE IF NOT EXISTS monstruos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL CHECK(tipo IN ('Dragón','Goblin','No-muerto','Bestia','Elemental','Orco')),
    nivel_amenaza INTEGER NOT NULL CHECK(nivel_amenaza BETWEEN 1 AND 10)
);
""")

c.execute("""
CREATE TABLE IF NOT EXISTS misiones_heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_mision INTEGER NOT NULL,
    id_heroe INTEGER NOT NULL,
    FOREIGN KEY (id_mision) REFERENCES misiones(id) ON DELETE CASCADE,
    FOREIGN KEY (id_heroe) REFERENCES heroes(id) ON DELETE CASCADE
);
""")

c.execute("""
CREATE TABLE IF NOT EXISTS misiones_monstruos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_mision INTEGER NOT NULL,
    id_monstruo INTEGER NOT NULL,
    FOREIGN KEY (id_mision) REFERENCES misiones(id) ON DELETE CASCADE,
    FOREIGN KEY (id_monstruo) REFERENCES monstruos(id) ON DELETE CASCADE
);
""")

conn.commit()
conn.close()

print("Base de datos tarea1.db creada correctamente.")
