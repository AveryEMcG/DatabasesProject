class MVD:
    def trivial_MVD(self, FD_dict, MVD, num_attrs):  # MVD format: A->->B
        if num_attrs <= 2:
            return True
        else:
            MVD = MVD.split('->->')
            key = MVD[0]
            value = MVD[1]
            if key in FD_dict:
                if FD_dict[key] == value or value in FD_dict[key]:
                    return True
                else:
                    return False
            else:
                return False

    # -------------------------------------------------------------------------------------------
    def define_MVDs(self,FD_dict,attrs_lst,num_attrs):
        print("The FD Dict in MVD is:",FD_dict)
        print("The attribute list in MVD is:",attrs_lst)
        print("The num_attr in MVD is:",num_attrs)
        MVD_dict={}  #List of non-trivial MVDs. 
        var = raw_input("Please enter MVDs in a string separated by comma {Format example: 'A->->B, D->->C'>}. or type quit \n")
        if (var!="quit"):
            var="".join(var.split())
            if var[0]=="'":
                var=var[1:]
            if var[-1]=="'":
                var=var[:-1]
            MVD_lst=var.split(',')
            print('List of MVDs you entered: '+ str(MVD_lst))
            for MVD in MVD_lst:
                if trivial_MVD(FD_dict,MVD,num_attrs)==False:
                    MVD=MVD.split('->->')
                    key=MVD[0]
                    value=MVD[1]
                    if key in MVD_dict:
                        MVD_dict[key].append(value)
                    else:
                        MVD_dict[key]=[value]
        return MVD_dict