from .models import CategoriesOfProducts, GroupsofProducts, Product
from django.db.models import Q



class MultiFiltering:
    def __init__(self, request, queryset):
        self.request = request
        self.queryset = queryset
    def get__atr(self):
        try:
            ans = str(self.request).split('?')[1]
            ans = ans[:-2]
            try:
                if '&' in ans:
                    ans=ans.split('&')
            except:
                pass
            if type(ans) is str:
                ans=ans.split('=')
                ans_dict = {
                    f'{ans[0]}__startswith':ans[1]
                }
            elif type(ans) is list:
                ans_dict = {}
                for i in range(len(ans)):
                    ans_new=ans[i].split('=')
                    if ans_new[0] == 'page':
                        pass
                    ans_dict.update({
                    f'{ans_new[0]}__startswith':ans_new[1]
                    })   
            print(ans_dict)     
            return ans_dict
        except:
            return None
    def get_filtered_queryset(self):
        filter_attr = self.get__atr()
        if filter_attr == None:
            data = {
            'queryset':self.queryset,
            }
            return data
        try:
            error = CategoriesOfProducts.objects.filter(**filter_dict).exists()
            out_queryset = CategoriesOfProducts.objects.filter(**filter_dict)
            if error == False:
                error = str("Nothing search")           
                data = {
                    'queryset':None,
                    'error':error
                }
                return data
            data = {
                    'queryset':out_queryset,
                    'error':None
                }
            return data
        except:
            data = {
                    'queryset':None,
                    'error':"CHECK FIELDS!"
                }
            return data   

