#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load
        # print(self.connections)

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#

# server = Server()
# print(f"Server instances: {server.connections}")
# server.add_connection("192.168.1.1")
# print(f"Server instances(key=ip:value=current load for all connections): {server.connections}")
# print(f"Current load for all connections: {server.load():.3f}%")

# server.add_connection("192.168.1.157")
# print(f"Server instances(key=ip:value=current load for all connections): {server.connections}")
# print(f"Current load for all connections: {server.load():.3f}%")


# server.close_connection("192.168.1.1")
# print(f"Server instances(key=ip:value=current load for all connections): {server.connections}")
# print(f"Current load for all connections: {server.load():.3f}%")


#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        for server in self.servers:
            if connection_id in server.connections:
                server.close_connection(connection_id)

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load = 0
        total_server = 0
        for server in self.servers:
            total_load += server.load()
            total_server += 1
        return total_load/total_server

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        print(loads)
        return "[{}]".format(", ".join(loads))
#End Portion 2#


l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l)
print(l.connections)
print(l.avg_load())

l.servers.append(Server())
print(l)
print(l.avg_load())
# l.add_connection("fdca:83d2::d02f")
# print(l)
# print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l)
print(l.avg_load())


for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())