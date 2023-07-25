import main
import requests
# get api
def get_food():
    global url
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
    # asking about user specfcation

    dish_type = input('what is the dish type')
    cuisine = input('what cousien do you whant')
    diet = input('what diet do you want')
    intolerances = input('do you have any intolerances')
    includeIngredients = input('what is the includeIngredients')


    def error_handle_get_api():



     try:
        global  querystring
        get_food()
        querystring = {"query": dish_type, "cuisine": cuisine, "diet": diet,
                   "intolerances": intolerances , "includeIngredients":includeIngredients}
     except Exception:
        print(Exception.args)


# api

headers = {
	"X-RapidAPI-Key": main.X_RapidAPI_Key(),
	"X-RapidAPI-Host": main.X_RapidAPI_Host()
}

response = requests.get(url, headers=headers, params=querystring)
print()
print(response.json())
