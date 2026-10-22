"""MCP starter. Business tools fail explicitly until verified implementation."""
from mcp.server.fastmcp import FastMCP
from gib_mcp.discovery import TARGET

mcp = FastMCP("gib-ozelge")

@mcp.tool()
def gib_status() -> dict:
    """Report implementation status and the official source."""
    return {"status": "scaffold", "source_url": TARGET,
            "search_ready": False, "detail_ready": False,
            "next_step": "Run gib-discover and follow docs/ROADMAP.md."}

@mcp.tool()
def search_ozelge(query: str, page: int = 1, page_size: int = 10) -> dict:
    """Search contract; live adapter is not implemented yet."""
    if not query.strip() or len(query) > 300:
        raise ValueError("query must contain 1–300 nonblank characters")
    if page < 1 or not 1 <= page_size <= 20:
        raise ValueError("page >= 1; page_size between 1 and 20 required")
    raise RuntimeError("DISCOVERY_REQUIRED: Live search adapter is not verified. No results were fetched.")

@mcp.tool()
def get_ozelge(document_id: str) -> dict:
    """Detail contract; use a source ID returned by verified search."""
    if not document_id.strip() or len(document_id) > 500:
        raise ValueError("Invalid document ID")
    raise RuntimeError("DISCOVERY_REQUIRED: Live detail adapter is not verified.")

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
