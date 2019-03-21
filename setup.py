import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='face_detector',
     version='0.1',
     scripts=['scripts/zlib_install'] ,
     author="Luis Rojas Aguilera",
     author_email="rojas@icomp.ufam.edu.br",
     description="State-of-the-art face detection and landmarks localization",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/roj4s/face_detector",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
