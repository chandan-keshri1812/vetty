from app import create_app

# Created Flask app
app = create_app()

if __name__ == "__main__":
    # Run the Flask development server
    app.run(host="0.0.0.0", port=5000, debug=True)