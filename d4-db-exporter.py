import requests

url = "http://127.0.0.1:8000/API/insertProductData/"

test = "allo"

payload = { #Replace the test values with variables :)
              "id":test,
              "name":"Test produit RCC",
              "brand_name":"Design 5",
              "total_weight":"0g",
              "serving_size":"0g",
              "calories":"0 cal",
              "fat":"0g",
              "saturated_fat":"0g",
              "trans_fat":"0g",
              "cholesterol":"0g",
              "sodium":"0g",
              "carbohydrate":"0g",
              "fibre":"0g",
              "sugars":"0g",
              "protein":"0g",
              "vitamin_a":"0%",
              "vitamin_c":"0%",
              "calcium":"0%",
              "iron":"0%",
              "ingredients":"Blood, sweat and tears",
              "logos":"McDonald",
              "ocr_text":"Lorem ipsum ocr",
              "image_front_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/McDonald%27s_Golden_Arches.svg/200px-McDonald%27s_Golden_Arches.svg.png"}


headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, json = payload)

print(response.content)
