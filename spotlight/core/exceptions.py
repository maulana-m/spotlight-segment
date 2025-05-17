class VideoUrlInvalidError(Exception):
    def __init__(self, msg):
        self.msg = msg


class SubtitleNotFoundError(Exception):
    def __init__(self, msg):
        self.msg = msg
