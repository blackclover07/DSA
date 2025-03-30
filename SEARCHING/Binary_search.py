search_list=[10,20,30,40,50,60,70,80,90]
search_key=100

low=0
high=len(search_list)-1

while low<=high:
    mid=(low+high)//2
    
    if search_list[mid]==search_key:
        print(f"Found at {mid}")
        break
    elif search_list[mid]<search_key:
        low=mid+1
    else:
        high=mid-1
        
else:
    print("not found")