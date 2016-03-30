#!/usr/bin/python

from electrotas import RelaySwitcher
import argparse
import sys

if __name__ == '__main__':

    device = RelaySwitcher()
#   following line can be uncommented to change relay names
#    device.set_names("A", "B", "C", "D")

    parser = argparse.ArgumentParser(description='Handles FT245R chip from ElectroTAS board')
    parser.add_argument('-r', '--read-pins', action='store_true', help='')
    parser.add_argument('-s', '--set-channel', metavar='chName', nargs='+', choices=sorted(device.get_names()), dest='channel_on', help='Sets chN Relay')
    parser.add_argument('-c', '--clear-channel', metavar='chName', nargs='+', choices=sorted(device.get_names()), dest='channel_off', help='Clear chN Relay')
    args = parser.parse_args()

    if args.channel_on and args.channel_off:
        set_clear_intersection = set(args.channel_on).intersection(args.channel_off)
        if set_clear_intersection:
            print 'Outputs can not be set and cleared at the same time'
            sys.exit(1)
    if args.channel_on:
        device.set_sw_by_name(args.channel_on)
    if args.channel_off:
        device.clear_sw_by_name(args.channel_off)
    if args.read_pins:
        device.get_states()
