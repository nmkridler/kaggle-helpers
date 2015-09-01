from setuptools import setup

setup(
    name='kaggle',
    version='0.0.1',
    author='Nicholas Kridler',
    author_email='nmkridler@gmail.com',
    license='MIT',
    description='Wrappers for common sklearn tools',
    packages = ['kaggle', 'kaggle.classifier'],
    long_description='Python tools for kaggle competitions',
    url='https://github.com/stitchfix/kaggle-tools',
    keywords=['kaggle', 'sklearn'],
    classifiers=[
        'Intended Audience :: Developers',
    ],
    install_requires=[
        'sklearn',
        'numpy',
        'pandas'
    ]
)