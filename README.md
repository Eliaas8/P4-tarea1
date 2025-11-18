Tabla: heroes

-id (INTEGER, PRIMARY KEY AUTOINCREMENT)
-nombre (TEXT, NOT NULL)
-clase (TEXT, CHECK(...))
-nivel_experiencia (INTEGER, CHECK(nivel_experiencia ≥ 1))

Tabla: misiones

id (INTEGER, PRIMARY KEY AUTOINCREMENT)

nombre (TEXT, NOT NULL)

nivel_dificultad (TEXT, CHECK(...))

localizacion (TEXT, NOT NULL)

recompensa (INTEGER, CHECK(recompensa ≥ 0))

Tabla: monstruos

id (INTEGER, PRIMARY KEY AUTOINCREMENT)

nombre (TEXT, NOT NULL)

tipo (TEXT, CHECK(...))

nivel_amenaza (INTEGER, CHECK BETWEEN 1 AND 10)

Tabla: misiones_heroes

id (INTEGER, PRIMARY KEY AUTOINCREMENT)

id_mision (INTEGER, FOREIGN KEY → misiones.id)

id_heroe (INTEGER, FOREIGN KEY → heroes.id)

Tabla: misiones_monstruos

id (INTEGER, PRIMARY KEY AUTOINCREMENT)

id_mision (INTEGER, FOREIGN KEY → misiones.id)

id_monstruo (INTEGER, FOREIGN KEY → monstruos.id)
