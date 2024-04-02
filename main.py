from flask import Flask,request
from flask_cors import CORS , cross_origin

from check_post_content import check_image
from posts import add_post, get_user_post, get_user_eligible_post, add_comment
from request import request_tokens
from user import get_profile_data
from user_account_score import user_acount_score_calculate

app = Flask(__name__)
CORS(app , resources={r"/":{"origins":"*"}})

@app.route("/")
def main():
    return "hello world"

@app.route("/home")
@cross_origin()
def home():
    return "First Page"

@app.route("/v1/prediction", methods=["POST"])
@cross_origin()
def image_upload_undefined():
    uploaded_file = request.files['image']
    body = request.form.to_dict(flat=False)
    print(body)
    if uploaded_file:
        uploaded_file.save('uploaded.png')
        try:
            response_post = check_image()
            response_score = user_acount_score_calculate(acount_data=body)
            return {
                "post":response_post,
                "score":response_score
            }
        except:
            return {
                "message": "Error",
                "state": False
            }

@app.route("/v1/request_token", methods=["POST"])
@cross_origin()
def request_():
    return request_tokens(request)

@app.route("/v1/post", methods=["POST"])
@cross_origin()
def add_post_():
    return add_post(request=request)

@app.route("/v1/user_profile", methods=["GET"])
@cross_origin()
def user_profile():
    return get_profile_data(request=request)

@app.route("/v1/user_posts", methods=["GET"])
@cross_origin()
def user_post():
    return get_user_post(request=request)

@app.route("/v1/user_eligible_posts", methods=["GET"])
@cross_origin()
def user_eligible_post():
    return get_user_eligible_post(request=request)

@app.route("/v1/comment/<post_id>", methods=["PUT"])
@cross_origin()
def comment(post_id):
    return add_comment(request=request , post_id=post_id)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
