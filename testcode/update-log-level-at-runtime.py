''' Set basic logging, change level on the fly

'''

import logging

def is_a(param1):
    return type(param1)

    
def test_types():    
    params = [1, "one", 1.0]
    for p in params:
        # Won't print
        logging.info('{} is type: {}'.format(p, is_a(p)))
        
        # Will print
        logging.warning('{} is type: {}'.format(p, is_a(p)))

        
if "__main__" == __name__:
    test_types()
    print('Change Log Level')
    # logging.basicConfig(level=logging.INFO)
    logging.getLogger().setLevel(logging.INFO)
    test_types()
    
