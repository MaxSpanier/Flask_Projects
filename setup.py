from setuptools import setup

setup(
    name="Flask_Template",
    packages=["app"],
    include_package_data=True,
    install_requires=[
        "flask",
        "Flask-WTF",
    ],
)

# Add requirements to the install_requires
# Then "pip install -e .
# flask --app app --debug run --port=5005
# ngrok http --domain=polecat-true-secretly.ngrok-free.app 5005
# access to config variables: current_app.config["name"]

# set the environment variables with: (Windows is set instead of export)
# export SECRET_KEY="your secret key"
# export DATABASE_URI="postgresql://username:password@host:port/database_name"

