from check_post_content import check_image
from user import return_profile_data
from user_account_score import user_acount_score_calculate


def request_tokens(request):
    profile_data = return_profile_data(request)
    print(profile_data)
    user_score = user_acount_score_calculate(acount_data=profile_data)
    print(user_score)
    post = check_image()
    return {
        "user_score":user_score,
        "post_grade":post[0]
    }
