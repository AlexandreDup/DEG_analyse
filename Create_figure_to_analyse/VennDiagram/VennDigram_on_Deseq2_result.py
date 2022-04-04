"""
This script get DESeq2 output as input and give the VennDiagram of them.
the DESeq2 output have to be filtered on p_adj <0.05

"""


# library
import matplotlib.pyplot as plt
from venn import *
from Verbosity import *
from datetime import datetime


def read(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return lines

def get_gene_names(file):
    list_gene = []
    for line in file:
        line = line.split("\t")
        print(line[0])
        list_gene.append(line[0])
    return list_gene

def Run_Program(list_input_file, list_name, Verbosity):

    # run program
    #create the dictionnary of the venn diagram (organism : {gene1, gene2})
    list_gene = []
    for file in list_input_file:
        list_gene.append(set(get_gene_names(read(file))))
    VennDictionnary = dict(zip(list_name, list_gene))

    #draw the venn diagram (with spécific size and font size)
    venn(VennDictionnary, figsize=(15, 15), fontsize=20)

    #create a name (with date) for the picture of the venn diagram
    img_title = 'figure_'
    for name in list_name:
        img_title+= str(name) + "_"
    now = datetime.now()
    img_title += "figure_" + now.strftime("%m_%d_%Y_%H_%M_%S")

    #save and show the picture (with a specific dpi (dot per inch)
    plt.savefig(img_title, dpi=300)
    plt.show()

    #create the output file containing the core or the unique genome.
    run_verbosity(list_gene, list_name, Verbosity)

if __name__ == '__main__':

    #input data
    input1_DESeq2 = "Galaxy133-[DESeq2_result_file_on_data_30,_data_129,_and_others].tabular"
    name_grpA = "DEG"

    input2_DESeq2 = "Galaxy136-[Filter_on_data_110].tabular"
    name_grpB = "Controle"

    input3_DESeq2 = "Galaxy137-[Filter_on_data_111].tabular"
    name_grpC = "Secheresse"

    #input data
    #input2_DESeq2 = "DEG's/DDM1/salmon/local/Galaxy148-[DESeq2_result_file_on_data_1,_data_141,_and_others].tabular"
    #name_grpB = "DDM1"

    #input2_DESeq2 = "DEG's/DDM1/salmon/mean/Galaxy145-[DESeq2_result_file_on_data_1,_data_141,_and_others].tabular"
    #name_grpB = "DDM1"

    #input2_DESeq2 = "DEG's/DDM1/salmon/parametric/Galaxy142-[DESeq2_result_file_on_data_1,_data_141,_and_others].tabular"
    #name_grpB = "DDM1"

    #Adapt to your data
    list_name = [name_grpA, name_grpB,name_grpC]
    list_input = [input1_DESeq2, input2_DESeq2, input3_DESeq2]

    #Run Program
    Verbosity = True #or False
    Run_Program(list_input, list_name,Verbosity)

    #ctrl_C_ctrl_S, Ctrl_C_KD_C_transcript, ctrl_C_OX_C_gene, ctrl_C_OX_C_transcript, Ctrl_ddm1_S_transcript, ctrl_KD_C_gene, Ctrl_S_KD_S_transcript, ctrl_S_OX_S_gene, ctrl_S_OX_S_transcript, KD_C_KD_S_gene, KD_C_KD_S_transcript, OX_C_OX_S_gene, OX_C_OX_S_transcript