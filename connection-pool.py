from collections import deque
import time

class Connection:
    def __init__(self, conn_id):
        self.id = conn_id
        self.created_at = time.time()
    
    def execute(self, query):
        return f"Connection {self.id} executed: {query}"

class ConnectionPool:
    def __init__(self, max_size=5):
        self.max_size = max_size
        self.available = deque()  # Free connections
        self.in_use = set()       # Active connections
        self._conn_counter = 0
    
    def get_connection(self):
        """Get a connection from pool or create new one"""
        # Reuse existing connection
        if self.available:
            conn = self.available.popleft()
            self.in_use.add(conn)
            return conn
        
        # Create new if under limit
        if len(self.in_use) < self.max_size:
            conn = Connection(self._conn_counter)
            self._conn_counter += 1
            self.in_use.add(conn)
            return conn
        
        # Pool exhausted
        raise Exception("No available connections")
    
    def release_connection(self, conn):
        """Return connection to pool"""
        if conn in self.in_use:
            self.in_use.remove(conn)
            self.available.append(conn)
    
    def get_stats(self):
        return {
            "available": len(self.available),
            "in_use": len(self.in_use),
            "total": len(self.available) + len(self.in_use)
        }

# Usage
pool = ConnectionPool(max_size=3)

conn1 = pool.get_connection()
conn2 = pool.get_connection()
print(pool.get_stats())  # {'available': 0, 'in_use': 2, 'total': 2}

pool.release_connection(conn1)
print(pool.get_stats())  # {'available': 1, 'in_use': 1, 'total': 2}