from .models import CategoriesOfProducts, GroupsofProducts, Product




class MultiFiltering:
    def __init__(self, request, queryset):
        self.request = request
        self._out_query = None
        self._error = {}
        self.queryset = queryset
        self.dict_field = self.to_dict()
    def to_dict(self):
        dict_field = {}
        if self.request.query_params:
            _page = self.request.query_params.get('page')
            _per_page = self.request.query_params.get('per_page')
            _id = self.request.query_params.get('id')
            _name = self.request.query_params.get('name')
            _seq = self.request.query_params.get('seq')
            _category_id = self.request.query_params.get('category_id')
            _description = self.request.query_params.get('description')
            _group_id = self.request.query_params.get('group_id')
            _price_more = self.request.query_params.get('price_more')
            _price_less = self.request.query_params.get('price_less')
            _price_equal = self.request.query_params.get('price_equal')
            _sbn = self.request.query_params.get('search_by_name') or False #Search_by_name
            _sbp = self.request.query_params.get('search_by_price') or False #Search_by_price
            dict_field.update({
                'id':_id,
                'name':_name,
                'seq':_seq,
                'category_id':_category_id,
                'description':_description,
                'group_id':_group_id,
                'price_more':_price_more,
                'price_less':_price_less,
                'price_equal':_price_equal,
                'sbn':_sbn,
                'sbp':_sbp,
                'page':_page,
                'per_page':_per_page,
                })
        dict_keys_fields = {
                '0':'id',
                '1':'name',
                '2':'seq',
                '3':'category_id',
                '4':'description',
                '5':'group_id',
                '6':'price_more',
                '7':'price_less',
                '8':'price_equal',
                '9':'sbn',
                '10':'sbp',
                '11':'page',
                '12':'per_page',
        }
        out_dict_field ={}
        out_dict = {}
        out_keys = {}
        for i in range(len(dict_field)):
            key = dict_keys_fields[str(i)]
            if dict_field[key] == None or dict_field[key] == False:
                pass
            else:
                out_keys.update({i:key})
                out_dict.update({key:dict_field[key]})
        out_dict_field.update({'keys':out_keys, 'dict':out_dict})
        return out_dict_field
    
    def get_object(self, method, value, queryset):
        try:
            if method == 'sbn':
                out_queryset = queryset.filter(name=value)
            if method == 'sbp':
                out_queryset = queryset.filter(price=value)
            if method == 'name':
                out_queryset = queryset.filter(name__contains=value)
            if method == 'seq':
                out_queryset = queryset.filter(seq__contains=value)
            if method == 'description':
                out_queryset = queryset.filter(description__contains=value)
            if method == 'category_id':
                out_queryset = queryset.filter(cathegory_id=value)
            if method == 'group_id':
                out_queryset = queryset.filter(group_id=value)
            if method == 'price_more':
                out_queryset = queryset.filter(price__gt=value)
            if method == 'price_less':
                out_queryset = queryset.filter(price__lt=value)
            if method == 'price_equal':
                out_queryset = queryset.filter(price=value)
            if method == 'page':
                out_queryset = queryset
            if method == 'per_page':
                out_queryset = queryset
            return out_queryset
        except Exception as e:
            error = f"error:{e}"
            return error
        
    def get_filtered_queryset(self):
        keys = self.dict_field.get('keys')
        dkeys = list(keys.keys())
        dict = self.dict_field.get('dict')
        querydict = self.queryset
        for i in range(len(keys)):
            method = keys[dkeys[i]]
            value = dict[method]
            if method == 'page' or method == 'per_page':
                pass
            else:
                querydict = (self.get_object(method, value, queryset=querydict))
        error = None    
        delete = []
        if type(querydict) is str:
            error = {"error":querydict}
            data = {
            'queryset':None,
            'error':error
            }
            return data
        if len(querydict)==0 or querydict==None:
            querydict = None
            error={"error":"Not_found"}
        data = {
            'queryset':querydict,
            'error':error
        }
        return data
