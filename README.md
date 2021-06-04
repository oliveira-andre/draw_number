# Draw Number

## How to use

installing dependencies
```
pip3 install -r requirements.txt
```

running the app
```
python3 ini.py
```

if you need a new number change this variable
```python
number = "666"
```

if you dont want the background you could remove this code:
```python
for x in range(img.size[0]):
    for y in range(img.size[1]):
        data[x,y] = (
            x % 55,
            y % 55,
            (x**2-y**2) % 255,
        )
```

## Result

![result image](./image.png)
