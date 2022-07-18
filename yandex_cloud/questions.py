import requests
import json
import pprint
import os


URL_QUESTIONS = "https://netology.ru/backend/admin/api/qna/questions"
URL_QUESTION = "https://netology.ru/frontendadmin/qna/questions/"
URL_SIGN_IN = "https://netology.ru/backend/admin/sign_in"

params = {
    "status": "waiting",
}

data = {
    "admin[email]": os.getenv("ADMIN_EMAIL"),
    "admin[password]": os.getenv("ADMIN_PASS"),
}


def quest():
    ses = requests.Session()
    reg = ses.post(url=URL_SIGN_IN, data=data)

    questions = ses.get(url=URL_QUESTIONS, params=params).json()['questions']

    mess_questions = []
    if len(questions) != 0:
        for _ in questions:
            mess_questions.append(
                f'❓ [{_["title"]}]({URL_QUESTION}{_["id"]})'
            )
        return mess_questions


if __name__ == "__main__":
    print(quest())
