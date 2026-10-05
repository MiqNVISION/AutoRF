# AutoRF
AutoRF is a Raspberry Pi 5 application that automates daily RF data acquisition and processing.

## Objectives
- Run automatically on a predefined schedule.
- Execute unattended.
- Acquire and process RF sensor data.
- Store outputs and logs locally.
- Support future cloud synchronization and reporting.

## Hardware
- Raspberry Pi 5
- RTC (DS3231)
- RF sensing hardware

## Software Architecture
```text
RTC
 ↓
systemd timer
 ↓
Python application
