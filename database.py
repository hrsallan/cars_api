import sqlite3

def conectar():
    conn = sqlite3.connect('cars_api.db')
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_banco():
    with conectar() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS carros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                ano TEXT NOT NULL,
                estilo TEXT NOT NULL,
                tracao TEXT NOT NULL
            )
        ''')
        
        cursor = conn.execute("SELECT COUNT(*) FROM carros")
        if cursor.fetchone()[0] == 0:
            print("Semeando garagem de lendas...")

            carros_iniciais = [
                ("Fiat Marea Turbo", "1999", "Sedan", "FWD"),
                ("Volkswagen Golf GTI", "1994", "Hatch", "FWD"),
                ("Chevrolet Omega CD 4.1", "1995", "Sedan", "RWD"),
                ("Ford Escort RS Cosworth", "1992", "Hatch", "AWD"),
                ("Honda Civic VTi", "1993", "Hatch", "FWD"),
                ("Mitsubishi Lancer Evolution IV", "1996", "Sedan", "AWD"),
                ("Subaru Impreza WRX", "1994", "Sedan", "AWD"),
                ("Toyota Supra A80", "1993", "Esportivo", "RWD"),
                ("Nissan Skyline GT-R R33", "1995", "Cupê", "AWD"),
                ("Chevrolet Astra GSi", "2003", "Hatch", "FWD"),
                ("Volkswagen Santana Quantum", "1992", "Perua", "FWD"),
                ("Fiat Tempra Turbo", "1994", "Sedan", "FWD"),
                ("Ford Focus RS", "2002", "Hatch", "FWD"),
                ("Audi RS2 Avant", "1994", "Perua", "AWD"),
                ("Chevrolet Vectra GSi", "1994", "Sedan", "FWD"),
                ("Renault Clio V6", "2001", "Hatch", "RWD"),
                ("Volkswagen Polo GTI", "1998", "Hatch", "FWD"),
                ("Peugeot 306 S16", "1994", "Hatch", "FWD"),
                ("Alfa Romeo 156", "1997", "Sedan", "FWD"),
                ("Chevrolet Silverado", "1997", "Picape", "RWD")
            ]
            
            conn.executemany(
                "INSERT INTO carros (nome, ano, estilo, tracao) VALUES (?, ?, ?, ?)", 
                carros_iniciais
            )
            conn.commit()
            print(f"{len(carros_iniciais)} carros adicionados!")

def buscar_carros():
    with conectar() as conn:
        cursor = conn.execute("SELECT * FROM carros")
        return [dict(row) for row in cursor.fetchall()]
    
def buscar_carro_por_id(car_id):
    with conectar() as conn:
        cursor = conn.execute("SELECT * FROM carros WHERE id = ?", (car_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    
def adicionar_carro(nome, ano, estilo, tracao):
    with conectar() as conn:
        cursor = conn.execute(
            "INSERT INTO carros (nome, ano, estilo, tracao) VALUES (?, ?, ?, ?)", 
            (nome, ano, estilo, tracao)
        )
        conn.commit()
        return cursor.lastrowid
    
def remover_carro(car_id):
    with conectar() as conn:
        conn.execute("DELETE FROM carros WHERE id = ?", (car_id,))
        conn.commit()