[BlueRobotics](https://bluerobotics.com/) has switched to using the RUST language and provides a precompiled [library](https://github.com/bluerobotics/navigator-lib) for the [Navigator](https://bluerobotics.com/store/comm-control-power/control/navigator/), compatible with python and c++.

This repository's parent seems to be abandoned with zero documentation. Therefore, this repository attempts to allow users to use python for direct communication with the PWM controller chip and supplement documentation.

The project this was modified for was unsuccessful in using the navigator library supported by BlueRobotics. On top of this the project asked for ROS Melodic which uses python 2.7. This library was modified to perform lower level calculations without using builtin functions available in python 3, and it adds a close function to prevent warnings during subsequent launches.

**Library Interface Structure:**
+ \_\_init\_\_(bus=4) - Open bus to set i2c bus number, run initialize, GPIO setup
+ initialize() - Start PCA
+ gpio_close() - Cleanup GPIO
1. #Prescaler Configuration
   + get_prescaler() - Read current chip prescaler
   + set_prescaler(prescaler) - Configure prescaler
   + set_pwm_frequency(target_frequency_hz) - Set frequency output of PCA
2. #Output Functions
   + output_enable() - Set Output Enable pin
   + output_disable() - Unset Output Enable pin
   + output_enabled() - Check Output Enable pin status
   + output_clear() - BL "clear all pwm output registers"
3. #List interface
   + raw() - Get Raw Byte values
   + raw(values) - Set Raw Byte values
   + duty() - Get Duty Cycle values
   + duty(values) - Set Duty Cycle values
   + pwm() - Get PWM us values
   + pwm_values() - Set PWM us values
4. #Channel access
   + channel_get_raw(channel) - Get Raw Bytes from channel
   + channel_get_duty(channel) - Get Duty Cycle from channel
   + channel_get_pwm(channel) - Get PWM us from channel
   + channels_get_raw_all() - Get Raw Bytes from all
   + channels_get_duty_all() - Get Duty Cycle from all
   + channels_get_pwm_all() - Get PWM us from all
   + channel_set_raw(channel, raw) - Set Raw Bytes to channel
   + channel_set_duty(channel, duty) - Set Duty Cycle to channel
   + channel_set_pwm(channel, pwm_us) - Set PWM us to channel
   + channels_set_raw(duties) - **Does not look right -todo edit**
   + channels_set_duty(duties) - Set Duty Cycles
   + channels_set_pwm(pwms_us) - Set PWM uses
   + channels_set_raw_all(raw) - Set Raw Bytes to all
   + channels_set_duty_all(duty) - Set Duty Cycle to all
   + channels_set_pwm_all(pwm_us) - Set PWM us to all
5. #Bus Transactions
   + read(register_address, nbytes) - read number of bytes from register and successive registers
   + write(register_address, data) - write L and H to some register and the next one
6. #Conversion facilities
   + offreg(channel) - gets register index by adding from the first
   + prescaler_to_frequency(prescaler) - BR "f(prescaler + 1) = extclk/(4096)"
   + frequency_to_prescaler(frequency_hz) - BR "datasheet section [7.2.5](https://www.nxp.com/docs/en/data-sheet/PCA9685.pdf#G4466852): prescaler = round(extclk/(4096*f)) - 1" - on 7.3.5
   + raw_to_pwm(raw) - multiply by the period in us defined by the pwm frequency and divide by 4095
   + pwm_to_raw(pwm_us) - multiply by 4095 and divide by the period
   + raw_to_duty(raw) - divide by 4095
   + duty_to_raw(duty) - multiply by 4095
   + raw_to_data(raw) - split and convert L nd H
   + data_to_raw(data) - shift and join L and H

  
List interface functions and the Access classes seem to be pretty useless, just abstraction layers that add nothing new and are not used consistently.


[**servo.py**](https://github.com/AdamPoloha/BlueROV2-Navigator-PWM-pca9685-python/blob/master/pca9685/servo.py)

This script was created to make sure that the camera servo could be operated.

Tested parameters are defined, for the centre, the minimum, and the maximum camera angles as us. The PCA is initialised, and then starts the test operation. Centre, min, max, and centre andgles are set with time breaks between.
The code is run with no arguments.


[**spin0.py**](https://github.com/AdamPoloha/BlueROV2-Navigator-PWM-pca9685-python/blob/master/pca9685/spin0.py)

This script should spin up the motor on channel 0, or port 1 as shown on the Navigator.

PCA is initialised, frequency is set to 500Hz as 1kHz did not seem to work. PWM is preset to [ESC](https://bluerobotics.com/store/thrusters/speed-controllers/besc30-r3/#tab-learn) middle value, and then the output is enabled to prevent instant random spin. The middle value is set again to initialise the ESC and then the test starts. The lowest constant speeds in the two directions are set with time between and then the middle value is set again to stop rotation.

[**test.py**](https://github.com/AdamPoloha/BlueROV2-Navigator-PWM-pca9685-python/blob/master/pca9685/test.py)

This script tries to be what the original [test.py](https://github.com/bluerobotics/pca9685-python/blob/master/pca9685/test.py) could have been.

It gives the user flexibility to set one speed to any number of motor channels, set the PWM frequency, and get the set value for any channel.

To run it in python 2 try:
```python2 ./test.py --set 0 1 2 3 4 5 6 7 --us 1430 --frequency 500```

This will run a similar operation to spin0.py for the channel numbers after ```--set```. It will set all of these channels to the us value after ```--us```, so a safe 1430. The frequency can also be set to 500Hz with ```--frequency``` to operate like spin0.py.

There is also the ```--get``` argument which is followed by the channel numbers like with ```--set```, but with no us, to check all channel values.

Using the example launch command, eight motors will be spun at a low speed with 1430us, they will start one-by-one and then turn off in the same order again.
