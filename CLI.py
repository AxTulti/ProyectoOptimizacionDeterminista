# Library for aestetic CLI
# do:
# pip install questionary
# if not already installed
import questionary 

data_path = 'respuesta_de_encuestas.xlsx'

def binary_question(prompt:str, choices = ['Sí', 'No']) -> bool:
    question = questionary.select(
        prompt,
        choices=choices).ask()
    
    return (question == 'Sí')


def normalize_gender(gender:str):
    if gender == 'Masculino':
        return 'Male'
    if gender == 'Femenino':
        return 'Female'
    if gender == 'Otro':
        return 'Other'
    
    return False

def normalize_age(age:str):
    if age == 'Hasta los 18 años':
        return [0, 18]
    if age == 'Entre 19 y 30 años':
        return [19, 30]
    if age == '31 años o más':
        return [31, 150]
    
    

def ask_gender_segmentation():
    '''
    Returns False if no segmentation is selected
    Returns a tuple containing one or more of the following:
        {'Male', 'Female', 'Other'}
    '''
    do_gender_segmentation = binary_question('¿Desea segmentar por género?')
    if not do_gender_segmentation: return False
    
    selected_genders = questionary.checkbox(
        'Selecciona el género a segmentar:',
        choices=[
            'Masculino',
            'Femenino',
            'Otro'
        ]
    ).ask()
    
    # If no option is selected, we don't segmentate
    if len(selected_genders) == 0: return False
    
    # If all options are selected, we don't segmentate
    if len(selected_genders) == 3: return False
    
    # Cast selection into return format
    selected_genders = [normalize_gender(gender) for gender in selected_genders]
    
    return selected_genders

def ask_age_segmentation():
    '''
    Returns False if no segmentation is selected
    Returns a tuple containing one or more of the following:
        {[0, 18], [19, 30], [30, 150]} Where each interval is inclusive
    '''
    
    do_age_segmentation = binary_question('¿Desea segmentar por rangos de edad?')
    if not do_age_segmentation: return False
    
    selected_ages = questionary.checkbox(
        'Selecciona la edad a segmentar:',
        choices=[
            'Hasta los 18 años',
            'Entre 19 y 30 años',
            '31 años o más'
        ]
    ).ask()
    
    # If no option is selected, we don't segmentate
    if len(selected_ages) == 0: return False
    
    # If all options are selected, we don't segmentate
    if len(selected_ages) == 3: return False
    
    
    # Cast selection into return format
    selected_ages = [normalize_age(age) for age in selected_ages]
    
    return selected_ages
    
def ask_segmentation():
    ''' 
        Returns False if no segmentation is required,
        Returns a tuple according to segmentation choices:
        (genders, ages)
        Where genders is a tuple containing one or more of the following:
        {'Male', 'Female', 'Other'}
        And Age is a tuple containing one or more of the following
        {[0, 18], [19, 30], [30, 150]} Where each interval is inclusive
    '''
    do_segmentation = binary_question('¿Desea segmentar los datos?')
    if not do_segmentation: return False
    
    # Gender
    genders = ask_gender_segmentation()
    
    # Age
    ages = ask_age_segmentation()
    
    return (genders, ages)
