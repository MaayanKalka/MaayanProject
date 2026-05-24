from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

nail_salons = [
    {
        "name": "Sparkle Nails",
        "address": "123 Main Street",
        "description": "Modern nail art with a relaxing atmosphere.",
        "services": ["Manicure", "Pedicure", "Nail Art"]
    },
    {
        "name": "Polished Perfection",
        "address": "456 Oak Avenue",
        "description": "Expert technicians and premium products.",
        "services": ["Gel Nails", "Acrylics", "Spa Pedicure"]
    }
]

HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Nail Salons</title>
    <style>
        body { font-family: Arial, sans-serif; background: #ffe5f0; margin: 0; padding: 0;}
        header { background: #e75480; color: white; padding: 20px; text-align: center;}
        .container { max-width: 900px; margin: 40px auto; background: white; padding: 30px; border-radius: 8px; }
        .salon { border-bottom: 1px solid #f5c2d3; padding: 20px 0; }
        .salon:last-child { border-bottom: none; }
        h2 { margin-top: 0;}
        .add-form { margin-top: 40px;}
        label { display: block; margin: 8px 0 4px;}
        input, textarea { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;}
        .services-input { margin-bottom: 16px;}
        button { background: #e75480; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;}
        button:hover { background: #c94365; }
    </style>
</head>
<body>
    <header>
        <h1>Nail Salons Directory</h1>
    </header>
    <div class="container">
        <h2>Salons</h2>
        {% for salon in nail_salons %}
            <div class="salon">
                <h3>{{ salon.name }}</h3>
                <p><strong>Address:</strong> {{ salon.address }}</p>
                <p><strong>Description:</strong> {{ salon.description }}</p>
                <p><strong>Services:</strong>
                    {% for s in salon.services %}
                        <span>{{ s }}</span>{% if not loop.last %}, {% endif %}
                    {% endfor %}
                </p>
            </div>
        {% endfor %}

        <div class="add-form">
            <h2>Add a Salon</h2>
            <form method="POST" action="{{ url_for('add_salon') }}">
                <label for="name">Salon Name:</label>
                <input type="text" name="name" id="name" required>
                <label for="address">Address:</label>
                <input type="text" name="address" id="address" required>
                <label for="description">Description:</label>
                <textarea name="description" id="description" required></textarea>
                <label for="services">Services (comma separated):</label>
                <input type="text" name="services" id="services" class="services-input" placeholder="e.g. Manicure, Pedicure, Nail Art" required>
                <button type="submit">Add Salon</button>
            </form>
        </div>
    </div>
</body>
</html>
"""
print("hi")
@app.route("/", methods=["GET"])
def home():
    return render_template_string(HOME_TEMPLATE, nail_salons=nail_salons)

@app.route("/add", methods=["POST"])
def add_salon():
    name = request.form["name"]
    address = request.form["address"]
    description = request.form["description"]
    services_list = [service.strip() for service in request.form["services"].split(",") if service.strip()]
    nail_salons.append({
        "name": name,
        "address": address,
        "description": description,
        "services": services_list
    })
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

