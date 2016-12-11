# stegano-python
Simple python program to hide an image inside another using LSB replacement

More info (french) :
https://bastienfaure.fr/notes/steganographie-en-python-cacher-une-image-dans-une-autre

# Usage

If your are using python3, first install dependencies :

```
sudo apt-get install libjpeg8-dev zlib1g-dev python3-pip  
sudo pip3 install Pillow  
```

## Hide

Cover image :

![cover](https://bastienfaure.fr/wp-content/uploads/2016/12/stegano-python-cover.jpg)

Secret image :

![secret](https://bastienfaure.fr/wp-content/uploads/2016/12/stegano-python-secret.jpg)

```
./stegano.py path/to/cover.jpg path/to/secret.jpg
```

This will produce result.png :

![result](https://bastienfaure.fr/wp-content/uploads/2016/12/stegano-python-result.png)


## Reveal

```
./stegano path/to/result.png
```

This will produce reveal.png :

![reveal](https://bastienfaure.fr/wp-content/uploads/2016/12/stegano-python-reveal.png)
