"""Verify the real stdio transport and explicit scaffold status."""
import asyncio
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    root = Path(__file__).resolve().parent.parent
    params = StdioServerParameters(command='/bin/sh', args=[str(root / 'scripts/serve.sh')])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            assert {'gib_status', 'search_ozelge', 'get_ozelge'} <= {t.name for t in tools.tools}
            status = await session.call_tool('gib_status', {})
            assert not status.isError
            result = await session.call_tool('search_ozelge', {'query': 'KDV'})
            assert result.isError, 'Unimplemented search must explicitly fail'
            print('PASS: initialize, list_tools, gib_status, explicit search error')

if __name__ == '__main__':
    asyncio.run(main())
