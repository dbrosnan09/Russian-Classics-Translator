#!/usr/bin/env python                                                                                                                                                                
# -*- coding: utf-8 -*-

import re





    
        
    

test_string = """




"""

result = re.sub(r"\b([А-ЯЁа-яё]+)\b","<span>" + r'\1' + '</span>', test_string)



text_file = open("wp2.txt", "w")
n = text_file.write(result)
text_file.close()


