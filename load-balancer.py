class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0  # For round-robin
        self.connections = {server: 0 for server in servers}  # For least connections
    
    def get_server_round_robin(self):
        """Simple round-robin: rotate through servers"""
        if not self.servers:
            return None
        
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server
    
    def get_server_least_connections(self):
        """Least connections: pick server with fewest active connections"""
        if not self.servers:
            return None
        
        # Find server with minimum connections
        return min(self.servers, key=lambda s: self.connections[s])
    
    def record_connection(self, server):
        """Track new connection to server"""
        if server in self.connections:
            self.connections[server] += 1
    
    def release_connection(self, server):
        """Track connection closed"""
        if server in self.connections:
            self.connections[server] = max(0, self.connections[server] - 1)

# Usage
lb = LoadBalancer(["server1", "server2", "server3"])

# Round-robin
print(lb.get_server_round_robin())  # server1
print(lb.get_server_round_robin())  # server2
print(lb.get_server_round_robin())  # server3
print(lb.get_server_round_robin())  # server1 (wraps around)

# Least connections
lb.record_connection("server1")
lb.record_connection("server1")
lb.record_connection("server2")
print(lb.get_server_least_connections())  # server3 (0 connections)