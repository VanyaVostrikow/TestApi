from rest_framework.filters import SearchFilter


class MySearch(SearchFilter):
    search_param = "search_by_name"