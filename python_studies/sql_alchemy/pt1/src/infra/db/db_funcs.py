import json
import cx_Oracle

def init_oracle(config_file:dict, key_name:str):
        '''
        Function that sets up cx_oracle with the Oracle's Instant Client driver 
        location.

        parameters
        ----------
        config_file:json
            A json file with the Oracle data base information.
        
        key_name:str
            The key name in the json file that indicates the location
            of the Oracle's Instant Client driver.

        '''
        orcl_conf=config_file[key_name]
        cx_Oracle.init_oracle_client(lib_dir=orcl_conf)

