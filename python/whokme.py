#!/usr/bin/python

# show_objs.py
def who_kick_me():
    import gc

    total_list_len = 0
    total_tuple_len = 0
    total_dict_len = 0
    len_max = 0
    max_list = None
    cnts = {}
    objs = gc.get_objects()
    for obj in objs:
        tp = type(obj)
        if tp == list:
            total_list_len = total_list_len + len(obj)
            if len(obj) > len_max:
                len_max = len(obj)
                max_list = obj
                pass
            pass
        elif tp == tuple:
            total_tuple_len = total_tuple_len + len(obj)
        elif tp == dict:
            total_dict_len = total_dict_len + len(obj)
            pass
        cnts[tp] = cnts.setdefault(tp, 0) + 1
        pass
    all_cnts = cnts.items()
    all_cnts.sort(key=lambda x: x[1], reverse=True)
    for tp, cnt in all_cnts:
        if tp == list:
            print '%d %s (total %d/%d)' % (cnt, repr(tp), total_list_len,
                                                         len_max)
        elif tp == tuple:
            print '%d %s (total %d)' % (cnt, repr(tp), total_tuple_len)
        elif tp == dict:
            print '%d %s (total %d)' % (cnt, repr(tp), total_dict_len)
        else:
            print '%d %s' % (cnt, repr(tp))
            pass
        pass
    print max_list
    pass

