# Face Detector

This python package provides state-of-the-art face detection as well as face
landmark points localization. It gathers the techniques implemented in dlib and
mtcnn[], which can be easily switched between by setting a parameter in the
FaceDetector class instantiation (mtcnn is default if no technique is
specified).

## How to use:

    from face_detector import FaceDetector

    #In next line, *faces* is an array of Face(BoundingBox, LandmarkPoints)
    faces = FaceDetector().get_faces(img_addr)

    # Show image with bounding boxes and landmarks
    import cv2
    img = cv2.imread(img_addr)

    for face in faces:
       bb = face.bounding_box
       landmarks = face.landmarks
       cv2.rectangle(img, (int(bb.x), int(bb.y)), (int(bb.x + bb.w), int(bb.y+bb.h)), (0, 255, 0), 1)
       for l in landmarks:
            cv2.circle(img, (l.x, l.y), 2, (0,0,255))

        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

## How to install:

- From Github:
    - Clone this repository
    - Install dependencies in requirements.txt:
        - pip install -r requirements.txt
    - You might need to install zlib and link it on /usr/lib/x86_64-linux-gnu/libz.so:
        ```console
         foo@bar:~/face_detector$ tar xzvf data/zlib-1.2.9.tar.gz
         foo@bar:~/face_detector$ cd data/zlib
         foo@bar:~/face_detector/data/zlib$ sudo ./configure && make && make install
         foo@bar:~/face_detector/data/zlib$ ln -s /lib/x86_64-linux-gnu/libz.so.1.2.8 /usr/lib/x86_64-linux-gnu/libz.so
         ```

- TODO: A pip package being created



