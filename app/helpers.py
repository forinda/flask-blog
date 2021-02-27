# Helper functions


def get_match(user_id, listIter)->list:
    """ 
        Accepts an id to iterate through
        the posts and pick a match and 
        returns a list
    """
    result = []
    for item in set(listIter):
        if item.author_id == user_id:
            result.append(item)
    return result.reverse()

def get_all_current(listIter)->list:
    """ 
        Accepts an list to iterate through
        the posts and pick a match and 
        returns a list
    """
    result = []
    for item in set(listIter):
            result.append(item)
    return result.reverse()