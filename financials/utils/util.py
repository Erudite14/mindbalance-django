#
# Copyright (C) 2013 Webvirtmgr.
#
import random
#import libxml2
import lxml.etree as ET
#import xml.etree.ElementTree as ET
import libvirt





def randomUUID():
    """Generate a random UUID."""

    u = [random.randint(0, 255) for dummy in range(0, 16)]
    return "-".join(["%02x" * 4, "%02x" * 2, "%02x" * 2, "%02x" * 2, "%02x" * 6]) % tuple(u)

