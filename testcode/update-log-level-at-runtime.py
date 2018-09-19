''' Set basic logging, change level on the fly

'''

import logging
# Change default WARNING to ERROR level
logging.basicConfig(level=logging.ERROR, 
        format='%(asctime)s | %(levelname)s | %(message)s'
        )                     

def is_a(param1):
    return type(param1)

    
def test_types():    
    params = [1, "one", 1.0]
    for p in params:
        # Won't print
        logging.debug('{} is type: {}'.format(p, is_a(p)))
        
        # Won't print first time
        logging.info('{} is type: {}'.format(p, is_a(p)))
        logging.warning('{} is type: {}'.format(p, is_a(p)))
        
        # Will print
        logging.error('{} is type: {}'.format(p, is_a(p)))
        logging.critical('{} is type: {}'.format(p, is_a(p)))

        print()
        
if "__main__" == __name__:
    test_types()

    print('####################')
    print('# Change Log Level #')
    print('####################')
    logging.getLogger().setLevel(logging.INFO)
    test_types()
    