import os
color=lambda :os.system('color 6')
color()
List = open("list.txt" , "r").read().splitlines()
save_2L= open("2L.txt","w")
save_3L= open("3L.txt","w")
save_4L= open("4L.txt","w")
save_another= open("another.txt","w")
#---------------------------------------------------
cls=lambda :os.system("cls")
def filter():
    print("""   [ Username ]      |        [ length ]""")
    for user in List:
        line = f"""
      {user}           |             {len(user)}
        """
        if len(user)==2:
            print(line)
            save_2L.write(user+"\n")
        elif len(user)==3:
            print(line)
            save_3L.write(user+"\n")
        elif len(user)==4:
            print(line)
            save_4L.write(user+"\n")
        else:
            print(line)
            save_another.write(user+"\n")
    save_another.close()
    save_4L.close()
    save_2L.close()
    save_3L.close()
    cls()
    input("Finished ! [ Total = {} ] ".format(len(List)))
    exit(0)
print("\n    -- Filter Length --\n     Instagram : @404.erroz \n       Github : itserrozz\n-------------------------------------------\n")
input("[+] Press enter to start ")
filter()
