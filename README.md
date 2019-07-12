# Intensify

## Show your intensity!

`python intensify.py -f samples/waiting.gif`

![waiting](samples/waiting.gif) -> ![waiting-intensified](samples/waiting-intensifies.gif)

Works on static images (jpg tested)

`python intensify.py -f samples/bigdata.jpg`

## Customize your intensity

* Loop for more variety in your intensity

`python intensify.py -f samples/waiting.gif -l 2`

![loop](samples/waiting-intensifies-loop.gif)

* Shake faster or slower for more calculated intensity

`python intensify.py -f samples/waiting.gif -s .1`

![loop](samples/waiting-intensifies-fast.gif)

`python intensify.py -f samples/waiting.gif -s 10`

![loop](samples/waiting-intensifies-slow.gif)

* Shake more on every frame for more deliberate intensity

`python intensify.py -f samples/waiting.gif -d 5`

![loop](samples/waiting-intensifies-duplicate.gif)

* Shake farther for more intense intensity

`python intensify.py -f samples/waiting.gif --shift 10`

![loop](samples/waiting-intensifies-bigshift.gif)

* Combine to match your personal intensity

`python intensify.py -f samples/waiting.gif -l 3 -s .1 -d 2 --shift 20`

![loop](samples/waiting-intensifies-too-intense.gif)

## Intensify already intense gifs

![intense data](samples/bigdata-intensifies-intensifies-intensifies-intensifies-intensifies.gif)