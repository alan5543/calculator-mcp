# Advanced Calculator MCP Server
[![smithery badge](https://smithery.ai/badge/@alan5543/calculator-mcp)](https://smithery.ai/server/@alan5543/calculator-mcp)


## Introduction
The Advanced Calculator MCP Server is a powerful tool designed to assist Large Language Models (LLMs) in performing complex mathematical calculations. It provides a suite of mathematical functions that can be integrated with MCP-compatible clients (such as Claude Desktop) to enhance computational capabilities.

## Video Demo
- Collaborating with Sequential Thinking to solve the complex Maths
https://github.com/user-attachments/assets/c0690a93-c1fa-485d-a948-074e923e45da


## Tools
The server provides the following mathematical tools with their exact names and arguments:
- `add(a: int, b: int) -> int`: Add two numbers
- `sub(a: int, b: int) -> int`: Subtract two numbers
- `mul(a: int, b: int) -> int`: Multiply two numbers
- `div(a: int, b: int) -> float`: Divide two numbers (returns floating point result)
- `power(base: float, exponent: float) -> float`: Raise a number to a power
- `square_root(x: float) -> float`: Calculate square root of a number
- `factorial(n: int) -> int`: Calculate factorial of a non-negative integer
- `log(x: float, base: float = math.e) -> float`: Calculate logarithm of a number with optional base (default: natural log)
- `sin(x: float) -> float`: Calculate sine of an angle in radians
- `cos(x: float) -> float`: Calculate cosine of an angle in radians
- `tan(x: float) -> float`: Calculate tangent of an angle in radians
- `degrees_to_radians(degrees: float) -> float`: Convert degrees to radians
- `radians_to_degrees(radians: float) -> float`: Convert radians to degrees
- `gcd(a: int, b: int) -> int`: Calculate greatest common divisor of two integers
- `lcm(a: int, b: int) -> int`: Calculate least common multiple of two integers
- `is_prime(n: int) -> bool`: Check if a number is prime
- `quadratic_roots(a: float, b: float, c: float) -> tuple`: Solve quadratic equation ax² + bx + c = 0, returns a tuple of roots (real or complex)

## Manual Configuration
To set up the Advanced Calculator MCP Server locally, follow these steps:
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   ```
2. **Set Up UV**:
   Install UV (a Python package and project manager) if not already installed. Follow the official UV documentation for installation instructions.
3. **Configure MCP Client**:
   Add the following configuration to your MCP client (e.g., Claude Desktop):
   ```json
   "calculator-mcp-server": {
       "command": "uv",
       "args": [
           "--directory",
           "YOUR_CLONED_FOLDER",
           "run",
           "main.py"
       ]
   }
   ```
   Replace `YOUR_CLONED_FOLDER` with the path to the cloned repository.

## Remote MCP Server Configuration
The Advanced Calculator MCP Server is hosted remotely at [https://smithery.ai/server/@alan5543/calculator-mcp](https://smithery.ai/server/@alan5543/calculator-mcp). To configure and use the remote server:
1. Visit [https://smithery.ai](https://smithery.ai) and sign in or create an account.
2. Navigate to the server page: [https://smithery.ai/server/@alan5543/calculator-mcp](https://smithery.ai/server/@alan5543/calculator-mcp).
3. Click the "Add to Client" button or follow the provided integration instructions on the Smithery.ai platform.
4. In your MCP client (e.g., Claude Desktop), update the configuration to use the remote server URL instead of a local command. Refer to your client's documentation for specific instructions on setting up remote MCP servers.
5. Test the connection to ensure the server is accessible and functioning correctly.
