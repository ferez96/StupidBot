# Services related to codeforces rating
from typing import List

from clients import discord_client, codeforces_client
from models.codeforces.rating_change import RatingChange


def get_user_rating(username):
    """get rating from codeforces server by API"""

    # get user rating changes from codeforces
    list_of_rating_changes = codeforces_client.get_user_rating_by_handle(username)
    # calculate rating
    return calc_final_rating(list_of_rating_changes)


def calc_final_rating(list_of_rating_changes: List[RatingChange]):
    """final rating = new_rating of the record with max rating_update_time_seconds"""
    latest_rating = 0
    latest_rating_time = 0
    for rating_change in list_of_rating_changes:
        if rating_change.rating_update_time_seconds > latest_rating_time:
            latest_rating_time = rating_change.rating_update_time_seconds
            latest_rating = rating_change.new_rating
    return latest_rating
