import json

# Parsing json data from file today.json
with open('today.json','r') as today:
    json_data = [json.loads(line) for line in today]
    format_today = json.dumps(json_data,indent=2)
    today_data = json.loads(format_today)

# Parsing json data from file yesterday.json
with open('yesterday.json','r') as yesterday:
    json_data = [json.loads(line) for line in yesterday]
    format_yesterday = json.dumps(json_data,indent=2)
    yesterday_data = json.loads(format_yesterday)

# Main menu function
def choose():
    choice = 1
    while choice != 6:

        print("\n\n1. No. of overlapped URLH")
        print("2. The price difference (wrt available_price) for all overlapped URLH if there is any between yesterday's and today's crawls")
        print("3. No of Unique categories in both files.")
        print("4. List of categories which is not overlapping.")
        print("5. Generate the stats with count for all taxonomies.")
        print("6. Exit\n\n")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            overlappedUrlhCount()
        elif choice == 2:
            pdiff()
        elif choice == 3:
            UniqueCategoriesCount()
        elif choice == 4:
            CategoriesNotOverlapping()
        elif choice == 5:
            stats()
        elif choice == 6:
            exit
        else:
            print("Please enter valid choice.\n")


def overlappedUrlhCount():

    count_yesterday = 0
    overlap_count=0
    for i in yesterday_data:

        if yesterday_data[count_yesterday]['urlh']==today_data[count_yesterday]['urlh']:
            overlap_count += 1
        count_yesterday += 1
    print('Overlapped urlh',overlap_count)




def pdiff():
    count_yesterday = 0
    overlap_count = 0
    for i in yesterday_data:

        if yesterday_data[count_yesterday]['urlh'] == today_data[count_yesterday]['urlh']:
            diff = float(today_data[count_yesterday+2]["available_price"])-float(yesterday_data[count_yesterday]["available_price"])
            print("{}  ||  available price difference today/yesterday: {}".format(yesterday_data[count_yesterday]['title'],diff))

            count_yesterday += 1
    print('Overlapped urlh', overlap_count)


def UniqueCategoriesCount():
    count = 1
    y_category_count = 1
    t_category_count = 1
    for i in range(len(yesterday_data)-1):
        if yesterday_data[i]['category'] != yesterday_data[count]['category']:
            y_category_count += 1
        count+=1

    count = 1
    for j in range(len(today_data)-1):
        if today_data[j]['category'] != today_data[count]['category']:
            t_category_count += 1
        count += 1

    print("Number of unique categories in y.json : ",y_category_count)
    print("Number of unique categories in x.json : ",t_category_count)

def CategoriesNotOverlapping():
    import itertools
    # print("List of Categories not Overlapping")

    count = 1
    for i in range(len(yesterday_data) - 1):
        if yesterday_data[i]['category'] != yesterday_data[count]['category']:
            y_category = yesterday_data[i]["category"]
        count += 1

    count = 1
    for j in range(len(today_data) - 1):
        if today_data[j]['category'] != today_data[count]['category']:
            t_category = today_data[i]["category"]
        count += 1

    unique = list(t_category ^ y_category)
    print(unique)


    # for t in t_category:
    #     for y in y_category:
    #         if y == t:
    #             continue




def stats():
    print("Generate Stats")



choose()
#     print(data)

