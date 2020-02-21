__author__ = "Maxim Ziatdinov"
__copyright__ = "Copyright Maxim Ziatdinov (2019)"
__version__ = "0.1.0"
__maintainer__ = "Maxim Ziatdinov"
__email__ = "maxim.ziatdinov@ai4microcopy.com"
__date__ = "02/20/2019"

from setuptools import setup
import os

module_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup(
        name='atomai',
        version='0.1.0',
        description='Deep/machine learning for atom-resolved data',
        long_description=open(os.path.join(module_dir, 'README.md')).read(),
        long_description_content_type='text/markdown',
        url='https://github.com/ziatdinovmax/atomai',
        author='Maxim Ziatdinov',
        author_email='maxim.ziatdinov@ai4microcopy.com',
        license='MIT license',
        packages=['atomai'],
        zip_safe=False,
        install_requires=[
            'torch>=1.0.0',
            'numpy>=1.16.4', 
            'scipy>=1.3.0',
            'scikit-learn>=0.22.1',
            'scikit-image==0.16.2',
            'opencv-python>=4.1.0',
            'gdown>=3.8.1'
        ],
        classifiers=['Programming Language :: Python',
                     'Development Status :: 2 - Pre-Alpha',
                     'Intended Audience :: Science/Research',
                     'Operating System :: OS Independent',
                     'Topic :: Scientific/Engineering']
    )