from langchain.tools import Tool
from datetime import datetime

def get_current_date(input: str = ""):
    return datetime.now().strftime("%Y-%m-%d")

def get_current_time(input: str = ""):
    return datetime.now().strftime("%H:%M:%S")

def read_sample_file(input: str = ""):
    try:
        with open("sample_data.txt", "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

date_tool = Tool(
    name="Current Date Tool",
    func=get_current_date,
    description="Returns the current system date in YYYY-MM-DD format"
)

time_tool = Tool(
    name="Current Time Tool",
    func=get_current_time,
    description="Returns the current system time in HH:MM:SS format"
)

file_tool = Tool(
    name="File Reader Tool",
    func=read_sample_file,
    description="Reads contents of sample_data.txt and returns them"
)

tools = [date_tool, time_tool, file_tool]