# common/swagger.py
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class SwaggerUtils:

    @staticmethod
    def create_endpoint(serializer_class, description="Create item"):
        return swagger_auto_schema(
            method='post',
            operation_description=description,
            request_body=serializer_class,
            responses={201: f"{description} successful"}
        )

    @staticmethod
    def get_endpoint(query_params=None, description="Get item"):
        """
        query_params: list of dict with keys: name, type, required, description
        Example: [{"name": "id", "type": openapi.TYPE_INTEGER, "required": True, "description": "Artist ID"}]
        """
        manual_params = []
        if query_params:
            for p in query_params:
                manual_params.append(
                    openapi.Parameter(
                        name=p["name"],
                        in_=openapi.IN_QUERY,
                        description=p.get("description", ""),
                        type=p.get("type", openapi.TYPE_STRING),
                        required=p.get("required", False),
                    )
                )

        return swagger_auto_schema(
            method='get',
            operation_description=description,
            manual_parameters=manual_params,
            responses={200: f"{description} successful"}
        )

    @staticmethod
    def update_endpoint(serializer_class, query_params=None, description="Update item"):
        manual_params = []
        if query_params:
            for p in query_params:
                manual_params.append(
                    openapi.Parameter(
                        name=p["name"],
                        in_=openapi.IN_QUERY,
                        description=p.get("description", ""),
                        type=p.get("type", openapi.TYPE_STRING),
                        required=p.get("required", False),
                    )
                )

        return swagger_auto_schema(
            method='put',
            operation_description=description,
            request_body=serializer_class,
            manual_parameters=manual_params,
            responses={200: f"{description} successful"}
        )

    @staticmethod
    def delete_endpoint(query_params=None, description="Delete item"):
        manual_params = []
        if query_params:
            for p in query_params:
                manual_params.append(
                    openapi.Parameter(
                        name=p["name"],
                        in_=openapi.IN_QUERY,
                        description=p.get("description", ""),
                        type=p.get("type", openapi.TYPE_STRING),
                        required=p.get("required", False),
                    )
                )

        return swagger_auto_schema(
            method='delete',
            operation_description=description,
            manual_parameters=manual_params,
            responses={200: f"{description} successful"}
        )
