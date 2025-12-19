import urllib
from rest_framework.request import Request


class MusicUtils:

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
        query, _ = MusicUtils.extract_params(url)

        for q in query:
            if "=" in q:
                k, v = q.split("=", 1)
                params[k] = v

        return params

    @staticmethod
    def add_page_parameter(data, page, total_page, total_count, present_url, has_next):
        response = {
            "data": data,
            "presentPage": page,
            "totalPage": total_page,
            "totalCount": total_count,
        }

        if has_next:
            if "page_num=" in present_url:
                response["nextPageUrl"] = present_url.replace(
                    f"page_num={page}", f"page_num={page + 1}"
                )
            else:
                sep = "&" if "?" in present_url else "?"
                response["nextPageUrl"] = f"{present_url}{sep}page_num={page + 1}"

        return response
