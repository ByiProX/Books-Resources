#!/usr/bin/python
# -*- coding: utf-8 -*-

import optparse
import socket
import threading

screenLock = threading.Semaphore(value=1)


def connScan(tgtHost, tgtPort):
    connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+] %d/tcp open' % tgtPort)
        print('[+] ' + str(results))
    except Exception:
        screenLock.acquire()
        print('[-] %d/tcp closed' % tgtPort)
    finally:
        screenLock.release()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except Exception:
        print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return

    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except Exception:
        print('\n[+] Scan Results for: ' + tgtIP)

    socket.setdefaulttimeout(1)
    # tgtPorts = range(10000)
    for tgtPort in tgtPorts:
        t = threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()


def main():
    parser = optparse.OptionParser('usage %prog ' +
                                   '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',
                      help='specify target port[s] separated by comma')

    options, args = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost is None) or (tgtPorts[0] is None):
        print(parser.usage)
        exit(0)

    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
