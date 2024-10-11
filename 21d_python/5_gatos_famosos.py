cats = [
    {
        'name':'Mimi',
        'followers':[320,120,70]
    },
    {
        'name':'Milo',
        'followers':[400,300,100,200]
    },
    {
        'name':'Gizmo',
        'followers':[250,750]
    }
]

def find_famous_cats (cats):
    followers_list = []
    for i in range(0,len(cats)):
        followers_list.append(sum(cats[i]['followers']))

    max_val = max(followers_list)

    max_index = []
    for i in range(0,len(followers_list)):
        if followers_list[i] == max_val:
            max_index.append(i)

    famous_cats = []
    for i in max_index:
        famous_cats.append(cats[i]['name'])
    return famous_cats

print(find_famous_cats(cats))