import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# My solution with python 🙄
# fur_color_list = list(data["Primary Fur Color"])

# cinnamon_count = 0
# gray_count = 0
# black_count = 0

# for color in fur_color_list:
#     if color == "Cinnamon":
#         cinnamon_count += 1

#     if color == "Gray":
#         gray_count += 1

#     if color == "Black":
#         black_count += 1


# squirrel_count_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [gray_count, cinnamon_count, black_count],
# }

# squirrel_count = pandas.DataFrame(squirrel_count_dict)
# squirrel_count.to_csv("squirrel_count.csv")

# Solution with pandas 😎
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_count_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}

squirrel_count = pandas.DataFrame(squirrel_count_dict)
squirrel_count.to_csv("squirrel_count.csv")
