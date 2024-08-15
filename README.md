Blue Robotics has switched to using the RUST language and provides a precompiled library compatible with python and c++.

This repository's parent seems to be abandoned with zero documentation. Therefore, this repository attempts to allow users to use python for direct communication with the PWM controller chip and supplement documentation.

The project this was modified for was unsuccessful in using the navigator library or the pca library supported by Blue Robotics. On top of this the project asked for ROS Melodic which uses python 2.7. The library was modified to perform lower level calculations without using builtin functions available in python 3, and it adds a close function to prevent warnings during subsequent launches.

Library Interface Structure:
initialize()
gpio_close()
#Prescaler Configuration
  get_prescaler() - Read current chip prescaler
  set_prescaler(prescaler) - Configure prescaler
  set_pwm_frequency(target_frequency_hz) - Set frequency output of PCA
#Output Functions
  output_enable() - Set Output Enable pin
  output_disable() - Unset Output Enable pin
  output_enabled() - Check Output Enable pin status
  output_clear() - BL "clear all pwm output registers"
#List interface
  raw() - Get Raw Byte values
  raw(values) - Set Raw Byte values
  duty() - Get Duty Cycle values
  duty(values) - Set Duty Cycle values
  pwm() - Get PWM us values
  pwm_values() - Set PWM us values
#Channel access
  channel_get_raw(channel) - Get Raw Bytes from channel
  channel_get_duty(channel) - Get Duty Cycle from channel
  channel_get_pwm(channel) - Get PWM us from channel
  channels_get_raw_all() - Get Raw Bytes from all
  channels_get_duty_all() - Get Duty Cycle from all
  channels_get_pwm_all() - Get PWM us from all
  channel_set_raw(channel, raw) - Set Raw Bytes to channel
  channel_set_duty(channel, duty) - Set Duty Cycle to channel
  channel_set_pwm(channel, pwm_us) - Set PWM us to channel
  channels_set_raw(duties) - Does not look right -todo edit
  channels_set_duty(duties) - Set Duty Cycles
  channels_set_pwm(pwms_us) - Set PWM uses
  channels_set_raw_all(raw) - Set Raw Bytes to all
  channels_set_duty_all(duty) - Set Duty Cycle to all
  channels_set_pwm_all(pwm_us) - Set PWM us to all
#Bus Transactions
  read(register_address, nbytes) - read number of bytes from register and successive registers
  write(register_address, data) - write L and H to some register and the next one
#Conversion facilities
  offreg(channel) - gets register index by adding from the first
  prescaler_to_frequency(prescaler) - BR "f(prescaler + 1) = extclk/(4096)"
  frequency_to_prescaler(frequency_hz) - BR "datasheet section 7.2.5: prescaler = round(extclk/(4096*f)) - 1"
  raw_to_pwm(raw) - multiply by the period in us defined by the pwm frequency and divide by 4095
  pwm_to_raw(pwm_us) - multiply by 4095 and divide by the period
  raw_to_duty(raw) - divide by 4095
  duty_to_raw(duty) - multiply by 4095
  raw_to_data(raw) - split and convert L and H
  data_to_raw(data) - shift and join L and H

List interface functions and the Access classes seem to be pretty useless, just abstraction layers that add nothing new.
