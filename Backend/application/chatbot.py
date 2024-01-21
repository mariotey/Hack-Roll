from langchain.chat_models import ChatOpenAI #this is used to generate the chatbot
from langchain.schema import HumanMessage, SystemMessage #SystemMessage to give context, while HumanMessage is the user input
import os

impersonation_scam = """
WHAT IS AN Impersonation Scam?

This scam usually involves a phone call or in-app call (e.g WhatsApp) from someone claiming to be a local government official (e.g. government official, police officer or court official), staff from a bank or telco, or a representative of a Chinese bank or courier company.

Look out for these scam signs:
1. Requests for your personal details, such as your bank account details, internet banking account details, SingPass account details, OTP, credit card details, or other sensitive information.
2. Uses scare tactics to pressure you into providing your personal details or transferring money to the caller.
3. Phone numbers with the '+' prefix, as these are usually not from Singapore
4. Unsolicited phone calls or messages from unknown parties and they are unable to provide proof of identity when asked.

How to stay safe?
1. Don't pick up calls from unknown or numbers with the '+' prefix unless expecting an overseas call.
2. Do not disclose your personal details to anyone without verification. Never share confidential information such as account passwords, OTPs with anyone. Banks and government officials will never ask you for bank transfers, personal details, bank account and credit card details, or OTPs over the phone. 
3. Identify and verify: Hang up immediately if the caller cannot identify themselves properly. Always verify the authenticity of the information or request through official websites, apps, email or call the company's hotline. 
4. Do not click on suspicious URLs in unsolicited emails or text messages. 
5. Stay Calm: Do not act on requests for sensitive and personal information without verification, especially if the request is made out of the blue. If in doubt, ask someone you trust for a second opinion. 
"""

phishing_scam = """
WHAT IS A PHISHING SCAM?

You receive a call, text or email soliciting personal information in order to claim a prize, secure your online accounts or to help investigate fraudulent transactions.

Fake websites are created to look identical to the official sites of organisations or banks, but with a slightly different web address. If you input your personal details, PINs or OTPs in these fake websites, your information and money are at risk of being stolen by criminals.

Look out for these scam signs:
1. Unsolicited phone calls: Be wary of phone calls from anyone claiming you won a lucky draw or prize and then asking you to provide your personal details like bank account details to claim the prize.
2. Unsolicited emails or SMSes: Look out for emails/SMSes threatening account closure, delivery issues and legal issues. Also emails/SMSes offering unbelievable deals like tax rebates, lucky draw prizes or surprise inheritence. Do not click on any links or open any attachments in these emails/SMSes.
3. You are not addressed by your name: Phishing emails are usually sent in bulk and are not personalised.
4. Poor grammar and spelling: Phishing emails are often written in poor English with spelling and grammatical mistakes.

How to stay safe?
1. Don't pick up calls from unknown or numbers with the '+' prefix unless expecting an overseas call.
2. Do not disclose personal particulars, banking and credit card details to anyone without verification. Never share your OTPs with anyone. No government agencies will ask you for your personal details or bank transfers over the phone or through robocalls (automated voice machines). 
3. Hang up immediately if the caller cannot identify themselves properly. Always verify the authenticity of the information or request through official websites, apps, email or call the company's hotline. 
4. Do not click on URLs in unsolicited emails and text messages. Always type the organisation's official web address into your web browser to ensure that you are at the official website. Access your account through the official company's website or app. 
5. Do not share sensitive and personal information without verification. Never share confidential information such as OTPs or passwords with anyone. If in doubt, speak to someone you trust to seek a second opinion. 
6. If available, turn on the two-factor authentication (2FA) for your online accounts for an additional layer of security. 
7. Turn on transaction alerts for your bank accounts and credit cards.
"""

job_scam = """
WHAT IS A JOB SCAM?

You receive an unsolicited job offer via messaging apps, social media, etc. Very often, potential ‘employers’ will offer high pay with very little time commitment or effort. There are a number of different job scams. ‘Affiliate Marketing’ jobs where you are asked to pay for products in advance to boost the sales of sellers in return for commission. 'Agent' jobs require you to process fund transfers using your personal bank account, then transfer the money through online banking or money transfer services such as Western Union or MoneyGram. Applicants for jobs like 'Assistant Purchaser', 'Stock Takers' or 'Trial Participant' may be asked to reveal details like name, identity card number, phone security code or OTPs. This allows the scammers to access your mobile phone to make online purchases. 'Male Social Escort' jobs promise introductions to wealthy female clients, but only after you pay a registration fee. You may also be asked to pay additional fees such as insurance or membership.

Look out for these scam signs:
1. Payment First: No legitimate employer will ask you to pay upfront before starting a job. Scammers may ask victims to open an account through an unverfiied third-party payment platform, or to transfer money to a third-party account. To build credibility, scammers may even pay you a small sum of money first.
2. High Pay, Low Investment: Job offers that promise high returns for minimal effort are likely to be scams.
3. Unsolicited Job Offers: Be wary of job offers that you did not apply for. These often come via social media or messaging apps. Once you express interest, the scammers may show you conversations or testimonials from other 'employees' to convince you that the job is legitimate.
4. Vague Job Descriptions: Scammers may not be able to provide details about the job scope or the company. 
5. Requests for Personal Information: Scammers may ask for your personal information such as your bank account details, SingPass account details, OTP, credit card details, or other sensitive information.
6. Request to transfer money: Do not agree to receive and transfer money on behalf of the company.

How to stay safe?
1. Don't respond to unsolicited job offers: If you receive an unsolicited job offer, always verify the authenticity of the offer with the hiring company through their official channels. You can check the information against the "Recruitment" section on the corporate website or by emailing the HR department. 
2. Don't allow others to use your bank account: Never allow others, including your "employers", to use your bank account to conduct transactions. You may be committing a crime by laundering money for criminals. Money laundering is a serious offence. Offenders may be fined up to $500,000 and imprisoned for 10 years. You are responsible for all the transactions that are carried out on your account. 
3. Don't use unverified apps: Do not download unverified apps from unknown sources to apply for a job.
4. Don't pay to secure a job offer: You should never be asked to pay to secure a job offer.
"""

loan_scam = """
WHAT IS A LOAN SCAM?

If you receive phone calls, unsolicited text messages via SMS, messaging apps or come across advertisements on social media or online offering loans or loan services, you’ve encountered a loan scam. The scammers may claim to be staff from a licensed money lender to gain your trust. You are then instructed to transfer money before the loan can be disbursed. The scammers disappear once the money is transferred. They may also ask for personal information like NRIC and contact numbers, Singpass details and bank account numbers. The information is then used to harass or threaten you for more payments.

Look out for these scam signs:
1. Loan Advertisements: Ads that reach out to you via SMS, messaging apps, social media or online.
2. Fake Websites: Scammers may create fake websites to convince you of their legitimacy. These websites may look similar to the websites of licensed moneylenders.
3. Fees First: They promise instant, fuss-free loan approvals, but ask you to pay a fee before the loan can be disbursed. They may also ask for your personal information like NRIC and contact numbers, Singpass details and bank account numbers.
4. Online Approval: Scammers may offer to approve your loan remotely directly via messaging apps or social media. This is illegal.

How to stay safe?
1. Ignore Loan Advertisements: Ignore any unsolicited loan ads. Licensed moneylenders are not permitted to advertise. Block and report the number or ad on the platform on which the advertisement appeared.
2. Use only legitimate institutions: Seek financial help only from legitimate financial institutions registered with the Registry of Moneylenders at https://rom.mlaw.gov.sg/information-for-borrowers/list-of-licensed-moneylenders-in-Singapore/. Only contact the licensed moneylenders via the contact details found in the registry. Scammers may impersonate licensed moneylenders by using their names, licence numbers and creating fake websites. 
3. Get Approval in Person: Licensed moneylenders are required to meet the borrower at the approved place of business to conduct physical face-to-face ID verification before granting a loan. Approving and disbursing loans online is disallowed. 
"""

investment_scam = """
WHAT IS AN INVESTMENT SCAM?

You receive a message from someone claiming to be stockbrokers or bank or financial company employees on social networking sites like Facebook, WeChat or Line. They ask you to share personal details like NRIC and passport numbers for an investment form. You are then asked to transfer money to banks in Hong Kong and China, pay hefty administrative and security fees, and taxes in order to receive the profits and returns.

You may also receive phone calls from people claiming to be from the Hong Kong Monetary Authority or Hong Kong Overseas Control Centre, asking for a deposit before profits can be released.

In other cases, you may be asked by an online friend to invest in cryptocurrencies, which are highly volatile and unregulated in Singapore.

Look out for these scam signs:
1. Binary Options: Many online trading platforms that offer binary options are fraudulent.
2. High Returns: Scammers promise high returns with little or no risk.
3. Unfamiliar Entities: Look out for unfamiliar platforms or entities based outside of Singapore.

How to stay safe?
1. Do your own checks: Always check with a licensed financial advisor before making any investments, or do a thorough check on the company and its representatives using resources such as the Financial Institution's Directory, Register or Representatives, and Investor Alert List, which can be found on the MAS website (www.mas.gov.sg). 
2. Understand the risks: When investing, always understand what you're investing in. High returns come with high risks. Please note that when dealing with unregulated entities, you will have little recourse if things go wrong. If an entity is based outside of Singapore, check if it is regulated with the respective overseas authority. 
3. Never give out personal information: Never provide your name, identification number, passport details, contact details, bank account or credit card details to anyone you do not know well.
4. Beware stranger danger: Be wary of befriending strangers on social media platforms who promises to make you rich.
"""

online_purchase_scam = """
WHAT IS AN ONLINE PURCHASE SCAM?

An unusually good deal for a gadget, amusement park or concert tickets attracts your attention online. You transfer payment to the ""seller"" who promises delivery of the item. In some cases, the seller demands further payment for duties or delivery charges after the first payment is made. Ultimately, you never receive the item.

In another variant, you may be asked to pay in cash for items that you did not purchase, that are different to what you thought you purchased or are cheap replicas.

Many of these fake sellers may pose as legitimate online sellers on popular marketplaces, create fake websites, or even place advertisements on social media to build credibility.

You only realise you've been scammed after paying for the items in cash.

Look out for these scam signs:
1. Be wary of good deals: If the deal is too good to be true, it probably is. Scammers may also promote popular, sold-out items for above market prices.
2. Lack of information: Scammers often omit product information and/or have unstated terms and conditions.
3. Scammers may try to take the conversation off the platform to avoid detection.
4. Requests payment via direkt bank transfer in return for a discount.
5. Asks for multiple payments: Scammers may also ask for extra payments like admin, delivery or insurance charges.

How to stay safe?
1. Insist on official payment methods or cash-on-delivery: Transact within the platform. Where possible, insist on cash-on-delivery or use the platform's secure payment method. 
2. Choose reputable sellers or platforms for high-value items: Always choose to deal with reputable sellers who have good ratings and reviews and have been with the site for some time. For high-value items, use reputable platforms with consumer protection and return policies. 
3. Check terms and conditions: Always check the terms and conditions and ensure fees are stated upfront.
4. Understand GST and Duty: Additional fees such as GST may be levied on goods that exceed a certain value ($400) for more information visit Singapore Customs: www.customs.gov.sg/individuals/buying-over-the-internet/
"""

scam_types = {
    'impersonation': impersonation_scam,
    'phishing': phishing_scam,
    'job': job_scam,
    'loan': loan_scam,
    'investment': investment_scam,
    'online_purchase': online_purchase_scam
}

class OpenAIBot:
    def __init__(self, scam_types = scam_types, model_name = 'gpt-3.5-turbo-1106', temperature = 0.5):
        self.scam_types = scam_types
        self.openai_key = os.environ.get("SECRET_KEY")
        self.model_name = model_name
        self.temperature = temperature
        self.chat_model = ChatOpenAI(openai_api_key= self.openai_key, model_name = self.model_name, temperature = self.temperature)
        
    
    def get_model(self):
        return self.chat_model
    
    #returns the info section for the scam type - this is also used to create system prompt for chatbot prompts (aka context)
    def get_scam_info(self, scam_type): 
        return self.scam_types[scam_type]

    #sends prompt to openai to generate scenario + quiz + correct option
    #returns the response from openai
    def pre_user_answer_prompt(self, scam_type):
        
        pre_user_answer_message = [
            SystemMessage(
                content = self.get_scam_info(scam_type),
            ),
            HumanMessage(
                content="""
                Generate a SMS conversation between a scammer and a victim. Make the conversation anywhere between 4-10 messages long. Make sure the theme of the conversation is different each time, as this query will be used to generate multiple scenarios.
                Then give us a question and give us 4 possible choices for answers. Only one choice should be correct and the other 3 choices should be wrong. The question should be related to the SMS conversation. 
                Then give us the correct answer to the question.
                Then gives us a detailed explanation of why the correct answer is correct.

                The format should be as follows:

                START
                Scammer: text text text
                Victim: text text text
                Scammer: text text text
                Victim: text text text
                and so on...


                Question: <Insert question here>


                Options:
                A <Insert option A here>
                B <Insert option B here>
                C <Insert option C here>
                D <Insert option D here>


                Correct Option: <Insert correct option here>
                END

                Insert the following: -----------------------------------
                Detailed Explanation: Option <Correct option> is correct because <Insert explanation here>
                """,
            ),
        ]
        
        response = self.chat_model(pre_user_answer_message)
        response = response.dict()
        response = response['content']
        
        response = response.split('-----------------------------------')
        if not len(response) == 2:
            return self.pre_user_answer_prompt(scam_type)
        
        return response[0].strip(), response[1].strip()
    
    #sends prompt to openai to generate response to user answer
    #uses the detailed explanation from the previous prompt as context -> reset back to empty string after this function
    #returns the response from openai
    def post_user_answer_message(self, user_answer,user_answer_context):
        
        post_user_answer_message = [
            SystemMessage(
                content = user_answer_context + ' User Answer was: ' + user_answer,
            ),
            HumanMessage(
                content="""
                Tell the user if they were correct or not. If they were correct, give them a detailed explanation of why they were correct. If they were wrong, give them a detailed explanation of why they were wrong. If there is some merit to their answer, give them a detailed explanation of why their answer is partially correct and partially wrong.

                The format should be as follows:

                START
                Response: <Insert response + Detailed Explanation here>
                END
                """,
            ),
        ]
        
        response = self.chat_model(post_user_answer_message)
        response = response.dict()
        response = response['content']
        
        return response
