import sys
try:
    from pylibftdi import BitBangDevice
except:
    print '"pylibftdi" python module must be installed \n type: "$ pip install pylibftdi" to get it and then try again'
    sys.exit()
RELE1=0x02
RELE2=0x08
RELE3=0x20
RELE4=0x80

output_mask = [RELE1, RELE2, RELE3, RELE4]

class RelaySwitcher(object):
    def __init__(self):
        try:
            self.ft245 = BitBangDevice()
        except:
            print 'It may be possible that your device it is not connected, check that and try again\n'
            sys.exit()
        self.__output_names = {"RELE1": 0, "RELE2": 1, "RELE3": 2, "RELE4": 3}

    def __del__(self):
        self.ft245.close()
        pass

    def set_sw_by_name(self, sw_names):
        output_numbers = [self.__output_names[i] for i in sw_names]
        output_word = [output_mask[i] for i in output_numbers]
        output_word = sum(output_word)
        self.ft245.port |= output_word

    def clear_sw_by_name(self, sw_names):
        output_numbers = [self.__output_names[i] for i in sw_names]
        output_word = [output_mask[i] for i in output_numbers]
        output_word = sum(output_word)^255
        self.ft245.port &= output_word

    def get_states(self):
        pins_status = self.ft245.read_pins()
        for k in sorted(self.__output_names.keys()):
            print "{}: {}\n".format(k,'ON'if output_mask[self.__output_names[k]]&pins_status else 'OFF')

    def set_names(self, rele1, rele2, rele3, rele4):
        self.__output_names = {rele1: 0, rele2: 1, rele3: 2, rele4: 3}
        return self.__output_names

    def get_names(self):
        return self.__output_names
