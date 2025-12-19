# core_app/todo/views.py
from django.core.paginator import Paginator
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from feature.todo.models import TodoItem
from feature.todo.utils import TodoUtils

class TodoView:

    def create(self, params):
        with transaction.atomic():
            obj = TodoItem.create_item(**params)
        return Response(
            TodoUtils.success_response_data(
                "Todo created successfully",
                TodoItem.to_response(obj)
            ),
            status=status.HTTP_201_CREATED
        )

    def get(self, params):
        todo_id = params.get("id")
        if not todo_id:
            return Response(
                TodoUtils.error_response_data("todo id is required"),
                status=400
            )

        obj = TodoItem.get_item(int(todo_id))
        if not obj:
            return Response(
                TodoUtils.error_response_data("Not found"),
                status=404
            )

        return Response(
            TodoUtils.success_response_data(
                "Data fetched successfully",
                TodoItem.to_response(obj)
            )
        )

    def get_all(self, params, request):
        page_num = int(params.get("page_num", 1))
        limit = int(params.get("limit", 10))

        qs = TodoItem.get_all_items()
        paginator = Paginator(qs, limit)

        if page_num > paginator.num_pages:
            return Response(
                TodoUtils.error_response_data("Page number exceeded"),
                status=400
            )

        page = paginator.page(page_num)
        data = [TodoItem.to_response(obj) for obj in page.object_list]

        paginated = TodoUtils.add_page_parameter(
            data,
            page_num,
            paginator.num_pages,
            paginator.count,
            request.get_full_path(),
            page_num < paginator.num_pages
        )

        return Response(
            TodoUtils.success_response_data(
                "Data fetched successfully",
                paginated
            )
        )

    def update(self, params):
        todo_id = params.get("id")
        if not todo_id:
            return Response(
                TodoUtils.error_response_data("todo id is required"),
                status=400
            )

        obj = TodoItem.get_item(int(todo_id))
        if not obj:
            return Response(
                TodoUtils.error_response_data("Not found"),
                status=404
            )

        for field in ["title", "description", "completed"]:
            if field in params:
                setattr(obj, field, params[field])

        obj.save()

        return Response(
            TodoUtils.success_response_data(
                "Todo updated successfully",
                TodoItem.to_response(obj)
            )
        )

    def delete(self, params):
        ids = params.get("ids")

        deleted_ids = []
        for todo_id in ids:
            if TodoItem.delete_item(todo_id):
                deleted_ids.append(todo_id)

        return Response(
            TodoUtils.success_response_data(
                "Todo(s) deleted successfully",
                {"deleted_ids": deleted_ids}
            ),
            status=200
        )