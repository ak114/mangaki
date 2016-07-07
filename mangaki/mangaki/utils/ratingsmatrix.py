from scipy.sparse import csc_matrix
from mangaki.models import Rating
from mangaki.utils.values import rating_values
import pandas


class RatingsMatrix():
    
    def __init__(self, fname=None):
       self.fname=fname

    def build_matrix(self):
        user_list, item_list, data = [], [], []

        if self.fname is None:
            content = Rating.objects.values_list('user_id',
                                                 'work_id',
                                                 'choice')
            for user_id, item_id, rating in content:
                user_list.append(user_id)
                item_list.append(item_id)
                data.append(rating_values[rating])
        else:
            content = pandas.read_csv(self.fname,
                                      header=None).as_matrix()
            for user_id, item_id, rating in content:
                user_list.append(user_id)
                item_list.append(item_id)
                data.append(rating_values[rating])

        user_set = set(user_list)
        item_set = set(item_list)
        user_dict = {v: k for k, v in enumerate(user_set)}
        item_dict = {v: k for k, v in enumerate(item_set)}
        user_dict_inv = {k: v for k, v in enumerate(user_set)}
        item_dict_inv = {k: v for k, v in enumerate(item_set)}
        row = [user_dict[v] for v in user_list]
        col = [item_dict[v] for v in item_list]
        matrix = csc_matrix((data, (row, col)), shape=(
            len(user_set), len(item_set)))
        self.item_set = item_set
        self.user_set = user_set
        self.item_dict = item_dict
        self.user_dict = user_dict
        self.item_dict_inv = item_dict_inv
        self.user_dict_inv = user_dict_inv
        return matrix