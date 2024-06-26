SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        descricao TEXT NOT NULL)
"""

SQL_INSERIR = """
    INSERT INTO produto (nome, preco, descricao)
    VALUES (?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, preco, descricao
    from produto
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE produto
    SET nome=?, preco=?, descricao=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM produto 
    WHERE id=?
"""

SQL_OBTER_UM = """
    SELECT id, nome, preco, descricao
    from produto
    WHERE id=?
"""


SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM produto
"""

