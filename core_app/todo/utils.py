def success_response_data(message: str = "Success", data=None):
    return {
        "message": message,
        "data": data
    }

def error_response_data(message: str = "Error", errors=None):
    return {
        "message": message,
        "errors": errors
    }

def add_page_parameter(final_data, page_num, total_page, total_count, next_page_required=False):
    return {
        "results": final_data,
        "page_num": page_num,
        "total_page": total_page,
        "total_count": total_count,
        "next_page_required": next_page_required,
    }
