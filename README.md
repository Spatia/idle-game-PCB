# Idle Game PCB

The purpose of this project is to make an Idle/Incremental game from the PCB to the software.

## Hardware Part
TLDR: STM32 with buttons and analogical thumbpad joystick

### Core parts
MCU: STM32F401 (RET6) in LQFP64
PMS: BQ24075RGT in QFN16
Flash: 128Mbits - SPI

### I/O
1 320x240 Screen ILI9341 based - SPI
6 Buttons for game control - GPIO
2 Buttons for screen/power control - GPIO
1 Button for BOOT0
1 PSP Thumbpad - ADC
1 USB-C for DFU and Charging battery

### PCB Architecture
4 Layer:
1. Front: I/O and STM32
2. In1: Ground
3. In2: Power (3v3 and VBAT)
4. Back: Battery and Power management
