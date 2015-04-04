# stegano-python
Simple python program to hide an image inside another using LSB replacement

More info (french) :
http://bastienfaure.fr/steganographie-en-python-cacher-une-image-dans-une-autre/

# Usage

If your are using python3, first install dependencies :

```
sudo apt-get install libjpeg8-dev zlib1g-dev python3-pip  
sudo pip3 install Pillow  
```

## Hide

```
./stegano.py path/to/cover.jpg path/to/secret.jpg
```

This will produce result.png

## Reveal

```
./stegano path/to/result.png
```

This will produce reveal.png


