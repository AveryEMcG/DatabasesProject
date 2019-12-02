def compress_FD(FD):  #Removes repetitions e.g. convert 'ABCBC->ABBB'  to 'BCA->BA'.
    org_FD=FD
    FD=FD.split('->')
    if len(FD)!=2:
        print('Invalid FD. One side is missing!: '+str(org_FD))
        return None
    else:
        LHS=FD[0]
        RHS=FD[1]
        LHS_set=set(list(LHS))
        RHS_set=set(list(RHS))
        LHS_compressed=''.join(LHS_set)
        RHS_compressed=''.join(RHS_set)
        return LHS_compressed+'->'+RHS_compressed

def valid_FD(FD,attrs): #Returns False: if a letter is not among attrs. Returns True: otherwise.
    org_FD=FD
    FD=FD.split('->')
    if len(FD)!=2:
        print('Invalid FD. One side is missing!: '+str(org_FD))
        return False
    else:
        LHS=FD[0]
        RHS=FD[1]
        out_L_letters=[x for x in list(LHS) if x not in attrs]
        out_R_letters=[x for x in list(RHS) if x not in attrs] 
        if out_L_letters!=[] or out_R_letters!=[]:
            print('Invalid FD. Some letters are not among attrs: '+str(org_FD))
            return False
        else:
            print('Valid FD: '+str(org_FD))
            return True
def standard_FD(FD):  #Makes sure if RHS is only one letter! 
    org_FD=FD
    FD=FD.split('->')
    print("The FD is:",FD)
    print("The length of FD is",len(FD))
    if len(FD)!=2:
        print('Invalid FD. One side is missing!: '+str(org_FD))
    else:
        LHS=FD[0]
        RHS=FD[1]
        RHS_list=list(RHS)
        if len(RHS_list)==1:
            return [LHS+'->'+RHS]
        else:
            FD_list_out=[]
            for i in range(len(RHS_list)):
                letter=RHS_list[i]
                FD_list_out.append(LHS+'->'+letter)
            return FD_list_out

def find_trivial_FDs(FD): #Checks if RHS is a member of LHS! 
    org_FD=FD
    FD=FD.split('->')
    if len(FD)!=2:
        print('Invalid FD. One side is missing!: '+str(org_FD))
        return None
    else:
        LHS=FD[0]
        RHS=FD[1]
        if RHS in LHS:
            print('Trivial FD: '+str(org_FD))
            return True
        else:
            print('Non-Trivial FD: '+str(org_FD))
            return False

#-------------------------------------------------------------------------------------------
def define_FDs(attrs_lst):
    print("The attribute list are",attrs_lst)
    var = input("Please enter FDs in a string separated by comma {Format example: 'A->B, D->C'>}. ")
    var="".join(var.split())
    if var[0]=="'":
        var=var[1:]
    if var[-1]=="'":
        var=var[:-1]
    FD_lst=var.split(',')
    print('List of FDs you entered: '+ str(FD_lst))
    print('--------------------------')
    print('Analyzing FDs...')
    revised_FD_list=[]   #List of standard non-trivial FD s. 
    for FD in FD_lst:
        FD=compress_FD(FD)
        if valid_FD(FD,attrs_lst):
            standard_lst=standard_FD(FD)
            print("The standard_lst is:",standard_lst)
            for el in standard_lst:
                if find_trivial_FDs(el)==False:
                    revised_FD_list.append(el)
        else:
            print('Ignore '+FD)
    print('--------------------------')
    FD_dict={}  #Removes repeated FDs and store FDs in a dictionary.
    for FD in revised_FD_list:
        FD=FD.split('->')    
        LHS=FD[0]
        RHS=FD[1]
        key="".join(sorted(LHS))
        if key not in FD_dict.keys():
            FD_dict[key]=[RHS]
        else:
            if RHS not in FD_dict[key]: 
                FD_dict[key].append(RHS)
    print('FDs Dictionary:')
    for key, value_lst in FD_dict.items():
        for value in value_lst:
            print(key+'->'+value)
            #print("The FD dictionary is",FD_dict)
    return FD_dict
if __name__== "__main__":
  define_FDs(['A', 'B','C'])

  #Need to write the code to delete the FDs
