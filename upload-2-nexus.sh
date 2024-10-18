python3 setup.py sdist bdist_wheel \
  && python3 -m twine upload --repository-url https://gzv-nex.piston.ink/repository/python-hosted/ dist/*

  pip3 install xyz_gmsm==1.1.0 -i https://gzv-nex.piston.ink/repository/python-group/simple