from Application import App

def test_hello(name):
    return f"Hello {name}"


if __name__ == "__main__":

    App.init()

    if App.args.test_arg:
        App.logger.info(App.args.test_arg)

    App.run()
