from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_query_param = 'sayfa'
    page_size = 10


class CustomLimitOffsetPagination(LimitOffsetPagination):
    limit_query_param = 'adet'
    offset_query_param = 'baslagic'
    default_limit = 10

class CustomCursorPagination(CursorPagination):
    cursor_query_param = 'imlec'
    page_size = 10
    page_size_query_param = 'sayfa_boyutu'
    ordering = '-id'
