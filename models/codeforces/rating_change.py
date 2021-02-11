class RatingChange(object):
    # contestId
    # contestName
    # handle
    # rank
    # ratingUpdateTimeSeconds
    # oldRating
    # newRating

    def __init__(self, contest_id, contest_name, handle, rank, rating_update_time_seconds, old_rating, new_rating):
        self.contest_id = contest_id
        self.contest_name = contest_name
        self.handle = handle
        self.rank = rank
        self.rating_update_time_seconds = rating_update_time_seconds
        self.old_rating = old_rating
        self.new_rating = new_rating
