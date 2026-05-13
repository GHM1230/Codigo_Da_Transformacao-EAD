import sqlite3

conn = sqlite3.connect('atividade_info_cliente.db')

cursor = conn.cursor()

clientes = cursor.fetchall()

cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES
                
    ('Leticia Dorta', 'joao.silva@mail.com'),
               
    ('Ayla Sousa', 'maria.oliveira@mail.com'),
               
    ('Aurélio Dinis ', 'carlos.santos@mail.com'),
               
    ('Igor Freitas', 'joao.silva@mail.com'),
               
    ('Ana Cecília ', 'maria.oliveira@mail.com'),
               
    ('Ana Alves', 'carlos.santos@mail.com'),
    
    ('André Ramalho', 'joao.silva@mail.com'),
               
    ('Maria Helena', 'maria.oliveira@mail.com'),
               
    ('Antônio Fernandes', 'carlos.santos@mail.com'),
    
    ('Ana Clara Machado', 'joao.silva@mail.com'),
               
    ('Vitor Bispo Cruz', 'maria.oliveira@mail.com'),
               
    ('Pedro Henrique', 'carlos.santos@mail.com')
               

''')

conn.commit()

cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', clientes)
conn.commit()
print("Sucesso: Novos clientes inseridos na base de dados.")

print("\n--- LISTA DE CLIENTES ATUAIS ---")
cursor.execute("SELECT * FROM clientes")
for cliente in cursor.fetchall():
    print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")

cursor.execute("UPDATE clientes SET email = ? WHERE nome = ?", ('igor.freitas@mail.com', 'Igor Freitas'))
print("\nSucesso: Email do Igor Freitas atualizado.")

cursor.execute("DELETE FROM clientes WHERE nome = ?", ('Leticia Dorta',))
print("Sucesso: Registro de Leticia Dorta removido.")

conn.commit()


print("Atividade 2 concluída: Operações CRUD realizadas.")

print('Atividade 2 concluída: Dados inseridos.')