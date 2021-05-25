import json
import requests


class AuthError(Exception):
    pass


def oauth(sns, access_token):
    if sns == "kakao":
        res = json.loads(
            requests.post("https://kapi.kakao.com/v2/user/me",
                          headers={
                              "Authorization": "Bearer {}".format(access_token)
                          }).text)

        id = res.get('id', None)
        if id == None:
            raise AuthError()

        name = res['kakao_account']['profile']['nickname']
        profile = "./img/profile_no_image.png" if res['kakao_account'][
            'profile']['is_default_image'] else res['kakao_account'][
                'profile']['thumbnail_image_url']

        return {
            "sns_id": "kakao_{}".format(id),
            "name": name,
            "profile": profile
        }
    else:
        raise AuthError()