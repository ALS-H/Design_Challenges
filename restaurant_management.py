"""  
Classes:
1. Restaurant
2. Branch
3. Menu
4. CourseCategory
5. MenuItem 


Relationships:
1. Restaurtant -> Branch , Aggregation (1- 1..*)
2. Branch ->Menu , Composition (1- 1..*)
3. Menu -> CourseCategory , Composition (1- 3..*)
4. CourseCategory -> MenuItem , Composition (1- 1..*)
"""

#Class MenuItem
class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
#Class CourseCategory
class CourseCategory:
    def __init__(self,name):
        self.name=name
        self.items=[]
    
    def add_item(self,item):
        self.items.append(item)

#Class Menu
class Menu:
    def __init__(self,name,is_special=False):
        self.name=name
        self.is_special=is_special
        self.categories=[]
    
    def add_category(self,category):
        self.categories.append(category)

    def get_discount(self):
        return 30 if self.is_special else 0

#Class Branch
class Branch:
    def __init__(self,location):
        self.location=location
        self.menus=[]
    
    def add_menu(self,menu):
        self.menus.append(menu)
        
#Class Restaurant
class Restaurant:
    def __init__(self,name):
        self.name=name
        self.branches=[]
    
    def add_branch(self,branch):
        self.branches.append(branch)
        
    #1. total number of menu Items
    def total_menu_items(self):
        count=0
        for branch in self.branches:
            for menu in branch.menus:
                for category in menu.categories:
                    count+=len(category.items)
        return count                    

    # 2. List all menu items for a particular course category
    def list_items_by_category(self,category_name):
        result=[]
        for branch in self.branches:
            for menu in branch.menus:
                for category in menu.categories:
                    if category.name==category_name:
                        result.extend(category.items)
        return result
    
    # 3. List all the special discount menus
    def list_special_menus(self):
        specials=[]
        for branch in self.branches:
            for menu in branch.menus:
                if menu.is_special:
                    specials.append(menu)
        return specials
    
    
    
if __name__=="__main__":
    # Create restaurant
    restaurant = Restaurant("Foodies Hub")

    # Create branch
    branch1 = Branch("Hyderabad")

    # Create menu
    menu1 = Menu("Regular Menu")
    menu2 = Menu("Festival Special", is_special=True)
    menu3 = Menu("Weekend Special", is_special=True)

    # Menu 1 categories
    starter1 = CourseCategory("Starter")
    main1 = CourseCategory("Main Course")
    dessert1 = CourseCategory("Dessert")

    starter1.add_item(MenuItem("Soup", 120))
    starter1.add_item(MenuItem("Spring Roll", 150))
    main1.add_item(MenuItem("Biryani", 250))
    dessert1.add_item(MenuItem("Ice Cream", 100))

    menu1.add_category(starter1)
    menu1.add_category(main1)
    menu1.add_category(dessert1)


    # Menu 2 categories (separate objects)
    starter2 = CourseCategory("Starter")
    main2 = CourseCategory("Main Course")
    drinks=CourseCategory("Drinks")
    dessert2 = CourseCategory("Dessert")

    starter2.add_item(MenuItem("Mushroom Soup", 130))   # different price
    main2.add_item(MenuItem("Roti Dal", 150))
    main2.add_item(MenuItem("Pav Bhaji",150))
    drinks.add_item(MenuItem("Sharbat",300))
    dessert2.add_item(MenuItem("Laddoo", 200))

    menu2.add_category(starter2)
    menu2.add_category(main2)
    menu2.add_category(drinks)
    menu2.add_category(dessert2)


    # menu3 categories: 5 Course Categories
    starter3 = CourseCategory("Starter")
    soup3 = CourseCategory("Soups")
    main3 = CourseCategory("Main Course")
    dessert3 = CourseCategory("Dessert")
    beverages3 = CourseCategory("Beverages")
    
    # Add items
    starter3.add_item(MenuItem("Garlic Bread", 180))
    soup3.add_item(MenuItem("Tomato Soup", 140))

    main3.add_item(MenuItem("Paneer Butter Masala", 260))
    main3.add_item(MenuItem("Butter Naan", 60))

    dessert3.add_item(MenuItem("Brownie", 220))
    beverages3.add_item(MenuItem("Fresh Lime Soda", 120))
    
    # Add categories to menu
    menu3.add_category(starter3)
    menu3.add_category(soup3)
    menu3.add_category(main3)
    menu3.add_category(dessert3)
    menu3.add_category(beverages3)
    
    
    # Add menus to branch
    branch1.add_menu(menu1)
    branch1.add_menu(menu2)
    branch1.add_menu(menu3)

    # Add branch to restaurant
    restaurant.add_branch(branch1)

    # Outputs
    print("Total menu items:", restaurant.total_menu_items())

    #by category wise
    print()
    for item in restaurant.list_items_by_category("Dessert"):
        print(item.name, "-", item.price)

    print("\nSpecial Menus:")
    for menu in restaurant.list_special_menus():
        print(menu.name, "- Discount:", menu.get_discount(), "%")

                    
                
            
        
                    