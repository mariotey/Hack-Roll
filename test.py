import requests
import json

# bot_url="https://hacknrollllm.onrender.com"

# headers = {"Content-Type": "application/json"}

# scenario_info = json.loads(
#         requests.post(f'{bot_url}/replyUser',
#                         headers=headers,
#                         json = {
#                             "data": "impersonation",
#                             "context":'Detailed Explanation: Option B is correct because the victim should hang up the call and report it to the police. It is important not to provide any personal information to unknown callers and to verify the authenticity of the call before taking any action.'
#                         }
#         ).content.decode("utf-8")
#     )

# print(scenario_info)

#################################################################################################

json_str = "{'info': \"\nWHAT IS A PHISHING SCAM?\n\nYou receive a call, text or email soliciting personal information in order to claim a prize, secure your online accounts or to help investigate fraudulent transactions.\n\nFake websites are created to look identical to the official sites of organisations or banks, but with a slightly different web address. If you input your personal details, PINs or OTPs in these fake websites, your information and money are at risk of being stolen by criminals.\n\nLook out for these scam signs:\n1. Unsolicited phone calls: Be wary of phone calls from anyone claiming you won a lucky draw or prize and then asking you to provide your personal details like bank account details to claim the prize.\n2. Unsolicited emails or SMSes: Look out for emails/SMSes threatening account closure, delivery issues and legal issues. Also emails/SMSes offering unbelievable deals like tax rebates, lucky draw prizes or surprise inheritence. Do not click on any links or open any attachments in these emails/SMSes.\n3. You are not addressed by your name: Phishing emails are usually sent in bulk and are not personalised.\n4. Poor grammar and spelling: Phishing emails are often written in poor English with spelling and grammatical mistakes.\n\nHow to stay safe?\n1. Don't pick up calls from unknown or numbers with the '+' prefix unless expecting an overseas call.\n2. Do not disclose personal particulars, banking and credit card details to anyone without verification. Never share your OTPs with anyone. No government agencies will ask you for your personal details or bank transfers over the phone or through robocalls (automated voice machines). \n3. Hang up immediately if the caller cannot identify themselves properly. Always verify the authenticity of the information or request through official websites, apps, email or call the company's hotline. \n4. Do not click on URLs in unsolicited emails and text messages. Always s into your web browser to ensure that you are at the official website. Access your account through the official company's website or app. \n5. Do not share sensitive and personal information without verification. Never share confidential information such as OTPs or passwords with anyone. If in doubt, speak to someone you trust to seek a second opinion. \n6. If available, turn on the two-factor authentication (2FA) for your online accounts for an additional layer of security. \n7. Turn on transaction alerts for your bank accounts and credit cards.\n"}"

modified_str=json_str.replace("'",'"')

print("Complete")