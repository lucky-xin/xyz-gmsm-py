from setuptools import setup, find_packages

__version__ = '1.0.2'  # 版本号
requirements = open('requirements.txt').readlines()  # 依赖文件

setup(
    name='xyz_gmsm',  # 在pip中显示的项目名称
    version=__version__,
    author='chaoxin.lu',
    author_email='chaoxin.lu@pistonint.com',
    license='MIT',
    url='https://github.com/lucky-xin/xyz-gmsm-py.git',
    description='gmsm 工具包',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.5.0',
    install_requires=requirements  # 安装依赖
)
