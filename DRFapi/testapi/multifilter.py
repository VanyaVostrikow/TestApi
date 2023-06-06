from .models import CategoriesOfProducts, GroupsofProducts, Product
from django.db.models import Q

class MultiFiltering:
    def __init__(self, request, queryset):
        self.request = request
        self.queryset = queryset
    def __del_page(self, params):
        if type(params) == str:
            if 'page' in params or \
                'search' in params:
                return None
            else:
                return params
        elif type(params) ==  list:
            out = []
            for i in range(len(params)):
                if  params[i].startswith('page') or \
                    params[i].startswith('per_page') or \
                    params[i].startswith('search'):
                    continue
                else:
                    out.append(params[i])
            return out

    def get__atr(self):
            try:
                ans = str(self.request).split('?')[1][:-2]
                try:
                    if '&' in ans:
                        ans=ans.split('&')
                except:
                    pass
                ans = self.__del_page(ans)
                if type(ans) is str:
                    ans=ans.split('=')
                    ans_dict = {
                        f'{ans[0]}__startswith':ans[1]
                    }
                elif type(ans) is list:
                    ans_dict = {}
                    for i in range(len(ans)):
                        ans_new=ans[i].split('=')
                        ans_dict.update({
                        f'{ans_new[0]}__startswith':ans_new[1]
                        })   
                elif ans == None:
                    return None
                return ans_dict
            except:
                return None

    def get_filtered_queryset(self):
        filter_dict = self.get__atr()
        if filter_dict == None:
            data = {
            'queryset':self.queryset,
            }
            return data
        try:
            error = self.queryset.filter(**filter_dict).exists()
            out_queryset = self.queryset.filter(**filter_dict)
            if error == False:          
                data = {
                    'queryset':None,
                    'error':str("404-Not-Found") 
                }
                return data
            data = {
                    'queryset':out_queryset,
                }
            return data
        except:
            data = {
                    'queryset':None,
                    'error':"CHECK FIELDS!"
                }
            return data   

