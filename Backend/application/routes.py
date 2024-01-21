# short info
# create question answe pairs
# create scenarios
# Send answers to the questions
from application import app
from flask import render_template, request, jsonify
from application.parser import Parser
from application.chatbot import OpenAIBot

parser = Parser()
bot = OpenAIBot()

@app.route("/getInfo", methods=['POST'])
def get_info():
    # input -> {"data":"blah blah blah"}
    # output -> info json
    try:
        json_data = request.get_json()
        data = json_data.get("data")
        if bot.get_scam_info(data) is None:
            return jsonify({"error":"invalid scam type"}),400
        response = bot.get_scam_info(data)
        response_data = {"info": response}
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/getScenarioQnAnswer", methods=['POST'])
def get_scenario():
    # input -> {"data":"blah blah blah"}
    # output -> scenario and quiz
    try:
        json_data = request.get_json()
        data = json_data.get("data")
        if bot.get_scam_info(data) is None:
            return jsonify({"error":"invalid scam type"}),400
        response, context = bot.pre_user_answer_prompt(data)
        parsed_data = parser.parse_scenario(response)
        counter = 0
        while parsed_data == 0 and counter <3: # try again three times
            response, context = bot.pre_user_answer_prompt(data)
            parsed_data = parser.parse_scenario(response)
            counter +=1 
        if counter == 3:
            return jsonify({"error":"Internal server error"}),400
        parsed_data["answerContext"] = context
        return jsonify(parsed_data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@app.route("/replyUser", methods=['POST'])
def get_reply():
    # input -> user response, correct answer, context
    # output -> ai reply
    try:
        json_data = request.get_json()
        data = json_data.get("data")
        context = json_data.get("context")
        response = bot.post_user_answer_message(data,context)
        response_data = parser.parse_response(response)
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({"error": str(e)})
