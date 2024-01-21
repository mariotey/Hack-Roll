import re

class Parser():
    def parse_summary(self,input_str):
        pattern = r'Start\nSummary: (.+?)\nEnd'
        match = re.search(pattern, input_str, re.DOTALL)
        if match:
            return {"info": match.group(1)}

    
    def parse_scenario(self, input_str):
        pattern = r'START\n(.*?)\nQuestion: (.+?)\nOptions:\n(.+?)\nCorrect Option: (.+?)\n'
        match = re.search(pattern, input_str, re.DOTALL)
        
        if match:
            users_data = match.group(1).strip().split('\n')
            users_data = [i for i in users_data if ":" in i]
            scenario_list = [
                {"name": line.split(":")[0].strip(), "content": line.split(":", 1)[1].strip()} for line in users_data
            ]
            question = match.group(2)

            options = match.group(3).split('\n')
            #answers = []
            #answers_dict = {f"option{i+1}": option.strip() for i, option in enumerate(options)}

            correct_option = match.group(4)
            #correct_option = correct_option[0]
            return {
                "scenario": scenario_list,
                "question": question,
                "answers": options[:4],
                "correct": correct_option
            }
        else:
            raise ValueError("Pattern not found in input string.")


    def parse_response(self, input_str):
        pattern = r'START\nResponse: (.+?)\nEND'
        match = re.search(pattern, input_str, re.DOTALL)
        
        if match:
            return {"answer": match.group(1)}
        else:
            raise ValueError("Pattern not found in input string.")



input_str = """
Start
Summary: Phishing scams are bad
End
"""

input_str2 = """
START
Scammer: Hi, this is Officer Tan from the Singapore Police Force. We have detected fraudulent activity on your bank account. Please provide your bank account details for verification.
Victim: Oh no, that's concerning. But I'm not comfortable sharing my details over the phone. Can you provide me with a case number so I can verify with the police station?

bwehwfhbcfejswd

Scammer: I understand your concern, but this is an urgent matter. We need your cooperation to resolve this issue. Please provide the details as soon as possible.
Victim: I will not proceed without proper verification. I'll visit the police station in person to clarify this matter.

Question: What should the victim do when receiving such a call?

Options:
A. Provide the bank account details immediately.
B. Request for a case number and verify with the police station.
C. Ignore the call and do nothing about it.
D. Transfer a small amount of money to the provided account for verification purposes.

Correct Option: B. Request for a case number and verify with the police station.
END
"""

input_str3 = """
START
Response: Your answer is correct!
END
"""

parser = Parser()
#info_dict = parser.parse_summary(input_str)
scenario_dict = parser.parse_scenario(input_str2)
#response_dict = parser.parse_response(input_str3)

#print(info_dict)
print(scenario_dict)
#print(response_dict)
