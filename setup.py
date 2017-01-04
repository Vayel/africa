from setuptools import setup, find_packages


setup(
    name='flask-projectile',
    url='https://github.com/Vayel/flask-projectile',
    author='Vincent Lefoulon',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-WTF',
        'projectile',
        'javelot',
    ],
    dependency_links=[
        'git+https://github.com/Vayel/projectile#egg=projectile-1.0.0',
        'git+https://github.com/Vayel/javelot#egg=javelot-1.0.0',
    ],
)
