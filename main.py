from rasa.cli import run

if __name__ == "__main__":
    run.main(["run", "--enable-api", "--cors", "*", "--debug"])
