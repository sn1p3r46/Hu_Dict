import os

_data = "data"
_file_name = "dict.csv"

_abs_path = os.path.abspath(os.path.dirname(__file__))
_data_abs_path = os.path.join(_abs_path,_data)


def write_dictionary(my_dic):
    if not os.path.isdir(_data_abs_path):
        os.makedirs(_data_abs_path)
    try:
        with open(os.path.join(_data_abs_path,_file_name), 'w') as out_f:
            for key, value in my_dic.items():
                out_f.write("{} {}\n".format(key, value))
    
        return True

    except:

        return False 


def load_dictionary():
    if not os.path.isdir(_data_abs_path):
        return False
    if not os.path.exists(os.path.join(_data_abs_path,_file_name)):
        return False

    with open(os.path.join(_data_abs_path,_file_name),'r') as in_f:

        hu_en_dic = {}
        en_hu_dic = {}

        for line in in_f:
            hu, en = line.strip().split(" ")
            hu_en_dic[hu] = en
            en_hu_dic[en] = hu

    return (hu_en_dic, en_hu_dic)
        
