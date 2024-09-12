import os
from exa_py import Exa
from langchain.agents import tool

class ToolBox():
    @tool
    def search(query: str):
        """Search for a webpage based on the query. Always check that Action Input is in the format {"query": "my_query"}"""
        return ToolBox._exa().search(f"{query}", use_autoprompt=True, num_results=3)

    @tool
    def find_similar(url: str):
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        Always check that Action Input is in the format {"url": "my_url"}
        """
        return ToolBox._exa().find_similar(url, num_results=3)

    @tool
    def get_contents(urls: str):
        """Get the contents of a webpage.
        The urls must be passed in as a list, a list of urls returned from `search`.
        Always check that Action Input is in the format {"urls": "[urls]"}
        """
        urls = eval(urls)

        contents = str(ToolBox._exa().get_contents(urls))
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)

    @tool
    def write_code(code: str, file_name:str):
        """Write code to file with file_name.  Make sure to input the code and the file name.
        Always check that Action Input is in the format {"code":"code","file_name":"file_name"}
        """
        file = open(file_name,"w")
        file.write(code)
        file.close()

    def web_tools():
        return [
            ToolBox.search,
            ToolBox.find_similar,
            ToolBox.get_contents
        ]

    def write_tools():
        return [
            ToolBox.write_code
        ]

    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))
