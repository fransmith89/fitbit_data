from flask import Flask

from fitbit_data.app import create_app

if __name__ == '__main__':
    create_app().run()
