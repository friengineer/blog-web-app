from app import app

# checks if the source file contains the main module being executed. This code prevents a warning
# from appearing when executing the code
if __name__ == '__main__':
    app.run(debug=True)
