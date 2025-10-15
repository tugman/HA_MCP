# Imports
from mcp.server.fastmcp import FastMCP
import requests 



# Instantiate the MCP server client
mcp = FastMCP("Hello, and welcome to HA MCP:-)")



@mcp.tool()
def getAPI(urlAddr: str) -> str:
    response = requests.get(urlAddr, auth=('moi','pass'))
    print(response.status_code)
    print(response.text)
    return str(response.text)


@mcp.tool()
def checkAPI():
    url = "http://192.168.1.60:8123/api/"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI1M2VkMDdmZDhhYzQ0YTI2OGNhMmZjMGY4MmZhMjJlNyIsImlhdCI6MTc0NjgwOTYwNCwiZXhwIjoyMDYyMTY5NjA0fQ.w5FM6otNEJFysqxWUJqc6hljyXbdBWQKyAEZkQfUitw",
        "content-type": "application/json",
    }

    response = requests.get(url, headers=headers)
    print(response.text)

    return str(response)


@mcp.tool()
def checkTemperature():
    """Check the temperature of luidgi"""
    url = "http://192.168.1.60:8123/api/states/ssensor.p027_battery_temperature"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI1M2VkMDdmZDhhYzQ0YTI2OGNhMmZjMGY4MmZhMjJlNyIsImlhdCI6MTc0NjgwOTYwNCwiZXhwIjoyMDYyMTY5NjA0fQ.w5FM6otNEJFysqxWUJqc6hljyXbdBWQKyAEZkQfUitw",
        "content-type": "application/json",
    }
    data = {"state": "25", "attributes": {"unit_of_measurement": "°C"}}
    response = requests.post(url, headers=headers, json=data)
    print(response.text)
    return str(response.text)


@mcp.prompt()
def calculator_prompt(a: float, b: float, operation: str) -> str:
    """Prompt for a calculation and return the result."""
    if operation == "add":
        return f"The result of adding {a} and {b} is {add(a, b)}"
    elif operation == "subtract":
        return f"The result of subtracting {b} from {a} is {subtract(a, b)}"
    elif operation == "multiply":
        return f"The result of multiplying {a} and {b} is {multiply(a, b)}"
    elif operation == "divide":
        try:
            return f"The result of dividing {a} by {b} is {divide(a, b)}"
        except ValueError as e:
            return str(e)
    else:
        return "Invalid operation. Please choose add, subtract, multiply, or divide."


# Execute and return the sse output
if __name__ == "__main__":
    mcp.run(transport="sse")


