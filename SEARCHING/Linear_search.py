search_list=[10,20,30,40,50,60,70,80,90]
search_key=100

for index,ele in enumerate(search_list):
    if search_key==ele:
        print(f"Found at {index}")
        break
else:
    print("not found")