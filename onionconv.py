#!/usr/bin/python
import otp2
import getopt, sys, os, base64

def usage():
    print "Onion OTP v0"
    print "2011 - Arturo Filasto' <art@baculo.org>"
    print "gives you a mnemonic alternative to standard onion urls"
    print "-h \t this help message"
    print "-o <onion url> (ex. jv6g2ucbhrjcnwgi)"
    print "-m <mnemonic name> (ex. anti-stan-bawd-fled-noll-fee-cant-1.onion)"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:m:")
    except getopt.GetoptError, err:
        usage()
        sys.exit(2)

    mnemonic = ""
    onionurl = ""
    o = False

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-o", "--onion"):
            onionurl = arg
            o = True
        elif opt in ("-m", "--mnemonic"):
            mnemonic = arg
            o = True
        a = otp2.OTP()

    if(o is False):
        usage()
        sys.exit()

    onionurl = onionurl.split('.')[0]

    if(onionurl):
        if(len(onionurl) == 16):
            print "mnemonic url: %s" % a.to_word(base64.b32decode(onionurl.upper()))
        else:
            print "invalid onion url length!"

    if(mnemonic):
        if(len(mnemonic.split('-')) == 8):
            print "onion url: %s.onion" % base64.b32encode(a.from_word(mnemonic)).lower()
        else:
            print "invalid mnemonic format!"

if __name__ == "__main__":
    main()

