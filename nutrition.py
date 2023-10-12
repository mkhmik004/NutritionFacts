#MKHABELE MMM
#06/07/2023
def main():
    doctionaryFruit={
    'apple':130,'avocado':50,'bannana':110,
    'cantaloupe':50,'grape fruit':60,'grapes':90,
    'honeydew melon':50,
    'kiwifruit':90,'lemon':15,'lime':20,
    'nectarine':60,'orange':80,'peach':60,'pear':100,
    'pineapple':50,'plums':70,'strawberries':50,
    'sweet cherries':100,'tangerine':50,'watermelon':80
    }
    try:
        item=input("Item: ")
        print("Calories:",doctionaryFruit[item.lower()])
    except:
        pass
main()
