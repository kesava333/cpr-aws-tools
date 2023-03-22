"""Set up the package using python3 setup.py install"""
import glob
import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='cpr-aws-tools',
    description='Tool to setup aws environment',
    version='1.0',
    url='https://github.com/kesava333/cpr-aws-tools.git',
    author='DevOps Team',
    author_email='kginjupalli@clearpath.ai',
    license='Proprietary',
    packages=setuptools.find_packages(),
    include_package_data=True,
    scripts=glob.glob('scripts/*'),
    install_requires=required,
    zip_safe=False
)
