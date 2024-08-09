#!/usr/bin/python3

#Made by Adam Poloha

def main():
    from pca9685 import PCA9685
    import time

    channel = 0
    initus = 1500

    pca = PCA9685()
    #pca.gpio_close() #close already open gpio
    #pca.__init__()

    pca.set_pwm_frequency(500)
    print("Init 1500")
    pca.channel_set_pwm(channel, initus)

    pca.output_enable()
    print("Wait for 1 second")
    time.sleep(1)

    #print(f'channel {channel} pwm: {pca.pwm[channel]}') 
    
    print("Init 1500")
    pca.channel_set_pwm(channel, initus)
    #pca.channel_set_duty(channel, 50)
    print("Wait for 1 second")
    time.sleep(1)
    print("Set 1466")
    pca.channel_set_pwm(channel, 1466) #lowest no pulsing
    print("Wait for 5 seconds")
    time.sleep(5)
    print("Set 1529")
    pca.channel_set_pwm(channel, 1529) #lowest no pulsing
    print("Wait for 5 seconds")
    time.sleep(5)
    print("Stop 1500")
    pca.channel_set_pwm(channel, initus)
    
    #pca.output_disable()
    #pca.gpio_close()

if __name__ == '__main__':
    main()
