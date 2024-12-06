from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Function to fetch Pokémon data
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "Name": data["name"].capitalize(),
            "ID": data["id"],
            "Height": data["height"],
            "Weight": data["weight"],
            "Base Experience": data["base_experience"],
            "Abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "Types": [ptype["type"]["name"] for ptype in data["types"]],
        }
    except requests.exceptions.RequestException:
        return {"Error": "Pokémon not found or an error occurred."}

@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    pokemon_name = request.args.get('name', '')
    if not pokemon_name:
        return jsonify({"Error": "Please provide a Pokémon name."}), 400

    data = fetch_pokemon_data(pokemon_name)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)


#python3 -m venv venv
#source venv/bin/activate
#pip install flask requests
#python app.py
#http://127.0.0.1:8080/pokemon?name=pikachu
