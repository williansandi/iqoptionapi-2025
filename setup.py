from setuptools import setup, find_packages

# Tenta ler o README.md para a descrição longa, se não encontrar, usa a descrição curta.
try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = 'Custom fork of the unofficial IQ Option API'

setup(
    name='iqoptionapi',
    version='6.8.9.1', # Versão baseada na original, com um patch seu
    packages=find_packages(),
    author='Willian Sandi',
    author_email='', # Pode adicionar seu email aqui
    description='Custom fork of the unofficial IQ Option API with updates.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/williansandi/iqoptionapi-2025-Atualizada-',
    license='MIT',
    install_requires=[
        'pydantic',
        'requests',
        'websocket-client'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
