SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone INTEGER NOT NULL,
        endereco TEXT NOT NULL,
        senha TEXT NOT NULL)
"""

SQL_INSERIR = """
    INSERT INTO cliente (nome, email, telefone, endereco, senha)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, email, telefone, endereco, senha
    from cliente
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE cliente
    SET nome=?, email=?, telefone=?, endereco=?, senha=?
    WHERE id=?
"""

SQL_EXCLUIR  = """
    DELETE FROM cliente
    WHERE id=?
"""

SQL_OBTER_UM = """
    SELECT id, nome, email, telefone, endereco, senha
    from cliente
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM cliente
"""