import requests
import json

bot_url="https://hacknrollllm.onrender.com"

headers = {"Content-Type": "application/json"}

scenario_info = json.loads(
        requests.post(f'{bot_url}/replyUser',
                        headers=headers,
                        json = {
                            "data": "impersonation",
                            "context":'Detailed Explanation: Option B is correct because the victim should hang up the call and report it to the police. It is important not to provide any personal information to unknown callers and to verify the authenticity of the call before taking any action.'
                        }
        ).content.decode("utf-8")
    )

print(scenario_info)