import logging
from utils.logger import logger
def validate_ip(ip: str) -> bool:
    parts = ip.split(".")
    if len(parts) != 4 :
        logger.error("Invalid IP octet : %s", ip)
        return False
    for i in parts :
        try :       
            num = int(i)
        except ValueError:
                logger.error("Invalid IP address : %s", ip)
                return False 
            
        if num < 0 or num > 256 :
            logger.error("Invalid IP address : %s", ip)  
            return False 

    logger.info("Connected to : %s",ip)
    return True 


            
    
    

    