from .models import CategoriesOfProducts, GroupsofProducts, Product
from django.shortcuts import get_object_or_404
class DeleteCheck:
    def __init__(self):
        pass
    class COPcheck:
        def check_delte(pk):
            print('start')
            model = GroupsofProducts
            print(model.category_id.field)
            try:
                ans = get_object_or_404(model, category_id=pk)
                return True
            except:
                return False
    class GOPcheck:
        def check_delte(pk):
            print('start')
            model = Product
            print(model.group_id.field)
            try:
                ans = get_object_or_404(model, category_id=pk)
                return True
            except:
                return False