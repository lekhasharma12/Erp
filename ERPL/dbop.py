sql_create_roles_table = """ CREATE TABLE IF NOT EXISTS roles (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        ); """

sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    role_id integer NOT NULL,
                                    FOREIGN KEY (role_id) REFERENCES roles (id)
                                );"""