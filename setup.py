import setuptools

with open("README.md", "rt") as fh:
    long_description = fh.read()

with open('requirements.txt', 'rt') as f:
    dependencies = f.read().split('\n')

setuptools.setup(
     name='face_detector',
     version='0.4',
     scripts=['scripts/facedetector'],
     author="Luis Rojas Aguilera",
     author_email="rojas@icomp.ufam.edu.br",
     description="State-of-the-art face detection and landmarks localization",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/roj4s/face_detector",
     packages=setuptools.find_packages(),
     include_package_data=True,
     install_requires=dependencies,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
