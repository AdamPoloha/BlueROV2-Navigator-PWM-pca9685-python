#!/usr/bin/python3

#Expanded by Adam Poloha

def main():
    import argparse
    from pca9685 import PCA9685
    import time
    parser = argparse.ArgumentParser()
    parser.add_argument('--frequency', action='store', type=int, default=None)
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('--get', action='store', nargs='+', type=int)
    group1.add_argument('--set', action='store', nargs='+', type=int)
    parser.add_argument('--us', action='store', type=int)
    args = parser.parse_args()
    
    #python2 ./test.py --set 0 1 2 3 4 5 6 7 --us 1430 --frequency 500

    servoch = 15
    initus = 1500

    pca = PCA9685()
    #pca.gpio_close() #close already open gpio
    #pca.__init__()

    if args.frequency:
        pca.set_pwm_frequency(args.frequency)

    #Preset all channels as motor except servo
    c = 0
    while c < servoch:
        pca.channel_set_pwm(c, initus)
        c = c + 1
    
    #Enable outputs
    pca.output_enable()
    print("Wait for 1 second")
    time.sleep(1)
    
    #Enable all channels as motor except servo
    c = 0
    while c < servoch:
        pca.channel_set_pwm(c, initus)
        c = c + 1
    print("Wait for 1 second")

    if args.get:
        for channel in args.get:
            print("Channel", channel, "pwm:", pca.pwm[channel]) 
    elif args.set:
        if args.us:
            print("Setting PWM for motors")
            #Set us to desired value
            for channel in args.set:
                print("Setting channel:", channel)
                try:
                    pca.channel_set_pwm(channel, args.us)
                    print("Working")
                    print("Hold ON for 2 seconds")
                    time.sleep(2)
                except Exception as e:
                    print("Failed")
                    print(e)
            
            #Stop motors
            for channel in args.set:
                print("Stopping channel:", channel)
                try:
                    pca.channel_set_pwm(channel, initus)
                    print("Working")
                    print("Hold OFF for 1 second")
                    time.sleep(1)
                except Exception as e:
                    print("Failed")
                    print(e)
        else:
            print("No speed to set")
    
    print("Motors may jolt once disabled, wait for 2 seconds")
    time.sleep(2)
    
    #Disable output
    pca.output_disable()
    #Close GPIO to prevent warning
    pca.gpio_close()

if __name__ == '__main__':
    main()
