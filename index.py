import random
from flask import Flask

app = Flask(__name__)

loot_containers = [
    "Buried Cache",
    "Duffle Bag",
    "Military Firearms Crate",
]

@app.route("/")
def home():

    container = random.choice(loot_containers)

    if container == "Buried Cache":
        items = [
            "CQA1",
            "Tuna",
            "Macrale",
            "Ice Tea",
        ]

        item = random.choice(items)
        
    return f"You lotted a {container} and found a {item}!"

if __name__ == "__main__":
    app.run()