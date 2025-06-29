# main.py

from mcp.server.fastmcp import FastMCP
import math
import os

# --- Step 1: Define all your tools as plain Python functions ---
# Notice the @mcp.tool() decorators are removed from here.

def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

def sub(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

def mul(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

def div(a: int, b: int) -> float:
    """Divide two numbers (returns floating point result)"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base: float, exponent: float) -> float:
    """Raise a number to a power"""
    return math.pow(base, exponent)

def square_root(x: float) -> float:
    """Calculate square root of a number"""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

def factorial(n: int) -> int:
    """Calculate factorial of a non-negative integer"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

def log(x: float, base: float = math.e) -> float:
    """Calculate logarithm of a number with optional base (default: natural log)"""
    if x <= 0:
        raise ValueError("Logarithm is only defined for positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(x, base)

def sin(x: float) -> float:
    """Calculate sine of an angle in radians"""
    return math.sin(x)

def cos(x: float) -> float:
    """Calculate cosine of an angle in radians"""
    return math.cos(x)

def tan(x: float) -> float:
    """Calculate tangent of an angle in radians"""
    return math.tan(x)

def degrees_to_radians(degrees: float) -> float:
    """Convert degrees to radians"""
    return math.radians(degrees)

def radians_to_degrees(radians: float) -> float:
    """Convert radians to degrees"""
    return math.degrees(radians)

def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor of two integers"""
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of two integers"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

def is_prime(n: int) -> bool:
    """Check if a number is prime"""
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

def quadratic_roots(a: float, b: float, c: float) -> tuple:
    """
    Solve quadratic equation ax² + bx + c = 0
    Returns a tuple of roots (real or complex)
    """
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return (root1, root2)


def main():
    # --- Step 2: Create the MCP instance inside main() ---
    mcp = FastMCP("Advanced Calculator")

    # --- Step 3: Register all your tools here ---
    # The mcp.tool() method returns a decorator, which we immediately call with the function.
    tools = [
        add, sub, mul, div, power, square_root, factorial, log, sin, cos, tan,
        degrees_to_radians, radians_to_degrees, gcd, lcm, is_prime, quadratic_roots
    ]
    for tool_func in tools:
        mcp.tool()(tool_func)

    # --- Step 4: Run the server as before ---
    port = int(os.environ.get("PORT", 8080))
    mcp.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()