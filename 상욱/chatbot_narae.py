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

# 장학관 홈페이지 알림
@chatbot_narae.route("/homepage",methods=['POST')
def homepage():
    res = {
        "version": "2.0",
        "template": {
        "outputs": [
                {
                    "basicCard": {
                        "title": "보물상자",
                        "description": "보물상자 안에는 뭐가 있을까",
                        "thumbnail": {
                            "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                        },
                        "profile": {
                            "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                            "nickname": "보물상자"
                        },
                        "social": {
                            "like": 1238,
                            "comment": 8,
                            "share": 780
                        },
                        "buttons": [
                            {
                                "action": "message",
                                "label": "열어보기",
                                "messageText": "짜잔! 우리가 찾던 보물입니다"
                            },
                            {
                                "action":  "webLink",
                                "label": "구경하기",
                                "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                            }
                        ]
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
                        #"imageUrl": "https://github.com/Hstree-Dongjak-Narae/ChatBot-Narae/blob/main/%EC%83%81%EC%9A%B1/images/introduce.png",
                        "imageUrl": "https://raw.githubusercontent.com/Hstree-Dongjak-Narae/ChatBot-Narae/main/%EC%83%81%EC%9A%B1/images/introduce.png",
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