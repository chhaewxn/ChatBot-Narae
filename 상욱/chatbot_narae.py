# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify

chatbot_narae = Flask(__name__)


@chatbot_narae.route("/")
def start():
    return "Hello goorm!"


# 화성시장학관 동작나래관 사생용 챗봇 스킬

# 식사 시간
@chatbot_narae.route("/Meal_Time",methods=['POST'])
def Meal_Time():
    
    textstr = "화성시장학관 동작나래관의 식사시간 입니다.\n"
    textstr += "평일\n"
    textstr += "아침: 7:00-8:30\n"
    textstr += "점심: 11:40-13:00\n"
    textstr += "저녁: 18:00-19:30\n"
    textstr += "주말\n"
    textstr += "아침: 8:00-9:00\n"
    textstr += "점심: 12:00-13:00\n"
    textstr += "저녁: 18:00-19:30\n"

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": textstr
                    }
                }
            ]
        }
    }

    return jsonify(res)

# 화성시장학관 동작나래관 외부인용 챗봇 스킬

# 장학관 소개
@chatbot_narae.route("/introduce",methods=['POST'])
def introduce():

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "https://github.com/Hstree-Dongjak-Narae/ChatBot-Narae/blob/main/%EC%83%81%EC%9A%B1/images/introduce.png",
                        #"imageUrl": "https://github.com/Hstree-Dongjak-Narae/ChatBot-Narae/blob/main/%EC%83%81%EC%9A%B1/images/introduce.png?raw=true",
                        "altText": "장학관 소개"
                    }
                }
            ]
        }
    }

    return jsonify(res)

if __name__ == "__main__":
    #chatbot_narae.run(host='0.0.0.0', port=5001, threaded=True)
    chatbot_narae.run(host='10.128.0.2', port=5001, threaded=True)