# common/utils.py

import urllib
from rest_framework.request import Request


class CommonUtils:
    # ---------- COMMON RESPONSE HELPERS ---------- #

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

    # ---------- QUERY PARAM HELPERS ---------- #

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
        query, _ = CommonUtils.extract_params(url)

        for q in query:
            if "=" in q:
                k, v = q.split("=", 1)
            else:
                k, v = q, ""

            # handle ids=1,2,3
            if k == "ids" and v:
                v = v.split(",")

            params[k] = v

        return params

    # ---------- PAGINATION (USED BY TODO & MUSIC) ---------- #

    @staticmethod
    def add_page_parameter(
        data,
        page,
        total_page,
        total_count,
        present_url,
        has_next=False,
    ):
        response = {
            "data": data,
            "presentPage": page,
            "totalPage": total_page,
            "totalCount": total_count,
        }

        if has_next and total_page > page:
            if "page_num=" in present_url:
                response["nextPageUrl"] = present_url.replace(
                    f"page_num={page}", f"page_num={page + 1}"
                )
            else:
                sep = "&" if "?" in present_url else "?"
                response["nextPageUrl"] = f"{present_url}{sep}page_num={page + 1}"

        return response
