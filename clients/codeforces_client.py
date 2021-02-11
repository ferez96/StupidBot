import requests
import marshmallow as ma
import marshmallow.fields as f
from marshmallow import post_load

from models.codeforces.rating_change import RatingChange


class RatingChangeSchema(ma.Schema):
    contestId = f.Integer()
    contestName = f.String()
    handle = f.String()
    rank = f.Integer()
    ratingUpdateTimeSeconds = f.Integer()
    oldRating = f.Integer()
    newRating = f.Integer()

    @post_load
    def to_object(self, data, **kwargs):
        """transform json data to model object"""
        return RatingChange(
            contest_id=data["contestId"],
            contest_name=data["contestName"],
            handle=data["handle"],
            rank=data["rank"],
            rating_update_time_seconds=data["ratingUpdateTimeSeconds"],
            old_rating=data["oldRating"],
            new_rating=data["newRating"]
        )


class GetUserRatingSchema(ma.Schema):
    status = f.String()
    result = f.List(f.Nested(RatingChangeSchema), required=True)


# https://codeforces.com/api/user.rating?handle=Fefer_Ivan
def get_user_rating_by_handle(handle):
    HOST = "https://codeforces.com"
    URL = "api/user.rating"
    params = {
        "handle": handle
    }

    resp = requests.get(HOST + "/" + URL, params=params)
    if resp.status_code == 200:
        raw_data = resp.json()
        # TODO: try-catch
        data = GetUserRatingSchema().load(raw_data)  # this can raise exception when schema load fail
        print(f"Success get {len(data.get('result'))} rating changes")
        return data.get("result")
    else:
        raise Exception("[Codeforces Client] can not get user rating by handle")
