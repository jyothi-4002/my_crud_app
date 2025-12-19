import urllib
from rest_framework.request import Request


class TodoUtils:

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

    # -------- PAGINATION HELPERS (ONLY FOR GET ALL) -------- #

    @staticmethod
    def extract_params(url: str):
        query = url.split("?")
        if len(query) > 1:
            info = urllib.parse.unquote(query[1])
        else:
            info = "page_num=1"
        return info.split("&"), query[0]

    @staticmethod
    def get_query_params(request: Request):
        params = {}
        try:
            url = request.get_full_path()
        except Exception:
            url = request.path

        query, _ = TodoUtils.extract_params(url)

        for q in query:
            if "=" in q:
                k, v = q.split("=", 1)
            else:
                k, v = q, ""

            # ✅ FIX: convert comma-separated ids into list
            if k == "ids" and isinstance(v, str) and v:
                v = v.split(",")

            params[k] = v

        return params

    @staticmethod
    def add_page_parameter(
        final_data,
        page_num,
        total_page,
        total_count,
        present_url,
        next_page_required=False,
    ):
        response = {
            "data": final_data,
            "presentPage": page_num,
            "totalPage": total_page,
            "totalCount": total_count,
        }

        if next_page_required and total_page > 1:
            if "page_num" in present_url:
                response["nextPageUrl"] = present_url.replace(
                    f"page_num={page_num}", f"page_num={page_num + 1}"
                )
            else:
                if "?" in present_url:
                    response["nextPageUrl"] = present_url + f"&page_num={page_num + 1}"
                else:
                    response["nextPageUrl"] = present_url + f"?page_num={page_num + 1}"

        return response
