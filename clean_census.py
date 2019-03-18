# make functions to organise data

def clean_census_data(data):
    # remove unwanted columns
    clean_data = (data.drop(['CDU_ID', 'GEO_LABEL', 'GEO_TYPE', 'GEO_TYP2'], axis =1)\
                  .drop([0], axis = 0)\
                  .set_index('GEO_CODE')\
                  .T)
    
    clean_data = clean_data.dropna(axis = 0).T
    
    return(clean_data)
    
def get_meta_data(data):
    # remove unwanted columns
    meta_data = (data.dropna(axis = 1)\
                .iloc[:1]\
                .T\
                )
    
    # separate into various columns
    for i in range(meta_data.iloc[0][0].count(' - ')):
        name = str(meta_data.iloc[0][0].split(' - ')[i].split(' : ')[0])
        
        # extract individual strings
        temp_list = []
        for j in range(len(meta_data)):
            var_string = str(meta_data.iloc[j][0].split(' - ')[i].split(' : ')[1])
            temp_list.append(var_string)
            #print(temp_list)

        # make columns
        meta_data[name] = temp_list
        #print(temp_list)
        
    # remove unwanted column
    meta_data = meta_data.drop([0], axis = 1)
    
    # clean headers
    meta_data.columns = meta_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(')', '').str.replace('(', '').str.replace(';', '')
        
    return(meta_data)
    
    
