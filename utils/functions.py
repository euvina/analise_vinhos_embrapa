# import libraries
# ------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# cleaning functions
# ------------------

def normalize_index(df):
    '''
    Normalize index name to lowercase 'id', without extra spaces
    
    Example:
        'Id' -> 'id',
        'id ' -> 'id',
        ' id' -> 'id',
        'ID' -> 'id',
    -------
    df: pandas dataframe
    
    '''
    # drop extra spaces
    df.columns = df.columns.str.strip()
    df.index.name = 'id'

    return df


def pais_to_country(df):
    '''
    Change any column named 'País' to 'country'
    -------
    df: pandas dataframe
    
    Example:\n
        |  id   |  País  |\n
        |  ---  |  ----  |\n
        |   1   | Brasil |\n
        |   ... |  ...   | ---> |  id   |  country |\n
                                |  ---  |   ----   |\n
                                |   1   |  Brasil  |\n
                                |  ...  |    ...   |
    '''
    df.rename(columns={'País': 'country'}, inplace=True)

    return df


# rename columns years with quantity and dolars
def correct_column_names(df):
    '''
    Rename headers to standard format:
        'year': 'year_quantity'
        'year.1': 'year_dolars'
        
    -------
    Params:
        df: pandas dataframe]
        return: pandas dataframe
    
    Example:\n
        |  id   |  País  |  1990  |  1990.1  |  1991  |  1991.1  |\n
        |  ---  |  ----  |  ----  |  ------  |  ----  |  ------  |\n
        |   1   | Brasil |  100   |   1000   |  200   |   2000   |\n
        |   ... |  ...   |  ...   |   ...    |  ...   |   ...    |\n
                                --->\n
        |  id   |  country |  1990_quantity  |  1990_dolars  |  1991_quantity  |  1991_dolars  |\n
        |  ---  |   ----   |      ----       |     ----      |      ----       |     ----      |\n
        |   1   |  Brasil  |       100       |      1000     |       200       |      2000     |\n
        |   ... |   ...    |       ...       |      ...      |       ...       |      ...      |

    '''
        
# rename columns
    new_columns = []
    for column in df.columns:
        # if column name contains letters, keep it as it is
        if column.isalpha():
            new_columns.append(column)
        # if column name contains 4 numbers
        elif column.isnumeric() and len(column) == 4:
            # then it is a quantity column
            new_columns.append(column + '_quantity')
        else:
            column = column[0:4]
            # it is a dolar column
            new_columns.append(column + '_dolars')
    df.columns = new_columns

    return df


def replace_country_names(df):
    '''
    Replace country names for standard names, mapped in a dictionary
    Also, order by ascending country and sets country as index
    
    -------
    Parameters:
        df: pandas dataframe
        return: pandas dataframe


    '''
    country_map = {
                    'Alemanha, República Democrática': 'Alemanha', # destruição do muro de Berlim foi em 1989
                    'Alemanha, República Democrática da': 'Alemanha',
                    'Africa do Sul': 'África do Sul',
                    'Antigua e Barbuda': 'Antígua e Barbuda',
                    'Arabia Saudita': 'Arábia Saudita',
                    'Australia': 'Austrália',
                    'Barein': 'Bahrein',
                    'Belice': 'Belize',
                    'Belgica': 'Bélgica',
                    'Birmânia': 'Myanmar', # trocou de nome em 1989
                    'Bosnia': 'Bósnia-Herzegovina',
                    'Bulgaria': 'Bulgária',
                    'Burquina Faso': 'Burkina Faso',
                    'Camores': 'Comores', # ortografia - pode ser Camarões, mas a probabilidade é menor
                    'Cingapura': 'Singapura',
                    'Cocos (Keeling)': 'Cocos, Ilhas',
                    'Cocos (Keeling), Ilhas': 'Cocos, Ilhas',
                    'Colombia': 'Colômbia',
                    'Coreia do Sul, Republica da': 'Coreia do Sul',
                    'Coréia do Sul': 'Coreia do Sul',
                    'Coreia, Republica Sul': 'Coreia do Sul',
                    # Coveite não está errado, mas Kuwait é mais popular segundo google trends
                    'Coveite': 'Kuwait',
                    'Djibuti': 'Djibouti',
                    'Dominica': 'Dominica, Ilha de', # padronizar?
                    'Emirados Arabes Unidos': 'Emirados Árabes Unidos',
                    'Eslovaca, Republica': 'Eslováquia',
                    'Eslovenia': 'Eslovênia',
                    'Estados Unidos': 'Estados Unidos da América', # nome completo permite usar a sigla EUA
                    'Estonia': 'Estônia',
                    'Falkland (Ilhas Malvinas)': 'Malvinas, Ilhas',
                    'Falkland (Malvinas)': 'Malvinas, Ilhas',
                    'Filânldia': 'Finlândia',
                    'Georgia': 'Geórgia',
                    'Grêcia': 'Grécia',
                    'Guiné Bissau': 'Guiné-Bissau', 
                    'Guine Bissau': 'Guiné-Bissau',
                    'Guine Equatorial': 'Guiné Equatorial',
                    'India': 'Índia',
                    'Indonêsia': 'Indonésia',
                    'Ilha de Man': 'Man, Ilha',
                    'Ilhas Virgens': 'Virgens, Ilhas',
                    'Islandia': 'Islândia',
                    'Italia': 'Itália',
                    # Em 25 de junho de 1991, Eslovênia e Croácia tornaram-se as primeiras repúblicas a declararem sua independência da Iugoslávia
                    'Iugoslâvia': 'Iugoslávia', # se dissolveu entre 1991 e 1992
                    'Jérsei': 'Jersey', # nome mais popular (google trends)
                    'Letonia': 'Letônia',
                    'Libêria': 'Libéria',
                    'Lituania': 'Lituânia',
                    'Malasia': 'Malásia',
                    'Maldivas': 'Maldivas, Ilhas',
                    'Mauricio': 'Maurício, Ilhas',
                    'Mexico': 'México',
                    'Nova Zelandia': 'Nova Zelândia',
                    'Paises Baixos (Holanda)': 'Holanda', 
                    'Países Baixos': 'Holanda',
                    'Panama': 'Panamá',
                    'Polonia': 'Polônia',
                    'Namibia': 'Namíbia',
                    'Nicaragua': 'Nicarágua',
                    'Quenia': 'Quênia',
                    'Republica Dominicana': 'Dominicana, República',
                    'Republica Tcheca': 'Tcheca, República',
                    'República Centro Africana': 'Centro-Africana, República',
                    'República Federativa da Rússia': 'Rússia',
                    'Russia,  Federação da': 'Rússia',
                    'Russia': 'Rússia',
                    'Suecia': 'Suécia',
                    'Suiça': 'Suíça',
                    'São Tomé e Principe': 'São Tomé e Príncipe',
                    'Tailandia': 'Tailândia',
                    'Taiwan (FORMOSA)': 'Taiwan', 
                    'Taiwan (Formosa)': 'Taiwan',
                    'Tcheca, República': 'Tcheca, República',
                    'Trinidade Tobago': 'Trindade e Tobago', 
                    'Trinidade e Tobago': 'Trindade e Tobago',
                    'Turcas e Caicos, ilhas': 'Turcas e Caicos, Ilhas',
                    'Suazilândia': 'Essuatíni', # mudou de nome em 2018
                    'Outros(1)': 'Outros'
        }
    
    df['country'] = df['country'].replace(country_map)
    df.sort_values(by='country', inplace=True)
    df.set_index('country', inplace=True)
    
    return df


def filter_years(df, year_space):
    
    '''
    Filter dataframe by last x years, defined by year_space
    -------
    Parameters:
        df: pandas dataframe
        year_space: int
        
    Returns:
        df: pandas dataframe
    
    '''
    # get range of last x*2 columns
    last_years = df.iloc[:, -year_space*2:].copy()
    
    # equivalent to:
    #last_years = df[df.columns.to_list()[-year_space*2:]].copy()

    return last_years



# transforming functions
# ----------------------

# function for droping '_dolars' from index
def drop_dolars(df):
    '''
    Drop '_dolars' from index
    '''
    df.index = df.index.str.replace('_dolars', '').astype(int)
    return df

def year_unit_value(df):
    '''
    calculate value per dolar in a new dataframe
    
    -------
    Parameters:
        df: pandas dataframe
        return: pandas dataframe

    Example:
        |  id   |  country |  1990_quantity  |  1990_dolars  |  1991_quantity  |  1991_dolars  |\n
        |  ---  |   ----   |      ----       |     ----      |      ----       |     ----      |\n
        |   1   |  Brasil  |       100       |      1000     |       200       |      2000     |\n
        |   ... |   ...    |       ...       |      ...      |       ...       |      ...      |\n
                                --->\n
        |  id   |  country |  1990  |  1991  |\n
        |  ---  |   ----   |  ----  |  ----  |\n
        |   1   |  Brasil  |   10   |   10   |\n
        |   ... |   ...    |   ...  |   ...  |
        
    '''
    
    # get _dolar columns
    dolar_columns = [col for col in df.columns if '_dolars' in col]
    # if want to check only on _quantity columns, use:
    #quantity_columns = [col for col in df.columns if '_quantity' in col]
    
    # create new dataframe
    new_df = pd.DataFrame()
    # loop through dolar columns
    for dolar_column in dolar_columns:
        # get year
        year = dolar_column[0:4]
        # get quantity column
        quantity_column = year + '_quantity'
        # create new column with value per dolar
        new_df[year] = df[dolar_column] / df[quantity_column]
    # add country column
    new_df.index = df.index.copy()
    # if nan, replace with 0 (no trade)
    new_df.fillna(0, inplace=True)
    
    return new_df


def sum_countries(df):
    '''
    Sum of all years for all countries in a new dataframe
        one column for the sum of quantity, another for the sum of dolars
    -------
    Parameters:
        df: pandas dataframe
        return: pandas dataframe
        
    Example:
        |  id   |  country |  1990_quantity  |  1990_dolars  |  1991_quantity  |  1991_dolars  |\n
        |  ---  |   ----   |      ----       |     ----      |      ----       |     ----      |\n
        |   1   |  Brasil  |       100       |      1000     |       200       |      2000     |\n
        |   ... |   ...    |       ...       |      ...      |       ...       |      ...      |\n
                        --->\n
        |  country |  quantity  |  dolars  |\n
        |   ----   |    ----    |   ----   |\n
        |  Brasil  |    300     |   3000   |\n
        |   ...    |    ...     |   ...    |
    
    '''
    
    # empty dataframe with countries from column 'country'
    sum_df = pd.DataFrame()
    countries = df['country'].unique().copy()
    # make index of sum_df
    sum_df['country'] = countries
    # set index
    sum_df.set_index('country', inplace=True)
    
    # get _quantity columns sum
    for country in countries:
        # if column has quantity in name, sum
        if '_quantity' in df.columns:
            # sum and put into quantity column of sum_df
            sum_df.iloc[sum_df.index == country, 0] = df[df['country'] == country]['_quantity'].sum(numeric_only=True)
        # if column has dolar in name, sum
        if '_dolar' in df.columns:
            # sum and put into dolar column of sum_df
            sum_df.iloc[sum_df.index == country, 1] = df[df['country'] == country]['_dolar'].sum(numeric_only=True)
            
    return sum_df


def transform_quantity_dolar(df, df_name=None):
    '''
    Transform a dataframe with quantity and dolar columns into a dataframe with 
    only one column for quantity and one for dolar. This is done by summing all coutries.
    -----
    Params:
        df: dataframe
        df_name (optional): str (default None)
            name of the dataframe,
            this will be used to name the columns and index
    Returns:
        df: transformed dataframe
        
    Example:
        |  id   |  country |  1990_quantity  |  1990_dolars  |  1991_quantity  |  1991_dolars  |\n
        |  ---  |   ----   |      ----       |     ----      |      ----       |     ----      |\n
        |   1   |  Brasil  |       100       |      1000     |       200       |      2000     |\n
        |   ... |   ...    |       ...       |      ...      |       ...       |      ...      |\n
                                --->\n
        |  year  |  vinho_quantity |  vinho_dolars |\n
        |  ----  |      ----       |     ----      |\n
        |  1990  |       300       |      3000     |\n
        |   ...  |       ...       |      ...      |
        
    '''
    
    df = pd.DataFrame(df.T.sum(axis=1).copy())
    # rename columns and index for quantity and dolar
    df_dolar = df.query('index.str.contains("dolars")').copy()
    df_dolar.index = df_dolar.index.str.replace('_dolars', '').astype(int)
    
    df_quantity = df.query('index.str.contains("quantity")').copy()
    df_quantity.index = df_quantity.index.str.replace('_quantity', '').astype(int)
    
    if df_name is not None:
            df_dolar.columns = [f'{df_name}_dolars']
            df_quantity.columns = [f'{df_name}_quantity']
            
            df = pd.merge(df_dolar, df_quantity, left_index=True, right_index=True)
    else:
        df_dolar.columns = ['dolars']
        df_quantity.columns = ['quantity']

        df = pd.merge(df_dolar, df_quantity, left_index=True, right_index=True)

    return df



def dolar_per_quantity(df, product_name=None):
    '''
    Calculate dolar per quantity and add new column to dataframe
    ---
    Params:
        df: dataframe
        product_name (optional): str (default None)
            name of the column to be created
    Returns:
        df: dataframe with new column 'dolar_per_quantity'

    '''
    # locate _quantity columns
    dolar_col = df.columns[df.columns.str.contains('dolars')]
    qty_col = df.columns[df.columns.str.contains('quantity')]
    # rename with {product_name} parameter
    if product_name is not None:
        df[f'{product_name}_dolar_per_quantity'] = (df[dolar_col].values / df[qty_col].values).round(3)
    else:
        df['dolar_per_quantity'] = (df[dolar_col].values / df[qty_col].values).round(3)

    return df


# plotting functions
# ------------------


def plot_top_countries_year(df):
    '''
    Plot top 5 countries by unit value of wine exports in each year.
    '''
    for year in df.columns:
        # top 10 countries
        top_5 = df.sort_values(by=year, ascending=False).head(5).T.copy()
    # plot all countries together with seaborn
    fig, ax = plt.subplots(figsize=(12, 6))
    # all top 5 line plot
    sns.lineplot(data=top_5, ax=ax, linewidth=2.5, dashes=False)
    plt.title('Top 5 Países por Exportação -  Valor por Unidade (U$) de Vinho', fontsize=16)
    plt.xlabel('Ano')
    plt.ylabel('Valor Unitário (U$)')
    plt.legend(loc='upper right')
    # max to 15
    plt.yticks(np.arange(0, 16, 3))
    plt.show()
    

def plot_top_countries_quantity(df):
    '''
    Plot top 5 countries by quantity of wine exports in each year.
    '''
    for year in df.columns:
        # top 10 countries
        top_5 = df.sort_values(by=year, ascending=False).head(5).T.copy()
    # plot all countries together with seaborn
    fig, ax = plt.subplots(figsize=(12, 6))
    # all top 5 line plot
    sns.lineplot(data=top_5, ax=ax, linewidth=2.5, dashes=False)
    plt.title('Top 5 Países por Exportação - Quantidade (L) de Vinho', fontsize=16)
    plt.xlabel('Ano')
    plt.ylabel('Quantidade (Litros)')
    plt.legend(loc='upper right')
    # max to 15
    plt.yticks(np.arange(0, 16, 3))
    plt.show()
    
    