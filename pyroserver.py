import Pyro4
import math

@Pyro4.expose
class MathOperations:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def modulus(self, a, b):
        return a % b

    def sqrt(self, a):
        if a < 0:
            return "Error: Square root of negative number"
        return math.sqrt(a)


def start_pyro_server():
    server = MathOperations()
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(server)
    ns.register("math.operations", uri)
    print("Pyro4 Server is running...")
    daemon.requestLoop()

if __name__ == "__main__":
    start_pyro_server()
