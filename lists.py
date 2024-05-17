# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
   if len(list_to_remove_elements)>0:
        del list_to_remove_elements[0]
        if len(list_to_remove_elements)>=4:
            del list_to_remove_elements[3]
        if len(list_to_remove_elements)>=4:
            del list_to_remove_elements[3]
        return list_to_remove_elements
    else:
        return "Error"

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements


def is_empty(list_to_check):
    if list_to_check== []:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>2 and len(list_to_compare2)>2:
        if list_to_compare1[2]== list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify)>2:
        if len(list_of_lists_to_modify[0])>=1:
            p1=list_of_lists_to_modify[0][0:2]
        else:
            p1=[]
        if len(list_of_lists_to_modify[1])>=2:
            p2=list_of_lists_to_modify[1][1:4]
        else:
            p2=[]
        if len(list_of_lists_to_modify[2])>=1:
            p3=list_of_lists_to_modify[2][-2:]
        else:
            p3=[]
        return [p1, p2, p3]
