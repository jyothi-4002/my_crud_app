# feature/artist/utils.py

import urllib
from rest_framework.request import Request

class ArtistUtils:  # <-- renamed from CommonUtils
    @staticmethod
    def success_response_data(message=None, data=None):
        if message is None and data is None:
            return {"status": True}
        if message is None:
            return {"status": True, "data": data}
        if data is None:
            return {"status": True, "message": message}
        return {"status": True, "message": message, "data": data}

    @staticmethod
    def error_response_data(message, error=None):
        return {"status": False, "message": message, "error": error}

    @staticmethod
    def extract_params(url: str):
        query = url.split("?", 1)
        if len(query) > 1:
            return urllib.parse.unquote(query[1]).split("&"), query[0]
        return [], query[0]

    @staticmethod
    def get_query_params(request: Request):
        try:
            url = request.get_full_path()
        except Exception:
            url = request.path

        params = {}
        query, _ = ArtistUtils.extract_params(url)

        for q in query:
            if "=" in q:
                k, v = q.split("=", 1)
                if k == "ids":
                    v = v.split(",")
                params[k] = v

        return params
