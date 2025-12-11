# core_app/todo/views.py
from django.core.paginator import Paginator
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from core_app.todo.dataclasses.request.create import TodoCreateRequest
from core_app.todo.dataclasses.request.update import TodoUpdateRequest
from core_app.todo.dataclasses.request.get import TodoGetRequest
from core_app.todo.dataclasses.request.getall import TodoGetAllRequest
from core_app.todo.dataclasses.request.delete import TodoDeleteRequest

from core_app.todo.models import TodoItem
from core_app.todo.utils import success_response_data, error_response_data, add_page_parameter


class TodoView:
    def __init__(self):
        self.data_created = "Todo created successfully"
        self.data_get = "Data fetched successfully"
        self.data_updated = "Todo updated successfully"
        self.data_deleted = "Todo deleted successfully"

    def create_extract(self, params: TodoCreateRequest):
        with transaction.atomic():
            obj = TodoItem.create_item(
                title=params.title,
                description=params.description,
                completed=params.completed,
            )
        resp = TodoItem._to_dict(obj)
        return Response(status=status.HTTP_201_CREATED,
                        data=success_response_data(message=self.data_created, data=resp))

    def get_all_extract(self, params: TodoGetAllRequest):
        page_num = int(getattr(params, "page_num", 1) or 1)
        limit = int(getattr(params, "limit", 50) or 50)
        rows = TodoItem.get_all_items()
        paginator = Paginator(rows, limit)
        if paginator.num_pages == 0:
            final = []
        else:
            if page_num > paginator.num_pages:
                return Response(error_response_data(message="Page number exceeded"), status=status.HTTP_400_BAD_REQUEST)
            page = paginator.page(page_num)
            final = page.object_list
        paginated = add_page_parameter(
            final_data=final,
            page_num=page_num,
            total_page=paginator.num_pages,
            total_count=paginator.count,
            next_page_required=(page_num != paginator.num_pages)
        )
        return Response(status=status.HTTP_200_OK, data=success_response_data(message=self.data_get, data=paginated))

    def get_extract(self, params: TodoGetRequest):
        todo_id = getattr(params, "id", None)
        if todo_id is None:
            return Response(error_response_data(message="todo id is required"), status=status.HTTP_400_BAD_REQUEST)
        t = TodoItem.get_item_by_id(int(todo_id))
        if t is None:
            return Response(error_response_data(message="Not found"), status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK, data=success_response_data(message=self.data_get, data=t))

    def update_extract(self, params: TodoUpdateRequest, todo_id: int = None):
        if todo_id is None:
            return Response(error_response_data(message="todo id is required"), status=status.HTTP_400_BAD_REQUEST)
        updated = TodoItem.update_item(todo_id, title=params.title, description=params.description, completed=params.completed)
        if updated is None:
            return Response(error_response_data(message="Not found"), status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK, data=success_response_data(message=self.data_updated, data=updated))

    def delete_extract(self, params: TodoDeleteRequest):
        ids = getattr(params, "ids", None) or ([getattr(params, "id", None)] if getattr(params, "id", None) else [])
        if not ids:
            return Response(error_response_data(message="id(s) are required"), status=status.HTTP_400_BAD_REQUEST)
        deleted_ids = []
        for tid in ids:
            ok = TodoItem.delete_item(int(tid))
            if ok:
                deleted_ids.append(int(tid))
        if not deleted_ids:
            return Response(error_response_data(message="No matching items to delete"), status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK, data=success_response_data(message=self.data_deleted, data={"deleted_ids": deleted_ids}))
