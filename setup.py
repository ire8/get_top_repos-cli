from setuptools import setup
setup(
    name = 'get_top_repos-cli',
    version = '0.1.0',
    packages = ['get_top_repos'],
    entry_points = {
        'console_scripts': [
            'get_top_repos = get_top_repos.__main__:main'
        ]
    })
