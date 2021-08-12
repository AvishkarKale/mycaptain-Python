Exten_dict={"py":"python","txt":"notepad","docx":"word"}
filename=str(input("Input the Filename (as filename.extention):"))
if "." in filename:
    j=0
    c=0
    while filename[j]!=".":
        c=c+1
        j=j+1
    index_position=c+1
    if filename[index_position:] in Exten_dict:
        print(f"The extension of the file is : {Exten_dict[filename[index_position:]]}")
    else:
        print("filename does not have a proper extention")
else:
    print("File name is written with no extention")