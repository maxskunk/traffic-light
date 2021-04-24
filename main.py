from aiohttp import web
from gpiozero import LED
from time import sleep
import threading

green_light = LED(21)
yellow_light = LED(20)
red_light = LED(16)

def LED_ON( led,wait_time ):
    threading.Timer(wait_time, lambda: led.on()).start()

def LED_OFF( led,wait_time ):
    threading.Timer(wait_time, lambda: led.off()).start()

async def handleDisco(request):
    LED_ON(yellow_light, 0)
    LED_OFF(yellow_light, 0.1)
    LED_ON(red_light, .2)
    LED_OFF(red_light, .3)
    LED_ON(green_light, .4)
    LED_OFF(green_light, .5)
    LED_ON(yellow_light, .6)
    LED_OFF(yellow_light, .7)
    LED_ON(red_light, .8)
    LED_OFF(red_light, .9)
    LED_ON(green_light, 1.0)
    LED_OFF(green_light, 1.1)
    LED_ON(yellow_light, 1.2)
    LED_OFF(yellow_light, 1.3)
    LED_ON(red_light, 1.4)
    LED_OFF(red_light, 1.5)
    LED_ON(green_light, 1.6)
    LED_OFF(green_light, 1.7)
    LED_ON(yellow_light, 1.8)
    LED_OFF(yellow_light, 1.9)
    LED_ON(red_light, 2)
    LED_OFF(red_light, 2.1)
    LED_ON(green_light, 2.2)
    LED_OFF(green_light, 2.3)
    return web.Response(text="disco")

async def handleYellow(request):
    yellow_light.on()
    return web.Response(text='yellow')


async def handleRed(request):
    red_light.on()
    return web.Response(text='red')


async def handleGreen(request):
    green_light.on()
    return web.Response(text='green')


async def handleOff(request):
    green_light.off()
    yellow_light.off()
    red_light.off()
    return web.Response(text='lights off')

app = web.Application()
app.add_routes([web.get('/yellow', handleYellow),
                web.get('/red', handleRed),
                web.get('/green', handleGreen),
                web.get('/off', handleOff),
                web.get('/disco', handleDisco),
                ])




if __name__ == '__main__':
    web.run_app(app)
