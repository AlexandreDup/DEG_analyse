import os

def Save_in_file(name_organism, list_gene, communs):
    if not os.path.exists("Pan-genome_folder/"):
        os.makedirs("Pan-genome_folder/")
    f = open("Pan-genome_folder/" + str(name_organism)+".txt", 'w')
    title = "For the sample(s) :" + str(name_organism) + "\n"
    if communs is False:
        title += "this sample is the only one how have" + "\n"
    else:
        title += "these samples have in communs :" +"\n"
    f.write(title)
    for gene in list_gene:
        f.write("- "+gene)
        f.write("\n")

    f.close()



def difference_between_two_list(list1, list2):
    list_difference = list(set(list1) - set(list2))
    return list_difference

def same_between_two_list(list1, list2):
    list_similarities = list(set(list1).intersection(list2))
    return list_similarities

def get_unique(list_de_list, name_list):

    for i in range(len(list_de_list)):
        current_list = list_de_list[i]
        list_difference = current_list
        for y in range(len(list_de_list)):
            if i != y:
                list_difference = difference_between_two_list(list_difference, list_de_list[y])
        if len(list_difference) > 0:
            #print("la list :", name_list[i], "est la seul a possédé", list_difference)
            Save_in_file(name_list[i], list_difference, False)

def get_communs_two(list_de_list, name_list):
    for x in range(len(list_de_list)):
        current_list_1 = list_de_list[x]
        for y in range(len(list_de_list)):
            if x < y:
                current_list_2 = list_de_list[y]
                commun_list = list(set(current_list_1).intersection(current_list_2))
                for z in range(len(list_de_list)):
                    if z < x and z < y:
                        commun_list = same_between_two_list(commun_list, list_de_list[z])
                if len(commun_list)>0:
                    #print("les listes :", name_list[x], "et", name_list[y], " sont les seuls à possèder", list(commun_list))
                    Save_in_file([name_list[x],name_list[y]], commun_list, True)

def get_communs_to_all(list_de_list, name_list):
    list_communs = list_de_list[0]
    for list_sample in list_de_list:
        list_communs = set(list_communs).intersection(list_sample)
    list_communs=list(list_communs)
    if len(list_communs)>0:
        #print("les listes", str(name_list) , "ont en communs : ", list_communs)
        Save_in_file(name_list, list_communs, True)



def run_verbosity(list_de_list, name_list, Core_Unique):

    if Core_Unique is False:
        get_unique(list_de_list, name_list)

    else:
        get_communs_to_all(list_de_list, name_list)
