from mcp.server.fastmcp import FastMCP
from dates import Date

mcp = FastMCP("dates_server")

@mcp.tool()
async def get_current_date() -> Date:
  """Get the current date.
  
  Args: none.
  
  """
  return Date.get()


if __name__ == "__main__":
  mcp.run(transport="stdio")