from setuptools import setup, find_packages
setup(
    name="File monitor", 
    version="0.0.2", 
    packages=find_packages(), 
    package_data={'':['test.log', '*.py']},
    author = 'Dmitry',
    author_email = 'Dmitry''s mail',
    scripts=['file_monitor.py']  
    )

