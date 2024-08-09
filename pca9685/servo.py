#!/usr/bin/python3

#Made by Adam Poloha

def main():
    from pca9685 import PCA9685
    import time

    channel = 15
    cenus = 1450
    minus = 752
    maxus = 1999

    pca = PCA9685()
    #pca.gpio_close() #close already open gpio
    #pca.__init__()

    pca.set_pwm_frequency(500)
    print("Init central")
    pca.channel_set_pwm(channel, cenus)

    pca.output_enable()
    print("Wait for 1 second")
    time.sleep(1)

    #print(f'channel {channel} pwm: {pca.pwm[channel]}') 
    
    print("Init central")
    pca.channel_set_pwm(channel, cenus)
    #pca.channel_set_duty(channel, 50)
    print("Wait for 1 second")
    time.sleep(1)
    print("Set min")
    pca.channel_set_pwm(channel, minus)
    print("Wait for 5 seconds")
    time.sleep(5)
    print("Set max")
    pca.channel_set_pwm(channel, maxus)
    print("Wait for 5 seconds")
    time.sleep(5)
    print("Stop central")
    pca.channel_set_pwm(channel, cenus)
    
    #pca.output_disable()
    #pca.gpio_close()

if __name__ == '__main__':
    main()
