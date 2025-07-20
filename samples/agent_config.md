# Agent Configuration Summary

**Model**: Mistral via Ollama  
**Framework**: LangChain (ZeroShotAgent)  
**Streaming Enabled**: ✅  
**Memory**: ConversationBufferMemory  
**Agent Type**: `ZERO_SHOT_REACT_DESCRIPTION`  
**Handle Parsing Errors**: ✅ `True`  
**Max Iterations**: ✅ `6`  

## Tools Used
| Name              | Purpose                                                   |
|-------------------|-----------------------------------------------------------|
| Current Date Tool | Returns current system date (YYYY-MM-DD)                  |
| Current Time Tool | Returns current system time (HH:MM:SS)                    |
| File Reader Tool  | Reads contents of `sample_data.txt` for emergency info    |

## Prompt Prefix
```text
You can use the following tools:
- Current Date Tool: returns today's system date.
- Current Time Tool: returns current system time.
- File Reader Tool: reads contents of sample_data.txt. This exists in the backend folder.

Format your reasoning exactly like this:
Thought: I need the current date.
Action: Current Date Tool
Action Input: ''
Observation: 2025-07-20
...
Final Answer: [your summary here]
```

## Input text entered in the UI
```text
Using today’s date, current time, and sample_data.txt, provide a short checklist for 3 family emergencies. Respond in under 100 words and conclude with Final Answer.
```