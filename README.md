# symbolic-flows
Data:    
    Data Description: the information about data
    
    restaurantname.7z: the original data of restaurant POI in test area
    
    Symbolicflows.csv：the attribute table of constructed symbolic flows
    
CitySymbolExtractor.py: Identify place symbols from restaurant names and match the identified place symbols to prefecture-level cities

EntropyandEccentricity.py: Calculate the symbolic force and eccentricity (with gravity center) for all cities based on symbolic flows

Entropy_files.py: Calculate the symbolic force for all cities  

Windrosemap.py: draw a wind rose diagram to visualize the aggregated flows for a given city
