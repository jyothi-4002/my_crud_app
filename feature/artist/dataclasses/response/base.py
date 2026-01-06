from dataclasses import asdict

class BaseResponseDataclass:
    def to_dict(self):
        return asdict(self)
