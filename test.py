from flask import Flask

app = Flask(import_name=__name__)


@app.get(rule="/")
def test():
    return "success", 200


if __name__ == "__main__":
    app.run()
