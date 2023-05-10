from database_initialization import initialize_db

def build():
    """Function to call initializing of database, used with poetry invoke task.
    """
    
    initialize_db()

if __name__ == "__main__":
    build()